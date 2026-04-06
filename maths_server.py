from mcp.server.fastmcp import FastMCP

mcp=FastMCP("maths")

@mcp.tool()
def add(a:int,b:int)->int:
    """
    Docstring for add
    
    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: addition of both a and b
    :rtype: int
    """
    return a+b

@mcp.tool()
def multiply(a:int,b:int)->int:
     """
    Docstring for add
    
    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: multiplication of both a and b
    :rtype: int
    """
     return a*b

if __name__=="__main__":
     mcp.run(transport="stdio")
