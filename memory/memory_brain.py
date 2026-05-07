from long_term import update_profile
from behavior import log_behavior

def learn_from_input(text):
    
    text = text.lower()

    if "i am a" in text:
        profession = text.split("i am a")[-1].strip()
        update_profile("profession", profession)

    if "i like" in text:
        hobby = text.split("i like")[-1].strip()
        update_profile("hobbies", [hobby])

    if "i will go gym" in text:
        log_behavior("gym_commitment")

    if "i skipped gym" in text:
        log_behavior("skip_gym")