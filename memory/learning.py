from memory.long_term import update_memory

def learn_user(text):
    text = text.lower()

    if "my name is" in text:
        name = text.split("my name is")[-1].strip()
        update_memory("name", name)

    elif "i am a" in text:
        profession = text.split("i am a")[-1].strip()
        update_memory("profession", profession)

    elif "i like" in text:
        hobby = text.split("i like")[-1].strip()
        update_memory("hobbies", hobby)

    elif "my goal is" in text:
        goal = text.split("my goal is")[-1].strip()
        update_memory("goals", goal)

    elif "my college time is" in text:
        time = text.split("my college time is")[-1].strip()
        update_memory("routine", {"college": time})

    elif "i go to gym at" in text:
        time = text.split("i go to gym at")[-1].strip()
        update_memory("routine", {"gym": time})