import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import eel
import threading
import sys
from JARVIS import jarvis  # 👈 import function, not file
from automation.internet_check import internet_status
from automation.system_info import get_system_stats
from automation.weather import get_weather
from automation.news import get_news

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)

eel.init(resource_path("frontend"))

# Run jarvis in background
threading.Thread(target=jarvis, daemon=True).start()

eel.start('index.html', mode='edge', host='localhost', port=8000)

# 🔹 GET REAL DATA
network_data = internet_status()
weather_data = get_weather()
news_data = get_news()
system_data = get_system_stats()