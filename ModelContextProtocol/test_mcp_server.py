from mcp import ClientSession
from mcp.client.sse import sse_client


async def check():
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Call add tool
            result = await session.call_tool("add", arguments={"a": 4, "b": 6})
            print(f"The result of 4 + 6 is {result}")

            # Get text code
            result = await session.read_resource("resource://ma_so_thue")
            print("Text code = {}".format(result))

            # Say hi
            result = await session.read_resource("resource://say_hi/Quanisme")
            print("Say hi = {}".format(result))

            # Get prompt
            prompt = await session.get_prompt("review_sentence", arguments={"sentence": "Toi co CCCD la 123456789"})
            print("Prompt = {}".format(prompt))
if __name__ == "__main__":
    import asyncio
    asyncio.run(check())
