# J.A.R.V.I.S. MARK 1

J.A.R.V.I.S. (Just A Rather Very Intelligent System) Mark 1 is a voice-controlled virtual assistant powered by a local Ollama AI brain, speech-to-text recognition, offline text-to-speech synthesis (Piper), and a modern desktop web dashboard built with Eel (HTML/CSS/JS).

---

## 🚀 Key Features

* **Interactive HUD Dashboard**: Premium, futuristic glassmorphic UI displaying system metrics, network speed, local weather, and news headlines in real time.
* **Local AI Integration**: Leverages local Ollama model (`gemma:2b`) for intelligence, allowing fully offline conversation features without API costs.
* **Offline High-Quality Speech**: Uses the fast, local neural speech synthesizer **Piper** (`en_US-ryan-medium`) for smooth voice output.
* **Voice Automation Commands**:
  * **Open Apps**: "Run notepad", "Run calculator"
  * **Open Websites**: "Open youtube", "Search Python tutorials"
  * **Media Control**: "Play shape of you" (plays on YouTube)
  * **WhatsApp Messages**: "Send message on whatsapp" (guides through speech input)
  * **System Control & Diagnostics**: "Check system" (reports CPU, RAM, and disk status), "Battery status"
  * **Screenshots**: "Take a screenshot" (saves directly to your Desktop)
  * **Live Information**: "Weather", "News" (reads general news headlines aloud)

---

## 📁 Project Structure

```text
├── app.py                      # Main GUI Entry Point (Eel server & dashboard loop)
├── JARVIS.py                   # Main Voice Assistant Listening & Command Loop
├── requirements.txt            # Python Pip Dependencies
├── build.bat                   # Compilation script for PyInstaller (onedir mode)
├── automation/                 # System automation modules (network, weather, apps, etc.)
├── Brain/                      # Local Ollama AI response handler
├── core/                       # Core Speech-To-Text & Piper Text-To-Speech modules
├── data/                       # Contact lists and persistent data files
├── frontend/                   # HTML/CSS/JS web dashboard files
├── memory/                     # Session history and behavior log JSON files
└── planing/                    # System design blueprints and diagrams
```

---

## 🛠️ Setup & Installation

### Prerequisites
1. **Python**: Python 3.10+ installed on your system.
2. **Ollama**: Download and install [Ollama](https://ollama.com/), then run:
   ```bash
   ollama pull gemma:2b
   ```
3. **Piper TTS**: Download [Piper Windows AMD64](https://github.com/rhasspy/piper/releases), extract it to `C:\piper_windows_amd64\`, and download the `en_US-ryan-medium.onnx` voice model (save both `.onnx` and `.onnx.json` inside the `C:\piper_windows_amd64\piper\models\` folder).

### Step-by-Step Installation

1. Clone or copy this project folder to your local machine.
2. Open a terminal in the project directory and create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - **Command Prompt (CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **PowerShell**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
4. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

---

## 🏃 Running the Application

### 1. Development Mode (Python Script)
Ensure Ollama is running in the background, then execute:
```powershell
python app.py
```
This will launch the futuristic Edge-based dashboard UI and activate JARVIS's voice system.

### 2. Standalone Executable (Production Build)
To compile the application into a single optimized Windows folder containing a launchable `.exe` file without console popups:
1. Run the build automation script:
   ```powershell
   .\build.bat
   ```
2. Navigate to `dist\Jarvis\` and run **`Jarvis.exe`**.
