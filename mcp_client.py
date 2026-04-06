# from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
# from langchain.chat_models import init_chat_model

# import os
# from dotenv import load_dotenv
# load_dotenv()

# import asyncio

# async def main():
#     client=MultiServerMCPClient(
#         {
#             "maths":{
#                 "command":"python",
#                 "args":["maths_server.py"],
#                 "transport":"stdio"
                
#               },
#             # "weather":
#             # {
#             #   "url":"http://127.0.0.1:8000",
#             #   "transport":"streamable-http"
#             # }
#         }
#     )
    
    

#     # # Get tools
#     # tools_result = await client.get_tools()
    
#     # # DEBUG: Print what we actually got
#     # print("=== DEBUG INFO ===")
#     # print(f"Type of tools_result: {type(tools_result)}")
#     # print(f"Length: {len(tools_result)}")
#     # print(f"First item type: {type(tools_result[0])}")
#     # print(f"First item: {tools_result[0]}")
    
#     # if isinstance(tools_result[0], tuple):
#     #     print(f"Tuple length: {len(tools_result[0])}")
#     #     for i, item in enumerate(tools_result[0]):
#     #         print(f"  Tuple[{i}] type: {type(item)}, value: {item}")
    
#     # # PROPER EXTRACTION
#     # tools = []
#     # for item in tools_result:
#     #     if isinstance(item, tuple):
#     #         # Take the tool object from the tuple
#     #         # Usually it's the second element, not the first
#     #         for element in item:
#     #             if hasattr(element, 'name') and hasattr(element, 'description'):
#     #                 tools.append(element)
#     #                 break
#     #     else:
#     #         tools.append(item)
    
#     # print(f"\n=== EXTRACTED TOOLS ===")
#     # print(f"Number of tools: {len(tools)}")
#     # for tool in tools:
#     #     print(f"  - {tool.name}: {tool.description}")

#     tools=await client.get_tools()
#     model=init_chat_model("ollama:llama3.2:1b")

#     agent=create_react_agent(
#         tools,model
#     )

#     maths_response=await agent.ainvoke(
#         {"messages":
#             [{

#             "role":"user",
#             "content":"what is the multiplication of 2 and 4"
#         }]
#          }
#     )
#     print(maths_response["messages"][-1].content)


#     # weather_response=await agent.ainvoke(
#     #     {"messages":
#     #         [{

#     #         "role":"user",
#     #         "content":"what is the weather in delhi "
#     #     }]
#     #      }
#     # )
#     # print(maths_response["messages"][-1].content)

# asyncio.run(main())


from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
import asyncio

async def main():
    # Initialize MCP client
    client = MultiServerMCPClient(
        {
            "maths": {
                "command": "python",
                "args": ["maths_server.py"],
                "transport": "stdio"
            }
        }
    )
    
    # Get tools
    tools = await client.get_tools()
    
    print(f"Loaded {len(tools)} tools:")
    for tool in tools:
        print(f"  - {tool.name}")
    
    # Initialize model
    model = ChatOllama(model="llama3.2:1b", temperature=0)
    llm_with_tools = model.bind_tools(tools)
    
    # Create tool node
    tool_node = ToolNode(tools)
    
    # Define agent node
    def agent_node(state: MessagesState):
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}
    
    # Define conditional edge
    def should_continue(state: MessagesState):
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END
    
    # Build graph
    workflow = StateGraph(MessagesState)
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tool_node)
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue)
    workflow.add_edge("tools", "agent")
    
    # Compile
    agent = workflow.compile()
    
    # Test multiplication
    print("\n=== Testing Multiplication ===")
    result = await agent.ainvoke(
        {"messages": [HumanMessage(content="what is the multiplication of 2 and 4?")]}
    )
    print("Answer:", result["messages"][-1].content)
    
    # Test addition
    print("\n=== Testing Addition ===")
    result = await agent.ainvoke(
        {"messages": [HumanMessage(content="what is 5 plus 3?")]}
    )
    print("Answer:", result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())