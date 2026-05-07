import json
import requests
from memory.long_term import update_memory

# 🔥 Replace this with your real LLM (Gemma/OpenAI)
def call_llm(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 120,   # increase for better JSON
                    "temperature": 0.3    # lower = more structured output
                }
            },
            timeout=30
        )

        result = response.json()
        return result.get("response", "").strip()

    except Exception as e:
        print("LLM Error:", e)
        return ""

def extract_memory(command):
    
    prompt = f"""
Extract useful long-term user information from this text.

Text:
"{command}"

Return ONLY valid JSON.

Possible fields:
- name (string)
- profession (string)
- goals (list)
- hobbies (list)
- routine (object)
- preferences (object)

If nothing useful, return empty JSON: {{}}
"""

    response = call_llm(prompt)

    try:
        data = json.loads(response)
        return data
    except:
        return {}



def store_extracted_data(data):
    
    for key, value in data.items():
        
        if isinstance(value, list):
            for item in value:
                update_memory(key, item)
        else:
            update_memory(key, value)