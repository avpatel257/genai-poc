from strands import Agent
from strands.models.litellm import LiteLLMModel
from strands_tools import calculator, current_time
import os


model = LiteLLMModel(
    client_args={
        "api_key": os.getenv("LITELLM_API_KEY"),
        "api_base": os.getenv("LITELLM_API_BASE"),
        "use_litellm_proxy": True
    },
    model_id="gpt-4o-mini",
)

# Create agent with model and tools
agent = Agent(model=model, tools=[calculator, current_time])

# Message

message = """
I was born in 1990, tell me my age in days.
"""

response = agent(message)
print(response)