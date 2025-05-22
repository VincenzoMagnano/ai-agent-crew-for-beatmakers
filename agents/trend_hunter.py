import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_trend_ideas(prompt: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    query = f"Trova 3 idee originali per TikTok o Instagram Reel per promuovere beat rap. Contesto: {prompt}"
    return llm.invoke(query).content