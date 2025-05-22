import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from agents.trend_hunter import get_trend_ideas
from agents.script_writer import write_script
from agents.scene_planner import plan_scenes
from agents.editor_advisor import suggest_editing

st.set_page_config(page_title="AI Beat Promo Assistant", layout="centered")

st.title("🎧 AI Assistant Reels / TikTok per Beatmakers!")
st.subheader("Promuovi i tuoi beat con contenuti creativi generati da agenti AI")

prompt = st.text_input("🔍 Descrivi il contesto del beat (es: trap malinconica, west coast potente...)", "")

if st.button("🎯 Genera Idee"):
    idee_raw = get_trend_ideas(prompt)
    idee_split = idee_raw.strip().split("\n")
    st.session_state.idee = idee_split

if "idee" in st.session_state:
    st.subheader("💡 Idee Generate")
    scelta = st.radio("Scegli l'idea da sviluppare:", st.session_state.idee)

    if st.button("✍️ Scrivi lo script"):
        script = write_script(scelta)
        st.text_area("📝 Script", script, height=200)
        
        scenes = plan_scenes(script)
        st.text_area("🎬 Scene", scenes, height=200)

        editing = suggest_editing(scenes)
        st.text_area("🎥 Suggerimenti di Montaggio", editing, height=200)