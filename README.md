# Telugu Voice Assistant Bot (Offline, AI-Powered)

This is an offline AI-powered voice assistant that recognizes spoken Telugu commands, verifies the speaker, uses a local large language model (LLM) to generate intelligent responses, and speaks the reply in Telugu. It combines Whisper (speech recognition), SpeechBrain (speaker verification), Ollama (local LLM), Google Text-to-Speech, and Google Translate to deliver an interactive voice experience without sending data to the cloud.

## Features

- 🎤 Speech-to-text in Telugu using OpenAI's Whisper
- 🔐 Speaker verification using SpeechBrain
- 🧠 LLM-powered smart replies using Ollama (e.g., LLaMA2 or LLaMA3)
- 🗣 Text-to-speech (Telugu) using Google TTS
- 🔄 English ↔ Telugu translation using `googletrans`
- Fully offline LLM operation (no internet required once models are downloaded)


---

## Project Structure

telugu_voice_bot/
├── telugu_voicebot.py # Main bot script
├── requirements.txt # All Python dependencies
├── Akshaya_voice_reference.wav # Reference voice for speaker verification
├── pretrained_models/ # Folder where SpeechBrain model is downloaded
├── README.md # Project documentation
└── .gitignore # To ignore virtual environment and temp files



---

## System Requirements

| Component      | Minimum                |
|----------------|------------------------|
| OS             | Windows 10/11 or Linux/macOS |
| Python         | 3.8 – 3.11             |
| RAM            | 8 GB recommended       |
| Disk Space     | ~8–10 GB (models + audio) |
| Internet       | Required once for initial model download |
| GPU (optional) | Improves Whisper performance |

---

## Setup Instructions

### 1. Clone or Create Project Folder

Make a folder called `telugu_voice_bot` and place all files inside it.

### 2. Create Virtual Environment

```bash
python -m venv venv
Activate it:

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt
Or install manually:

pip install torch sounddevice soundfile gtts whisper googletrans==4.0.0-rc1 speechbrain requests

4. Install and Configure FFmpeg
Download FFmpeg from gyan.dev, extract it, and add the bin/ path to your system’s PATH variable.

To verify:
ffmpeg -version
5. Install and Run Ollama
Download and install Ollama: https://ollama.com/download

Pull the model:

ollama run llama2:7b-chat
Once running, Ollama will serve your LLM at: http://localhost:11434

6. Add a Reference Voice Sample
Record a 3–4 second .wav clip of your voice and save it as:

Akshaya_voice_reference.wav
This is used to verify your identity.

Running the Bot
Once everything is set up:

python telugu_voicebot.py
Speak in Teluguor English. The bot will:

Recognize your voice

Verify if it matches the reference voice

Transcribe your sentence

Ask the LLM for a response

Translate the reply into Telugu

Speak the reply aloud

Say “exit”, “quit”, or “వీడ్కోలు” to stop the bot.

Commands Summary (Terminal)
Action	Command
Create virtual environment	python -m venv venv
Activate environment	venv\Scripts\activate (Windows)
Install libraries	pip install -r requirements.txt
Pull LLM model	ollama run llama2:7b-chat
Start bot	python telugu_voicebot.py
Export dependencies (optional)	pip freeze > requirements.txt

File Descriptions
File & Purpose
telugu_voicebot.py- Main Python script for recording, verification, transcription, LLM query, and speech output.
requirements.txt- Lists all Python dependencies required to run the bot.
Akshaya_voice_reference.wav- Reference voice used for speaker identity verification.
README.md-  documentation file.
.gitignore- Specifies which files/folders to exclude from Git (e.g., venv/, .mp3)

Troubleshooting
Model hangs or slow? Use a lighter LLM (like llama2:7b) or mock Ollama response temporarily.

Voice not recognized? Re-record the reference clip and ensure clear audio.

Whisper too slow? Switch to a smaller model like tiny or base.en.

Audio device errors? Make sure your mic is set correctly in system settings.

"Ollama didn’t respond" error? Check if Ollama is running properly in another terminal.

Future Improvements
Add wake-word detection

GUI version using Tkinter or PyQt

Faster model switching support

Telugu command-specific actions (e.g., open browser, play music)

