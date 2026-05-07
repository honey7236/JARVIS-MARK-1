import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
import threading
from datetime import datetime, timedelta
from core.text_to_speech import speak
from automation.whatsapp_automation import send_whatsapp_instant

# 🔥 store reminders
reminders = []


# 🧠 SIMPLE INPUT NORMALIZER
def normalize_time_input(time_input):
    time_input = time_input.lower().strip()

    replacements = {
        "p.m.": "pm",
        "a.m.": "am",
        ".": ":"
    }

    for k, v in replacements.items():
        time_input = time_input.replace(k, v)

    return " ".join(time_input.split())


# 🧠 PARSE TIME
def parse_time(time_input):
    time_input = normalize_time_input(time_input)

    formats = ["%I:%M %p", "%I %p"]

    for fmt in formats:
        try:
            return datetime.strptime(time_input, fmt)
        except:
            pass

    return None


# ⏱ SAVE REMINDER
def save_reminder(task, time_input):
    parsed = parse_time(time_input)

    if not parsed:
        return "❌ Couldn't understand time"

    now = datetime.now()

    remind_time = parsed.replace(
        year=now.year,
        month=now.month,
        day=now.day
    )

    # if time passed → next day
    if remind_time <= now:
        remind_time += timedelta(days=1)

    reminders.append({
        "task": task,
        "time": remind_time
    })

    print("✅ Saved:", task, "at", remind_time.strftime("%I:%M %p"))
    return f"Reminder set for {task} at {remind_time.strftime('%I:%M %p')}"


# 🔔 LOOP
def reminder_loop():
    while True:
        now = datetime.now()

        for r in reminders[:]:
            if now >= r["time"]:
                message = f"Reminder: {r['task']}"
                speak(message)
                send_whatsapp_instant("+916376056667", message)

                # 🔊 Replace with your TTS
                # speak(message)

                # 📱 Replace with your WhatsApp function
                # send_whatsapp_instant("6376056667", message)

                reminders.remove(r)

        time.sleep(5)


# 🚀 START THREAD
def start_reminder_thread():
    thread = threading.Thread(target=reminder_loop, daemon=True)
    thread.start()
    print("🚀 Reminder system started")


# 🧪 TEST
if __name__ == "__main__":
    start_reminder_thread()
    task = input("Enter task: ")
    time_input = input("Enter time (e.g. 1:40 pm): ")
    print(save_reminder(task, time_input))