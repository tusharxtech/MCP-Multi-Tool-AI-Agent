from mcp.server.fastmcp import FastMCP



mcp=FastMCP("weather")


@mcp.tool()
def weather(a:str)->str:
    """
    Docstring for weather provide weather for input location
    
    :param a: locatiom
    :type a: str
    :return: weather at location a
    :rtype: str
    """

if __name__=="__main__":
    mcp.run(transport="streamable-http")