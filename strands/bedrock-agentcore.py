from strands import Agent
from strands.models.litellm import LiteLLMModel
from strands_tools import calculator, current_time, http_request
from strands.agent.conversation_manager import SlidingWindowConversationManager
import pprint


from bedrock_agentcore.runtime import BedrockAgentCoreApp

import os

# Setup Model
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

# Create agent with model and tools
print("Creating agent...")
agent = Agent(
    model=model, 
    tools=[calculator, current_time, http_request],
    # conversation_manager= conversation_manager
    )

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload: dict):
    user_input = payload.get("prompt")
    response = agent(user_input)
    pprint.pprint(agent.messages)


    return response.message

if __name__ == "__main__":
    print("App is running...")
    app.run()