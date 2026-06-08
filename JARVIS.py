import sys
import os
import time
import re
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

    awake = True
    last_active_time = time.time()
    wake_timeout = 150  # 2.5 minutes inactivity timeout

    while True:
        command = listen()

        if awake:
            if not command:
                # Check for inactivity timeout
                if time.time() - last_active_time > wake_timeout:
                    speak("Going to sleep, sir. Call me if you need me.")
                    try:
                        import eel
                        eel.updateJarvisOutput("Sleeping... Say 'Jarvis' to wake me up.")
                    except:
                        pass
                    awake = False
                continue

            command_lower = command.lower()
            last_active_time = time.time()  # Reset timer on activity

            # Extract actual command if they said "jarvis"
            cleaned_command = re.sub(r'\bjarvis\b', '', command, flags=re.IGNORECASE).strip()
            cleaned_command = re.sub(r'^[,\s]+|[,\s]+$', '', cleaned_command)

            if "jarvis" in command_lower:
                if not cleaned_command:
                    # User just said "jarvis" to keep it awake/check-in
                    speak("Yes, sir?")
                    try:
                        import eel
                        eel.updateJarvisOutput("Yes, sir?")
                    except:
                        pass
                    continue
                else:
                    command_to_process = cleaned_command
            else:
                command_to_process = command

            # Process the command
            add_message("you", command_to_process)
            try:
                import eel
                eel.updateUserInput(command_to_process)
            except Exception as e:
                pass
                
            learn_user(command_to_process)

            response = processcomand(command_to_process)

            add_message("jarvis", response)
            try:
                import eel
                eel.updateJarvisOutput(response)
            except Exception as e:
                pass

            save_session()

            if response == "exit":  
                speak("Shutting down")
                break

            speak(response)

        else:
            # Asleep mode
            if not command:
                continue

            command_lower = command.lower()
            if "jarvis" in command_lower:
                awake = True
                last_active_time = time.time()

                # Extract command in case they said "jarvis do something"
                cleaned_command = re.sub(r'\bjarvis\b', '', command, flags=re.IGNORECASE).strip()
                cleaned_command = re.sub(r'^[,\s]+|[,\s]+$', '', cleaned_command)

                speak("Online and ready, sir.")
                try:
                    import eel
                    eel.updateJarvisOutput("Online and ready, sir.")
                except:
                    pass

                if cleaned_command:
                    command_to_process = cleaned_command
                    
                    # Process the command
                    add_message("you", command_to_process)
                    try:
                        import eel
                        eel.updateUserInput(command_to_process)
                    except Exception as e:
                        pass
                        
                    learn_user(command_to_process)

                    response = processcomand(command_to_process)

                    add_message("jarvis", response)
                    try:
                        import eel
                        eel.updateJarvisOutput(response)
                    except Exception as e:
                        pass

                    save_session()

                    if response == "exit":  
                        speak("Shutting down")
                        break

                    speak(response)
            else:
                # Ignore commands unless they contain "jarvis"
                continue

if __name__ == "__main__":
    jarvis()