import requests

def ai_command(user_input):

    prompt = f"""
You are a command parser.

Return ONLY ONE command.
No explanation.
No extra text.
No sentences.
No formatting.
No markdown.
No quotes.

Output must be exactly one of these formats:

open youtube
run chrome
search <query>
play <song name>
battery status
news
weather
check system
take screenshot
time
date
greet
close tab
none

If unsure → return "none"

Input: {user_input}
Output:
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 40,
                    "temperature": 0.3
                }
            },
            timeout=30
        )

        result = response.json()["response"].strip()
        return result.lower()

    except:
        return "none"


# 🔥 Test
command = ai_command("can you please play the song shape of you for me")
print("Command:", command)