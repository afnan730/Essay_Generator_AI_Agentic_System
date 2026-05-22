import os
from dotenv import load_dotenv
load_dotenv()

from agents.image_agent import image_agent

analysis_json = """{
  "sections": [
    {
      "heading": "Historical Roots of Palestinian Rights and the Erosion of Sovereignty",
      "tone": "Informative, somber, critical",
      "keywords": [
        {
          "query": "Jaffa old city historic Palestinian port 1930s documentary",
          "priority": 10
        },
        {
          "query": "British Mandate Palestine map 1947 UN Partition Plan",
          "priority": 9
        },
        {
          "query": "Palestinian refugees Al Nakba 1948 displacement documentary",
          "priority": 9
        },
        {
          "query": "Destruction of Palestinian villages 1948 historical photos",
          "priority": 8
        },
        {
          "query": "Balfour Declaration historical document",
          "priority": 7
        }
      ]
    },
    {
      "heading": "The Ideological Underpinnings of Dispossession and Media Narratives",
      "tone": "Analytical, critical, accusatory",
      "keywords": [
        {
          "query": "Israeli settlements West Bank documentary footage",
          "priority": 10
        },
        {
          "query": "Gaza blockade checkpoints aerial view",
          "priority": 9
        },
        {
          "query": "Zionism historical movement propaganda posters",
          "priority": 8
        },
        {
          "query": "Western news media bias Middle East conflict illustration",
          "priority": 7
        },
        {
          "query": "Palestinian protest against occupation documentary",
          "priority": 7
        }
      ]
    },
    {
      "heading": "The Imperative of Upholding Palestinian Rights and International Law",
      "tone": "Assertive, urgent, legalistic",
      "keywords": [
        {
          "query": "Palestinian flag raised UN General Assembly",
          "priority": 10
        },
        {
          "query": "Palestinian refugees returning to ancestral lands symbolic",
          "priority": 9
        },
        {
          "query": "International Court of Justice mural symbolizing justice",
          "priority": 8
        },
        {
          "query": "Map showing Palestinian territories before and after 1948",
          "priority": 8
        },
        {
          "query": "Protest for Palestinian rights demonstration",
          "priority": 7
        }
      ]
    }
  ]
}"""

print("Invoking image_agent...")
try:
    image_results = image_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": analysis_json
            }
        ]
    })
    
    print("SUCCESS!")
    print("Number of messages:", len(image_results["messages"]))
    for i, msg in enumerate(image_results["messages"]):
        print(f"Message {i} ({type(msg).__name__}):")
        print("  Content:", repr(msg.content))
        if hasattr(msg, "tool_calls"):
            print("  Tool calls:", msg.tool_calls)
except Exception as e:
    print("FAILED with exception:")
    import traceback
    traceback.print_exc()
