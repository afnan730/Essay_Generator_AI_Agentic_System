from langchain.agents import create_agent

from config.model import ANALYZER_MODEL, GEMINI_MODEL
from tools.image_tool import image_search_tool


image_agent = create_agent(
    model=GEMINI_MODEL,
    tools=[image_search_tool],
    system_prompt="""
You are an image keyword extraction agent.

INPUT:
You receive sections with:
- heading
- keywords (each has query + priority)

TASK:
For each section:
- sort keywords by priority (highest first)
- return ONLY structured JSON

DO NOT:
- call tools
- perform API logic
- do fallback reasoning
- assume image availability

OUTPUT FORMAT:
{
  "sections": [
    {
      "heading": "...",
      "keywords": ["k1", "k2", "k3"]
    }
  ]
}
"""
)