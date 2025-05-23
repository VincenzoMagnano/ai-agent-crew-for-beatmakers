from dotenv import load_dotenv
load_dotenv()

from agents.trend_hunter import get_trend_ideas
from agents.script_writer import write_script
from agents.scene_planner import plan_scenes
from agents.editor_advisor import suggest_editing
from agents.creative_director import review_idea_and_script
from agents.performance_analyst import analyze_performance
from agents.marketing_strategist import generate_distribution_plan
from agents.community_manager import generate_engagement_prompts
from agents.visual_designer import generate_visual_style, generate_visual_prompt
from agents.archivist import check_for_similar_ideas, save_to_archive

# STEP 1: Genera idee
idee = get_trend_ideas("Sto promuovendo un beat west coast con influenze trap.")
idee_split = idee.strip().split("\n")

print("🎯 Idee:")
for idx, idea in enumerate(idee_split, 1):
    print(f"{idx}. {idea}")

scelta = int(input("\n➡️ Scegli il numero dell'idea che vuoi sviluppare: "))
idea_scelta = idee_split[scelta - 1]

# STEP 2: Controlla se è simile ad altre idee
simili = check_for_similar_ideas(idea_scelta)
if simili:
    print("\n⚠️ IDEE SIMILI GIÀ USATE:")
    for sim in simili:
        print(f"- {sim['idea']} (similarità {sim['similarity'] * 100:.0f}%)")

# STEP 3: Script
script = write_script(idea_scelta)
print("\n📝 SCRIPT:\n", script)

# STEP 4: Scene
scenes = plan_scenes(script)
print("\n🎬 SCENE DA GIRARE:\n", scenes)

# STEP 5: Montaggio
editing = suggest_editing(scenes)
print("\n🎥 CONSIGLI MONTAGGIO:\n", editing)

# STEP 6: Feedback Creativo
feedback = review_idea_and_script(idea_scelta, script)
print("\n🎨 FEEDBACK DIRETTORE CREATIVO:\n", feedback)

# STEP 7: Analisi Performance Prevista
performance = analyze_performance(idea_scelta, script)
print("\n📊 ANALISI PERFORMANCE:\n", performance)

# STEP 8: Strategia di Distribuzione
distribution = generate_distribution_plan(idea_scelta, script)
print("\n📣 STRATEGIA DI DISTRIBUZIONE:\n", distribution)

# STEP 9: Community
engagement = generate_engagement_prompts(idea_scelta, script)
print("\n💬 COMMUNITY MANAGEMENT:\n", engagement)

# STEP 10: Visual Design
visual = generate_visual_style(idea_scelta, script)
print("\n🖼️ DIREZIONE VISIVA:\n", visual)

# STEP 11: Prompt per generazione AI
visual_prompt = generate_visual_prompt(idea_scelta, script)
print("\n🎨 PROMPT PER IMMAGINE AI:\n", visual_prompt)

# STEP 12: Salva in archivio
save_to_archive({
    "idea": idea_scelta,
    "script": script,
    "scenes": scenes,
    "visual": visual,
    "prompt": visual_prompt
})
print("\n✅ Contenuto salvato nell’archivio.")