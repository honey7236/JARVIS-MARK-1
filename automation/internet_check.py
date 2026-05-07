import requests
from core.text_to_speech import speak
from data.DLG_data import online_DLG, offline_DLG
import random

ran_online_DLG = random.choice(online_DLG)
ran_offline_DLG = random.choice(offline_DLG)

def is_online(url = "http://www.google.com", timeout = 5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200 and response.status_code < 300
    
    except requests.ConnectionError:
        return False
    
def internet_status():
    if is_online():
        speak(ran_online_DLG)
        print("sir, i am online and ready to assist you")
    else:
        speak(ran_offline_DLG)
        print("sir i am offline, please check your internet connection")

# network = internet_status()


