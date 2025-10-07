from typing import Annotated
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
import os

def get_stock_price(symbol: str) -> float:
    '''Return the current price of a stock given the stock symbol
    :param symbol: stock symbol
    :return: current price of the stock
    '''
    return {
        "MSFT": 200.3,
        "AAPL": 100.4,
        "AMZN": 150.0,
        "RIL": 87.6
    }.get(symbol, 0.0)

def buy_stocks(symbol: str, quantity: int, total_price: float) -> str:
    '''Buy stocks given the stock symbol and quantity'''
    return f"You bought {quantity} shares of {symbol} for a total price of {total_price}"



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
    tools=[buy_stocks,get_weather, get_stock_price],
)


def main():
    """Launch the weather agent in dev UI"""

    import logging
    import os
    from agent_framework.devui import serve

    logger = logging.getLogger(__name__)
    logger.info("Startiing dev ui server")

    # Launch server with agent

    serve(entities=[agent], port=8090, auto_open=True)


if __name__ == "__main__":
    main()

    