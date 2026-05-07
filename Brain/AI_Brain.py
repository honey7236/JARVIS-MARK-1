import requests

def ai_response(prompt):
    try:
        system_prompt = "You are Jarvis. Speak concisely, confidently, and intelligently. Max 2 lines."

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": f"{system_prompt}\nUser: {prompt}\nJarvis:",
                "stream": False,
                "options": {
                    "num_predict": 40,
                    "temperature": 0.5
                }
            },
            timeout=30
        )

        data = response.json()
        return data.get("response", "I am unable to respond at the moment.")

    except requests.exceptions.ConnectionError:
        return "Connection error. Please ensure Ollama is running."

    except requests.exceptions.Timeout:
        return "Response timed out. Please try again."

    except Exception as e:
        return f"Unexpected error: {str(e)}"
