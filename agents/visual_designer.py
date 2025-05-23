import os
from langchain_google_genai import ChatGoogleGenerativeAI

def generate_visual_style(idea: str, script: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    query = f"""
Sei un graphic designer AI per contenuti Reels e TikTok musicali.
Hai il seguente input:

IDEA:
{idea}

SCRIPT:
{script}

Suggerisci:
1. Stile della copertina ideale del reel (thumbnail): cosa mostra, colori dominanti, vibe visiva.
2. Overlay text da inserire nel video: massimo 2 righe potenti, brevi, leggibili da mobile.
3. Font e stile (grassetto? sans serif? tutto maiuscolo?).
4. Emoji o simboli coerenti se utili.
5. Effetti visivi coerenti (grana, glitch, sfocature, ecc.).

Tono: chiaro, sintetico, adatto al pubblico social.
"""
    return llm.invoke(query).content


def generate_visual_prompt(idea: str, script: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.6,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    query = f"""
Genera un prompt per creare una immagine AI coerente con questo contenuto destinato a una thumbnail di un reel musicale.

IDEA:
{idea}

SCRIPT:
{script}

Il prompt deve:
- descrivere l’inquadratura e lo stile visivo
- usare un linguaggio compatibile con generatori di immagini AI (es. "portrait of a man in shadows, urban street background, cinematic lighting")
- riflettere il mood del beat (dark, energico, malinconico, ecc.)
- includere lo stile fotografico (es. "35mm", "cinematic", "studio lighting")

Rispondi con un prompt singolo su una riga.
"""
    return llm.invoke(query).content