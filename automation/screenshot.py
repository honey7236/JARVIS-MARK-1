import pyautogui
import time
import os

def take_screenshot():
    try:
        time.sleep(1)

        # Create Screenshots folder in Documents
        folder = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
        os.makedirs(folder, exist_ok=True)  # create if not exists

        filename = f"screenshot_{int(time.time())}.png"
        path = os.path.join(folder, filename)

        screenshot = pyautogui.screenshot()
        screenshot.save(path)

        return f"Screenshot saved in Documents/Screenshots as {filename}"

    except Exception as e:
        print("Screenshot Error:", e)
        return "Unable to take screenshot"
    
# result = take_screenshot()
# print(result)