import shutil
from datetime import datetime

def backup_files():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M")
    files = {
        "blueprint": "L:/GIT/Projects/AI Vision Command Center/AI Vision Boardroom/blueprint_for_ai.json",
        "summary": "L:/GIT/Projects/AI Vision Command Center/AI Vision Boardroom/master-summary_for_humans.md"
    }
    for name, path in files.items():
        backup_path = f"L:/GIT/Projects/AI Vision Command Center/backup_center/{name}_{now}.bak"
        shutil.copy(path, backup_path)
