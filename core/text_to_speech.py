import os
import winsound
import subprocess
import uuid

# Paths
PIPER_PATH = r"C:\piper_windows_amd64\piper\piper.exe"
MODEL_PATH = r"C:\piper_windows_amd64\piper\models\en_US-ryan-medium.onnx"
TEMP_DIR = "temp_audio"

# Ensure temp directory exists
os.makedirs(TEMP_DIR, exist_ok=True)

def speak(text):
    try:
        # Create temp file path
        file_name = f"{uuid.uuid4()}.wav"
        file_path = os.path.join(TEMP_DIR, file_name)

        # Piper command
        command = [
            PIPER_PATH,
            "-m", MODEL_PATH,
            "-f", file_path,
            "--length_scale", str(0.7)
        ]

        # Run Piper
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Communicating with Piper
        process.communicate(input=text)

        # Get absolute path for winsound
        abs_file_path = os.path.abspath(file_path)

        # Play audio using winsound (better for Windows WAV)
        if os.path.exists(abs_file_path):
            winsound.PlaySound(abs_file_path, winsound.SND_FILENAME)
        else:
            print(f"Error: Output file {abs_file_path} was not created.")

        # Delete file after playing
        if os.path.exists(abs_file_path):
            os.remove(abs_file_path)

    except Exception as e:
        print("Error in speak():", e)

# speak("Hello sir i am jarvis")