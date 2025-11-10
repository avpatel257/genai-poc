from strands import Agent
from strands.models.litellm import LiteLLMModel
from strands_tools import calculator, current_time, http_request
import os


model = LiteLLMModel(
    client_args={
        "api_key": os.getenv("LITELLM_API_KEY"),
        "api_base": os.getenv("LITELLM_API_BASE"),
        "use_litellm_proxy": True
    },
    model_id="gpt-4o-mini",
)

SYSTEM_PROMPT = """
                You are a helpful assistant, and you can use APIs that don't required auth, you give output in a few lines.
                """
# Create agent with model and tools
print("Creating agent...")
agent = Agent(
    system_prompt=SYSTEM_PROMPT, 
    model=model, 
    tools=[calculator, current_time, http_request],
    )


agent.tool.calculator(expression="123 * 456")

# print("Agent created. You can start chatting with the agent now.")
# user_input = input("Amit: ")

# response = agent(user_input)
print("Agent:", agent.messages)