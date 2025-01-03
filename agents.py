from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_searcher = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    name="Web Searcher",
    role="Searches the web for information on a topic",
    tools=[DuckDuckGo()],
    markdown=True,
    # add_datetime_to_instructions=True,
)

article_reader = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    name="Article Reader",
    role="Reads articles from URLs.",
    tools=[Newspaper4k()],
    markdown=True,
)

yahoo_finance_agent = Agent(
    name="Yahoo Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
