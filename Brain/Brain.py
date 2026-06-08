import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import webbrowser
import requests

from core.text_to_speech import speak
from core.speech_to_text import listen

from automation.web_opener import open_website
from automation.open_app import open_app
from automation.play_music_youtube import play_music_on_youtube
from automation.battery import battery_alert
from automation.internet_check import internet_status
from automation.system_info import get_system_stats
from automation.weather import get_weather
from automation.whatsapp_automation import send_whatsapp_instant
from Brain.AI_Brain import ai_response
from automation.screenshot import take_screenshot


def processcomand(c):
    if not c or not isinstance(c, str):
        return "Empty command"

    command_text = c.strip().lower()
    if not command_text:
        return "Empty command"

    if "close tab" in command_text:
        import pyautogui
        import time
        time.sleep(0.5)  # small delay (optional)
        pyautogui.hotkey('alt', 'f4')
        return "Closing tab"

    # you can open any website by saying "open" followed by the website name, for example "open youtube"
    if "open" in command_text:
        result = open_website(c)
        # speak(result)
        return result

    # for search command, this function can open google search with the query
    elif command_text.startswith("search"):
        query = command_text.replace("search", "").strip()

        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            response = f"Searching for {query}"
            # speak(response)
            return response
        else:
            response = "What should I search for?"
            # speak(response)
            return response

    # this can open any application by saying "run" followed by the application name, for example "run notepad"
    elif command_text.startswith("run"):
        result = open_app(c)
        # speak(result)
        return result

    # this command will play a random song from the library, you can say "drop my nail" to trigger this command
    # elif "drop my nail" in command_text:
    #     result = play_random_song()
    #     speak(result)
    #     return result

    # this command will play a song on youtube, you can say "play" followed by the song name, for example "play shape of you"
    elif command_text.startswith("play"):
        song = c.replace("play", "", 1).strip()
        play_music_on_youtube(song)
        response = f"Playing {song} on YouTube"
        # speak(response)
        return response

    # this command will check the battery status of your laptop, you can say "battery status" to trigger this command
    elif "battery status" in command_text:
        result = battery_alert()
        if result:
            # speak(result)
            return result
        return "Battery status checked"

    # this command will check the internet status, you can say "internet status" to trigger this command
    elif "internet status" in command_text:
        result = internet_status()
        if result:
            # speak(result)
            return result
        return "Internet status checked"

    # this command will check cpu, ram and disk usage of your system, you can say "check system" to trigger this command
    elif "check system" in command_text:
        stats = get_system_stats()
        # speak(stats)
        return stats

    elif "take a screenshot" in command_text:
        result = take_screenshot()
        # speak(result)
        return result

    # this command will fetch the current weather information, you can say "weather" to trigger this command
    elif "weather" in command_text:
        result = get_weather()
        # speak(result)
        return result

    # this command will fetch the latest news headlines using gnews api, you can say "news" to trigger this command
    elif "news" in command_text:
        newsapi = "5ffb3eafe8f6dd3da8cd3bb041cd0557"
        url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&apikey={newsapi}"

        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])

        if not articles:
            speak("No news available")
            return "No news available"

        headlines = [article.get("title", "") for article in articles]
        for i, title in enumerate(headlines, 1):
            speak(f"{i}. {title}")

        return "News headlines spoken"

    elif "send message on whatsapp" in command_text:
        speak("Whom should I send the message to?")
        receiver = listen()

        speak("What is the message?")
        message = listen()

        if receiver and message:
            result = send_whatsapp_instant(receiver, message)
            # speak(result)
            return result

        return "WhatsApp message canceled"

    elif "exit" in command_text:
        return "exit"

    else:
        output = ai_response(c)
        # speak(output)
        return output

# processcomand("open youtube")
