import speech_recognition as sr
# from text_to_speech import speak

recognizer = sr.Recognizer()

# 🔥 Optimize once (IMPORTANT)
recognizer.energy_threshold = 300      # adjust mic sensitivity
recognizer.dynamic_energy_threshold = False

def listen():
    with sr.Microphone() as source:
        # print("Listening...")

        try:
            # ⚡ Faster listening
            audio = recognizer.listen(
                source,
                timeout=5,              # don't wait forever
                phrase_time_limit=5     # short commands only
            )
        except:
            return ""

    try:
        # ⚡ Faster recognition
        text = recognizer.recognize_google(audio, language="en-IN")
        print("You:", text)
        return text.lower()

    except:
        return ""

# while True:
#     x = listen()
#     speak(x)