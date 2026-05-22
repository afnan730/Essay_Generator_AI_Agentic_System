from langchain.agents import create_agent

from config.model import LAYOUT_MODEL, GEMINI_MODEL


layout_agent = create_agent(
    model=GEMINI_MODEL,
    tools=[],
    system_prompt="""
You are a professional markdown renderer.

STRICT RULES:
- Return ONLY markdown
- Never explain reasoning
- Never analyze
- Never think aloud

For each section:
- render heading
- render content
- render image below section

Use markdown image syntax.
"""
)