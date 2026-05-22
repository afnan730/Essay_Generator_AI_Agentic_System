from dotenv import load_dotenv
load_dotenv()

from agents.research_agent import research_agent
from agents.writer_agent import writer_agent
from agents.analyzer_agent import analyzer_agent
from tools.image_tool import image_search_tool

import json
import re


# ----------------------------
# SAFE JSON PARSER
# ----------------------------
def safe_json_load(text: str):
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    try:
        return json.loads(text.strip())
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("Invalid JSON from LLM")


# ----------------------------
# IMAGE FETCHING LOGIC (NEW - IMPORTANT)
# ----------------------------
def get_image_from_keywords(keywords):
    """
    Try keywords in priority order until image is found.
    """
    for kw in keywords:
        result = image_search_tool.invoke({"query": kw})
        if result.get("image_url"):
            return result["image_url"]

    # FINAL FALLBACK
    return image_search_tool.invoke({
        "query": "palestine documentary"
    }).get("image_url")


# ----------------------------
# MAIN PIPELINE
# ----------------------------
def generate_essay(topic):

    print("\n Step 1: Researching...\n")

    research = research_agent.invoke({
        "messages": [
            {"role": "user", "content": f"Research {topic}"}
        ]
    })

    research_text = research["messages"][-1].content

    print(research_text)
    print("\n Step 2: Writing essay...\n")

    essay = writer_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"""
Use the following research:

{research_text}

Write a structured essay in JSON format.
"""
            }
        ]
    })

    essay_data = safe_json_load(essay["messages"][-1].content)

    print(essay_data)


    print("\n🧠 Step 3: Analyzing essay...\n")

    analysis = analyzer_agent.invoke({
        "messages": [
            {"role": "user", "content": json.dumps(essay_data)}
        ]
    })

    analysis_data = safe_json_load(analysis["messages"][-1].content)
    print(analysis_data)

    print("\n🖼️ Step 4: Fetching images...\n")

    combined_sections = []

    for essay_section, analysis_section in zip(
        essay_data["sections"],
        analysis_data["sections"]
    ):

        heading = essay_section["heading"]
        content = essay_section["content"]

        # extract ordered keywords
        keywords = [
            k["query"]
            for k in analysis_section.get("keywords", [])
        ]
        print(keywords)
        image_url = get_image_from_keywords(keywords)
        print({image_url})

        combined_sections.append({
            "heading": heading,
            "content": content,
            "image_url": image_url
        })


    return {
        "title": essay_data.get("title", topic),
        "sections": combined_sections
    }