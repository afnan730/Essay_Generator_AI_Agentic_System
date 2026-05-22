# import json

# from dotenv import load_dotenv

# load_dotenv()

# from agents.research_agent import research_agent
# from agents.writer_agent import writer_agent
# from agents.analyzer_agent import analyzer_agent
# from agents.image_agent import image_agent
# from agents.layout_agent import layout_agent


# TOPIC = "Palestine and Palestinian rights"


# print("Running research agent...")

# research = research_agent.invoke({
#     "messages": [
#         {
#             "role": "user",
#             "content": f"Research {TOPIC}"
#         }
#     ]
# })

# research_text = research["messages"][-1].content
# print(research_text)

# print("Generating essay...")

# essay = writer_agent.invoke({
#     "messages": [
#         {
#             "role": "user",
#             "content": f"""
# Use this research:

# {research_text}

# Generate essay.
# """
#         }
#     ]
# })

# essay_json = essay["messages"][-1].content
# print(essay_json)

# print("Analyzing paragraphs...")

# analysis = analyzer_agent.invoke({
#     "messages": [
#         {
#             "role": "user",
#             "content": essay_json
#         }
#     ]
# })

# analysis_json = analysis["messages"][-1].content

# print(analysis_json)
# print("Searching images...")

# image_results = image_agent.invoke({
#     "messages": [
#         {
#             "role": "user",
#             "content": analysis_json
#         }
#     ]
# })

# images_json = image_results["messages"][-1].content

# print(images_json)

# import re
# import json

# def clean_json(text: str) -> str:
#     # remove ```json and ```
#     text = re.sub(r"```json", "", text)
#     text = re.sub(r"```", "", text)
#     return text.strip()

# essay_data = json.loads(clean_json(essay_json))
# images_data= json.loads(clean_json(images_json))


# print('organizing essay...')
# combined_sections = []

# for section, image in zip(
#     essay_data["sections"],
#     images_data["sections"]
# ):

#     combined_sections.append({
#         "heading": section["heading"],
#         "content": section["content"],
#         "image_url": image["image_url"]
#     })


# final_data = {
#     "title": essay_data["title"],
#     "sections": combined_sections
# }


# print("Generating final layout...")


# import streamlit as st

# st.set_page_config(
#     page_title=final_data["title"],
#     layout="wide"
# )

# st.title(final_data["title"])

# for section in final_data["sections"]:

#     st.header(section["heading"])

#     st.image(
#         section["image_url"],
#         use_container_width=True
#     )

#     st.write(section["content"])

#     st.divider()
#     st.sidebar.title("Sections")
# st.download_button(...)
    


# # markdown = layout_agent.invoke({
# #     "messages": [
# #         {
# #             "role": "user",
# #             "content": json.dumps(final_data)
# #         }
# #     ]
# # })

# # final_markdown = markdown["messages"][-1].content


# # with open("output.md", "w", encoding="utf-8") as file:
# #     file.write(final_markdown)


# print("Done.")