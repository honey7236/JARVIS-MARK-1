import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.contact_data import contacts
import webbrowser
import time
from urllib.parse import quote


def send_whatsapp_instant(receiver, message):
    import pyautogui
    try:
        # Check name or number
        phone = contacts.get(receiver.lower(), receiver)

        # Encode message for URL
        encoded_message = quote(message)

        # WhatsApp URL
        url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"

        # Open browser
        webbrowser.open(url)

        # Wait for WhatsApp Web to load
        time.sleep(10)

        # Press Enter to send
        pyautogui.hotkey("enter")

        return f"Message sent to {receiver}"

    except Exception as e:
        print("Error:", e)
        return "Failed to send message"
    

# # # 🔥 Test
# if __name__ == "__main__":
#     send_whatsapp_instant("kirti", "Hello, this is a test message from Jarvis!")