import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Brain.Brain import processcomand
from core.speech_to_text import listen
from core.text_to_speech import speak
from automation.datetimegreet import greet_user
from memory.short_term import add_message, save_session, load_session
from memory.learning import learn_user

def jarvis():
    speak("initializing JARVIS...")
    greet = greet_user()
    speak(greet)
    load_session()

    while True:
        command = listen()

        if not command:
            continue

        add_message("you", command)         # add input to short term memory
        learn_user(command)               # learn from input if long term memory update required
        # extracted = extract_memory(command) # extract long term memory from input
        # store_extracted_data(extracted)     # store long term memory

        response = processcomand(command)   # process command

        add_message("jarvis", response)     #add output to short term memory

        save_session()                        #save conversation to file

        if response == "exit":  
            speak("Shutting down")
            break

        speak(response)

if __name__ == "__main__":
    jarvis()