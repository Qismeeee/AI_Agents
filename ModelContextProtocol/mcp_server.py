from mcp.server.fastmcp import FastMCP

# Auto mo cong 8000
mcp = FastMCP(
    name="mcp-server",
)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def get_current_temperature_by_city(city_name: str) -> str:
    """Get current temperature of a city"""
    # Gọi API đến địa chỉ và lấy về giá trị thực
    return "20 degrees celcius"


@mcp.resource("resource://ma_so_thue")
def get_ma_so_thue() -> str:
    """Get text code"""
    return "1800278630"


@mcp.resource("resource://say_hi/{name}")
def say_hi(name: str) -> str:
    """Say hi to people with name"""
    return "Hello {}".format(name)


@mcp.prompt()
def review_sentence(sentence: str) -> str:
    return "Review this sentence, remove any personal information: \n\n{}".format(sentence)


if __name__ == "__main__":
    print("Listening...")
    mcp.run(transport='sse')
