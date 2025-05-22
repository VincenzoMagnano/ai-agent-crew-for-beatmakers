import os
from langchain_google_genai import ChatGoogleGenerativeAI

def write_script(idea: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    query = f"Scrivi uno script breve (max 60 sec) per TikTok basato su questa idea: {idea}"
    return llm.invoke(query).content