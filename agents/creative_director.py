import os
from langchain_google_genai import ChatGoogleGenerativeAI

def review_idea_and_script(idea: str, script: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.6,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    query = f"""
Sei un direttore creativo. Devi valutare questa idea e questo script per un contenuto TikTok che promuove un beat rap.
Contesto artistico: stile urban, siciliano, professionale, forte identità. Target: artisti indipendenti, giovani produttori.
Valuta: tono, coerenza con brand, originalità, possibilità di engagement.
Dai un feedback in max 5 righe.

Idea:
{idea}

Script:
{script}
    """
    return llm.invoke(query).content