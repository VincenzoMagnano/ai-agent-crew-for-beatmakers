import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from agents.trend_hunter import get_trend_ideas
from agents.script_writer import write_script
from agents.scene_planner import plan_scenes
from agents.editor_advisor import suggest_editing
from agents.creative_director import review_idea_and_script
from agents.performance_analyst import analyze_performance, analyze_published_content
from agents.marketing_strategist import generate_distribution_plan
from agents.community_manager import generate_engagement_prompts
from agents.visual_designer import generate_visual_style, generate_visual_prompt
from agents.archivist import check_for_similar_ideas, save_to_archive

# Inizializza session_state
for key in [
    "prompt", "idee", "idea_scelta", "feedback", "performance", "script", 
    "scenes", "editing", "distribution", "engagement", "visual", "visual_prompt"
]:
    if key not in st.session_state:
        st.session_state[key] = ""

st.set_page_config(page_title="AI Beat Promo Assistant", layout="centered")

st.title("🎧 AI Assistant Reels / TikTok per Beatmakers!")
st.subheader("Promuovi i tuoi beat con contenuti creativi generati da agenti AI")

# STEP 1: Prompt
prompt = st.text_input("🔍 Descrivi il contesto del beat", st.session_state.prompt)

if st.button("🎯 Genera Idee"):
    st.session_state.prompt = prompt
    idee_raw = get_trend_ideas(prompt)
    st.session_state.idee = idee_raw.strip().split("\n")

# STEP 2: Idee e valutazione
if st.session_state.idee:
    st.subheader("💡 Idee Generate")
    st.session_state.idea_scelta = st.radio("Scegli l'idea da valutare:", st.session_state.idee)

    if st.button("🔎 Controlla se è già stata usata"):
        simili = check_for_similar_ideas(st.session_state.idea_scelta)
        if simili:
            st.warning("⚠️ Idea simile già presente!")
            for sim in simili:
                st.markdown(f"- {sim['idea']} (**{int(sim['similarity']*100)}%** similarità)")
        else:
            st.success("✅ Nessuna idea simile trovata")

    if st.button("🧠 Valuta l'idea selezionata"):
        st.session_state.feedback = review_idea_and_script(
            st.session_state.idea_scelta, "Script ancora non generato"
        )
        st.session_state.performance = analyze_performance(
            st.session_state.idea_scelta, "Script ancora non generato"
        )

    if st.session_state.feedback and st.session_state.performance:
        st.text_area("🎨 Feedback Direttore Creativo", st.session_state.feedback, height=150)
        st.text_area("📊 Analisi di Performance Prevista", st.session_state.performance, height=200)

        if st.button("🚀 Procedi con questa idea"):
            st.session_state.script = write_script(st.session_state.idea_scelta)
            st.session_state.scenes = plan_scenes(st.session_state.script)
            st.session_state.editing = suggest_editing(st.session_state.scenes)
            st.session_state.distribution = generate_distribution_plan(
                st.session_state.idea_scelta, st.session_state.script
            )
            st.session_state.engagement = generate_engagement_prompts(
                st.session_state.idea_scelta, st.session_state.script
            )
            st.session_state.visual = generate_visual_style(
                st.session_state.idea_scelta, st.session_state.script
            )
            st.session_state.visual_prompt = generate_visual_prompt(
                st.session_state.idea_scelta, st.session_state.script
            )

# STEP 3: Output contenuto completo
if st.session_state.script:
    st.text_area("📝 Script", st.session_state.script, height=200)
    st.text_area("🎬 Scene", st.session_state.scenes, height=200)
    st.text_area("🎥 Suggerimenti di Montaggio", st.session_state.editing, height=200)
    st.text_area("📣 Strategia di Distribuzione", st.session_state.distribution, height=250)
    st.text_area("💬 Coinvolgimento & Risposte ai Commenti", st.session_state.engagement, height=250)
    st.text_area("🖼️ Direzione Visuale", st.session_state.visual, height=250)
    st.text_area("🎨 Prompt per generare copertina AI", st.session_state.visual_prompt, height=150)

    if st.button("💾 Salva in archivio"):
        save_to_archive({
            "idea": st.session_state.idea_scelta,
            "script": st.session_state.script,
            "scenes": st.session_state.scenes,
            "visual": st.session_state.visual,
            "prompt": st.session_state.visual_prompt
        })
        st.success("✅ Contenuto salvato")

# STEP 4: Analisi contenuto pubblicato
with st.expander("📉 Analizza un contenuto già pubblicato"):
    cap = st.text_input("Caption", "Il beat parla da solo...🔥 #westcoast")
    tags = st.text_input("Hashtag", "#westcoast #trap")
    views = st.number_input("Views", 0, step=1, key="views_input")
    likes = st.number_input("Likes", 0, step=1, key="likes_input")
    comments = st.number_input("Commenti", 0, step=1, key="comments_input")
    notes = st.text_area("Osservazioni o feedback ricevuti", key="notes_input")

    if st.button("Analizza performance reale"):
        analysis = analyze_published_content(cap, tags, views, likes, comments, notes)
        st.text_area("📈 Risultato Analisi", analysis, height=300)