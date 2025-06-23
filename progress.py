import json
import os
from datetime import datetime

SAVE_FILE = "data/results.json"

def save_result(level, correct, total):
    os.makedirs("data", exist_ok=True)
    result = {
        "date": str(datetime.now().date()),
        "grade": level,
        "score": f"{correct}/{total}"
    }
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {"history": []}

    data["history"].append(result)
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)