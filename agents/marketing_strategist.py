import os
from langchain_google_genai import ChatGoogleGenerativeAI

def generate_distribution_plan(idea: str, script: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.6,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    query = f"""
Sei uno stratega di marketing per contenuti musicali su TikTok e Instagram Reels.

Hai il seguente contenuto da promuovere:

IDEA:
{idea}

SCRIPT:
{script}

1. Scrivi una caption breve ma impattante per questo Reel (max 2 righe).
2. Suggerisci 5-7 hashtag adatti al target (beatmaker, trap, urban).
3. Indica giorno e ora migliori per pubblicare questo tipo di contenuto.
4. (Bonus) Suggerisci se serve una thumbnail e che stile usare.

Scrivi in stile diretto, adatto ai social.
"""
    return llm.invoke(query).content