import os
import json
from difflib import SequenceMatcher

ARCHIVE_PATH = "archive.json"

def load_archive():
    if not os.path.exists(ARCHIVE_PATH):
        return []
    with open(ARCHIVE_PATH, "r") as f:
        return json.load(f)

def save_to_archive(entry: dict):
    archive = load_archive()
    archive.append(entry)
    with open(ARCHIVE_PATH, "w") as f:
        json.dump(archive, f, indent=2)

def check_for_similar_ideas(new_idea: str, threshold: float = 0.6):
    archive = load_archive()
    similar = []
    for entry in archive:
        ratio = SequenceMatcher(None, new_idea.lower(), entry.get("idea", "").lower()).ratio()
        if ratio >= threshold:
            similar.append({
                "idea": entry.get("idea"),
                "similarity": round(ratio, 2)
            })
    return similar