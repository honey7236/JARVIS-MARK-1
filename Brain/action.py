import os

def execute_command(cmd):
    action = cmd.get("action")

    if action == "open_website":
        target = cmd.get("target")

        if "youtube" in target:
            os.system("start https://www.youtube.com")
            return "Opening YouTube"

        if "google" in target:
            os.system("start https://www.google.com")
            return "Opening Google"

    elif action == "search_google":
        query = cmd.get("target")
        os.system(f"start https://www.google.com/search?q={query}")
        return f"Searching {query}"

    return None