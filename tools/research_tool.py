import os

from tavily import TavilyClient
from langchain.tools import tool


client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def palestine_research_tool(query: str) -> str:
    """
    Search for factual information about Palestine.
    """

    response = client.search(
        query=query,
        search_depth="advanced",
        include_domains=[ "aljazeera.net","gaza.is-best.net"],
        max_results=5
    )

    results = []

    for item in response["results"]:

        results.append(
            f"""
TITLE: {item['title']}

CONTENT:
{item['content']}
"""
        )

    return "\n\n".join(results)

    
