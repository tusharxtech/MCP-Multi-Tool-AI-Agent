# 🧠 AI Tool Calling Agent using MCP + LangGraph + Ollama

This project demonstrates how to build a **multi-tool AI agent** using:

* **MCP (Model Context Protocol)** servers
* **LangGraph** for agent workflows
* **Ollama (LLaMA 3.2)** as the LLM

The agent can dynamically call external tools (like math functions) via MCP servers and return accurate results.

---

## 🚀 Features

* 🔗 Multi-server MCP integration
* 🧠 LLM-powered reasoning using Ollama
* 🛠️ Dynamic tool calling (Add, Multiply, etc.)
* 🔄 LangGraph workflow-based agent
* ⚡ Async execution support
* 📦 Modular architecture (separate tool servers)

---

## 🏗️ Project Structure

```id="projstruct"
.
├── main.py              # LangGraph agent workflow
├── maths_server.py     # MCP server with math tools
├── weather_server.py   # MCP server (weather - placeholder)
```

---

## 🛠️ Tech Stack

* **Python**
* **LangGraph**
* **LangChain MCP Adapters**
* **Ollama (LLaMA 3.2)**
  

---

## ⚙️ How It Works

1. MCP servers expose tools (e.g., add, multiply)
2. Client connects to these servers using `MultiServerMCPClient`
3. Tools are fetched dynamically
4. LangGraph agent decides:

   * Whether to call a tool
   * Or respond directly
5. ToolNode executes the selected tool
6. Final response is returned to the user

---

## 📂 MCP Tools Implemented

### ➕ Math Server (`maths_server.py`)

* `add(a, b)` → Returns sum
* `multiply(a, b)` → Returns product

### 🌦️ Weather Server (`weather_server.py`)

* Placeholder for weather tool (can be extended)

---

## ⚙️ Installation

### 1. Clone the repository

```id="clone"
git clone https://github.com/your-username/mcp-langgraph-agent.git
cd mcp-langgraph-agent
```

### 2. Install dependencies

```id="install"
pip install -r requirements.txt
```

### 3. Install & Run Ollama

Make sure Ollama is installed and running:

```id="ollama"
ollama run llama3.2:1b
```

---

## ▶️ Run the Project

### Step 1: Start MCP Server

```id="server"
python maths_server.py
```

### Step 2: Run Agent

```id="run"
python main.py
```

---

## 💡 Example Usage

### Input:

```id="ex1"
what is the multiplication of 2 and 4?
```

### Output:

```id="out1"
8
```

---

### Input:

```id="ex2"
what is 5 plus 3?
```

### Output:

```id="out2"
8
```

---

## 🔄 Agent Workflow

* User query → LLM
* LLM decides → Tool call or direct answer
* If tool needed → MCP server executes
* Result → Returned via LangGraph

---

## ⚠️ Notes

* Ensure `maths_server.py` is running before agent
* Uses **stdio transport** for MCP communication
* Weather server is optional (currently not active)

---

## 🔮 Future Improvements

* 🌐 Enable HTTP-based MCP servers (weather API)
* 🧮 Add more tools (division, advanced math)
* 💬 Add conversational memory
* 🧠 Multi-step reasoning improvements
* 🌍 Deploy as API or web app

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit a PR.

---



## 👨‍💻 Author

Your Name
GitHub: https://github.com/tusharxtech
