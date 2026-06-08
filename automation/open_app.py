import subprocess
import time

def open_app(text):
    import pyautogui as gui
    text = text.lower().replace("run", "").strip()

    try:
        subprocess.Popen(text)

    except Exception:
        gui.press("win")
        time.sleep(0.5)
        gui.write(text)
        time.sleep(0.5)
        gui.press("enter")
    return f"Opening {text}"