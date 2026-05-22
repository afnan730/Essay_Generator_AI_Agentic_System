from langchain_openrouter import ChatOpenRouter
from langchain_google_genai import ChatGoogleGenerativeAI
from config.keys import (
    KEY1,
    NEW_KEY
)

ANALYZER_MODEL = ChatOpenRouter(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    api_key=KEY1,
    temperature=0.2,
)

WRITER_MODEL = ChatOpenRouter(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    api_key=KEY1,
    temperature=0.2,
    max_tokens=2500,
    streaming=False

)

LAYOUT_MODEL = ChatOpenRouter(
    # model="google/gemma-4-26b-a4b-it:free",
    model="nvidia/nemotron-3-super-120b-a12b:free",
    api_key=NEW_KEY,
    temperature=0.2,
)

GEMINI_MODEL=ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# GEMINI_MODEL=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")







