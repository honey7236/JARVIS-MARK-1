# web_opener.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import webbrowser
from data.Web_Data import websites
from core.text_to_speech import speak


def open_website(command):
    site = command.lower().replace("open", "").strip()

    if not site:
        speak("No website specified")
        return

    if site in websites:
        url = websites[site]
    elif "." in site:
        url = f"https://{site}"
    else:
        url = f"https://www.{site}.com"

    try:
        webbrowser.open(url)
    except:
        webbrowser.open(f"https://www.google.com/search?q={site}")

    return f"Opening {site}"

#test
# open_website("open youtube")