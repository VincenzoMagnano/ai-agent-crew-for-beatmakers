from dotenv import load_dotenv
load_dotenv()

from agents.trend_hunter import get_trend_ideas
from agents.script_writer import write_script
from agents.scene_planner import plan_scenes
from agents.editor_advisor import suggest_editing

# STEP 1: Genera idee
idee = get_trend_ideas("Sto promuovendo un beat west coast con influenze trap.")
print("🎯 Idee:", idee)

# STEP 2: Scrivi lo script
script = write_script(idee)
print("\n📝 Script:", script)

# STEP 3: Crea le scene
scenes = plan_scenes(script)
print("\n🎬 Scene:", scenes)

# STEP 4: Suggerisci il montaggio
editing = suggest_editing(scenes)
print("\n🎥 Editing:", editing)