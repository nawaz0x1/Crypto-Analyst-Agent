from phi.agent import Agent
from phi.model.groq import Groq
from agents import web_searcher, article_reader, yahoo_finance_agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    name="Cryptocurrency Analyst",
    team=[web_searcher, article_reader, yahoo_finance_agent],
    instructions=[
        "1. Use the web searcher to find the latest news.",
        "2. Provide the article reader with the top links from the search results to gather important information.",
        "3. Ensure the article reader reviews the links to extract key details.",
        "4. Use the Yahoo Finance agent to retrieve detailed information and analysis.",
        "5. Provide a summary of the analyst recommendations, including quantitative data in a table.",
        "6. Offer investment advice based on the gathered information, presented in a table.",
        "7. Provide both bullish and bearish signals",
    ],
    # reasoning=True,
    debug_mode=True,
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Provide a recommendation for BTC.", stream=True)
