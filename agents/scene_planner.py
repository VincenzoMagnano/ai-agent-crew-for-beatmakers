import os
from langchain_google_genai import ChatGoogleGenerativeAI

def plan_scenes(script: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    query = f"Dividi questo script in scene da girare. Per ogni scena indica l'inquadratura, cosa deve succedere e se servono props: {script}"
    return llm.invoke(query).content