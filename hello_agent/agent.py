import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


class HelloAgent(Agent):
    """A simple agent to greeting with user"""

    async def run(self, user_input):
        return "Hello user! How are you today?"


root_agent = HelloAgent(
    name="hello_agent",
    description="A simple test agent to greeting",
    instruction="Answer user questions to the best of your knowledge",
    model=LiteLlm(
        model="openai/gpt-4o",
        api_key=os.environ["OPENAI_API_KEY"]
    ),
    tools=[]
)
