from strands import Agent
from strands.models.litellm import LiteLLMModel
import os
from strands.agent.conversation_manager import SlidingWindowConversationManager


model = LiteLLMModel(
    client_args={
        "api_key": os.getenv("LITELLM_API_KEY"),
        "api_base": os.getenv("LITELLM_API_BASE"),
        "use_litellm_proxy": True
    },
    model_id="gpt-4o-mini",
)

# Create a conversation manager with custom window size
# By default, SlidingWindowConversationManager is used even if not specified
conversation_manager = SlidingWindowConversationManager(
    window_size=10,  # Maximum number of message pairs to keep
)

# Use the conversation manager with your agent
agent = Agent(model=model, conversation_manager=conversation_manager)

response = agent("Hi my name is John Doe")
print(response)

response = agent("What is my name?")
print(response)
