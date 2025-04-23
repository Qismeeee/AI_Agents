from agents.mcp import MCPServerSse
from agents.model_settings import ModelSettings
from agents import Agent, Runner
from agents import set_default_openai_client, set_default_openai_api
from openai import AsyncOpenAI
import os
import sys
import shutil
import asyncio
from dotenv import load_dotenv

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE_URL = os.getenv(
    "OPENAI_API_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

client = AsyncOpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE_URL)
set_default_openai_client(client)
set_default_openai_api("chat_completions")

os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"


async def run(mcp_server: MCPServerSse):
    agent = Agent(
        name="Assistant",
        model=OPENAI_MODEL,
        instructions="Use the tools to answer the questions.",
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="auto"),
    )
    prompt = "What is the temperature in Hanoi?"
    print(f"\nRunning: {prompt}")
    result = await Runner.run(
        starting_agent=agent,
        input=[{"role": "user", "content": prompt}],
        max_turns=10,
    )
    print("Result:", result.final_output)


async def main():
    async with MCPServerSse(
        name="SSE Python Server",
        params={"url": "http://localhost:8000/sse"},
    ) as server:
        await run(server)

if __name__ == "__main__":
    if not shutil.which("uv"):
        raise RuntimeError(
            "uv is not installed. Cài uv theo https://docs.astral.sh/uv/getting-started/installation/"
        )
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
