import json
from datetime import datetime

FILE = "memory/behavior.json"

def log_behavior(event):
    data = load_behavior()
    
    data.append({
        "event": event,
        "time": str(datetime.now())
    })
    
    save_behavior(data)

def load_behavior():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_behavior(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def detect_patterns():
    data = load_behavior()
    
    events = [d["event"] for d in data]
    
    patterns = {}
    
    for e in events:
        patterns[e] = patterns.get(e, 0) + 1

    return patterns
    