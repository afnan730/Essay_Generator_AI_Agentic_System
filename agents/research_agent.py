from langchain.agents import create_agent

from config.model import WRITER_MODEL, GEMINI_MODEL
from tools.research_tool import palestine_research_tool


research_agent = create_agent(
    model=GEMINI_MODEL,
    tools=[palestine_research_tool],
    system_prompt="""
You are a research specialist.

Use the research tool to gather:
- history
- legal context
- humanitarian information
- Palestinian rights information
- Nowadays situations

Return concise factual research.
"""
)