import json

FILE = "memory/long_term.json"


def load_memory():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "name": "",
            "profession": "",
            "goals": [],
            "hobbies": [],
            "routine": {},
            "preferences": {}
        }


def save_memory(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# 🔥 Core function (smart update)
def update_memory(key, value):
    data = load_memory()

    # handle lists (goals, hobbies)
    if isinstance(data.get(key), list):
        if value not in data[key]:
            data[key].append(value)

    # handle dict (routine, preferences)
    elif isinstance(data.get(key), dict):
        data[key].update(value)

    # handle simple values (name, profession)
    else:
        data[key] = value

    save_memory(data)


def get_memory():
    return load_memory()