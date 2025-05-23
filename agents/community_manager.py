import os
from langchain_google_genai import ChatGoogleGenerativeAI

def generate_engagement_prompts(idea: str, script: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    query = f"""
Sei un community manager per un producer musicale che pubblica contenuti Reels/TikTok per promuovere beat rap.

Hai questo contenuto:

IDEA:
{idea}

SCRIPT:
{script}

Genera:
1. 2 call to action (CTA) adatte da dire o scrivere nel video.
2. 3 risposte preimpostate per commenti tipici (es. “Come si chiama il beat?”, “Quanto costa?”, “Lo posso usare?”).
3. 2 domande da inserire nel post o nel commento per stimolare interazione.

Risposte brevi, tono fresco e diretto.
"""
    return llm.invoke(query).content