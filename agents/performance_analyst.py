import os
from langchain_google_genai import ChatGoogleGenerativeAI

def analyze_performance(idea: str, script: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.5,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    query = f"""
Hai il ruolo di analista di performance per contenuti virali su TikTok e Instagram Reels.
Ricevi un’idea e uno script destinati a promuovere un beat rap.

Analizza:
1. Se l’idea è attualmente in linea con i trend noti (challenge, POV, transizioni…)
2. Che tipo di performance aspettarsi (CTR, watch time, engagement)
3. Consigli per migliorarne l’efficacia

IDEA:
{idea}

SCRIPT:
{script}
"""
    return llm.invoke(query).content

def analyze_published_content(caption: str, hashtags: str, views: int, likes: int, comments: int, notes: str = ""):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.5,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    query = f"""
    
Sei un performance analyst specializzato in contenuti social musicali.

Analizza questo contenuto già pubblicato:
- CAPTION: {caption}
- HASHTAG: {hashtags}
- VIEWS: {views}
- LIKES: {likes}
- COMMENTS: {comments}
- FEEDBACK NOTE: {notes}

1. Valuta la performance reale in base ai numeri.
2. Evidenzia punti forti o deboli.
3. Suggerisci come replicare o migliorare il risultato nei prossimi contenuti simili.

Scrivi in tono professionale ma conciso.
"""
    return llm.invoke(query).content