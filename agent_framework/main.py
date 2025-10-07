from typing import Annotated
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
import os

def get_weather(
    location: Annotated[str, "The location to get the weather for."],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny""", "cloudy", "rainy", "stormy"]
    temperature = 53
    return f"The weather in {location} is {conditions[0]} with a high of {temperature}°C."

# Create the agent
agent = ChatAgent(
    name="WeatherAgent",
    description="A helpful agent that provides weather information",
    instructions="You are a weather assistant. Provide current weather information for any location.",
    chat_client=OpenAIChatClient(
        api_key=os.environ.get("MY_OPENAI_API_KEY", ""),
        model_id="gpt-5-nano"
    ),
    tools=[get_weather],
)


def main():
    """Launch the weather agent in dev UI"""

    import logging
    from agent_framework.devui import serve

    logger = logging.getLogger(__name__)
    logger.info("Startiing dev ui server")

    # Launch server with agent

    serve(entities=[agent], port=8090, auto_open=True)


if __name__ == "__main__":
    main()