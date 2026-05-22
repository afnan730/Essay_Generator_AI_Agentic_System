from langchain.agents import create_agent

from config.model import WRITER_MODEL, GEMINI_MODEL


writer_agent = create_agent(
    model=GEMINI_MODEL,
    tools=[],
    system_prompt="""
You are an expert essay writer.

Generate a professional essay about Palestine and their total rights in their lands

IMPORTANT:
Return ONLY valid raw JSON.
DO NOT use:
- ```json
- markdown
- explanations
- comments

FORMAT:

{
  "title": "...",
  "sections": [
    {
      "heading": "...",
      "content": "..."
    }
  ]
}
"""
)