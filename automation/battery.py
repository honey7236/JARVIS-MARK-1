import psutil
import time
from plyer import notification
from core.text_to_speech import speak

def alert100():
    try:
        notification.notify(
            title="Battery Alert",
            message="Battery is fully charged. Please unplug the charger.",
            timeout=1
        )
    except Exception as e:
        print("Notification Error:", e)


def battery_alert():
    try:
        time.sleep(1)
        
        battery = psutil.sensors_battery()
        
        if battery is None:
            speak("Unable to get battery information.")
            return
        
        percentage = int(battery.percent)

        if percentage == 100:
            alert100()
            speak("Battery is fully charged. Please unplug the charger.")

        elif percentage <= 20:
            speak("Battery is low. Please plug in the charger.")

        else:
            speak(f"Battery is at {percentage} percent")

    except Exception as e:
        print("Battery Alert Error:", e)
        speak("Sorry, I could not check the battery status.")

