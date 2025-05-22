import os
from langchain_google_genai import ChatGoogleGenerativeAI

def suggest_editing(scenes: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    query = f"Per queste scene, suggerisci effetti, transizioni, testo da sovrapporre, musica o cut tipici dei contenuti virali: {scenes}"
    return llm.invoke(query).content