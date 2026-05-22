import os
import requests
from langchain.tools import tool

IMAGE_CACHE = {}
MAX_CALLS = 3
call_count = 0


@tool
def image_search_tool(query: str) -> dict:
    """
    Search for relevant images (cached + limited).
    Returns structured result.
    """

    global call_count

    # 🔥 1. CACHE CHECK
    if query in IMAGE_CACHE:
        return IMAGE_CACHE[query]

    # 🔥 2. HARD LIMIT (VERY IMPORTANT)
    if call_count >= MAX_CALLS:
        return {
            "url": None,
            "error": "API limit reached"
        }

    url = "https://api.unsplash.com/search/photos"

    response = requests.get(
        url,
        params={
            "query": query,
            "per_page": 1
        },
        headers={
            "Authorization": f"Client-ID {os.getenv('UNSPLASH_ACCESS_KEY')}"
        }
    )

    data = response.json()
    call_count += 1

    if not data.get("results"):
        return {"url": None}

    result = {
        "image_url": data["results"][0]["urls"]["regular"],
        "query": query
    }

    # 🔥 3. SAVE TO CACHE
    IMAGE_CACHE[query] = result

    return result