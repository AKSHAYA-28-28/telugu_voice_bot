# Telugu Voice Assistant Bot

This project is a voice-activated assistant that responds in Telugu. It performs speaker verification, transcribes voice input using OpenAI Whisper, generates responses via a local Ollama language model, and delivers responses through Google Text-to-Speech (gTTS) in Telugu.

---

## Features

- **Speaker Verification**: Ensures responses are only triggered by the authorized user using SpeechBrain ECAPA-VOX model.
- **Speech Recognition**: Uses OpenAI Whisper for transcription of Telugu voice input.
- **Local LLM Integration**: Supports response generation via local Ollama models (LLaMA2 or LLaMA3).
- **Translation to Telugu**: English responses from the model are translated to Telugu using Google Translate API.
- **Speech Output**: Final Telugu response is synthesized and spoken using gTTS.

---

## System Requirements

- Python 3.10 or later
- 4.5 GB+ system RAM (for running `llama2:7b-chat`)
- Ollama installed and properly configured
- FFmpeg installed and added to system PATH
- Reference voice `.wav` file of the user (used for authentication)

---

## Installation Instructions

### 1. Clone the Repository

``bash
git clone https://github.com/<your-username>/telugu_voice_bot.git
cd telugu_voice_bot

2. Set Up a Virtual Environment
python -m venv venv
venv\Scripts\activate  # On Windows


3. Install Python Dependencies
pip install -r requirements.txt

4. Install FFmpeg
Download from: https://www.gyan.dev/ffmpeg/builds/

Extract the contents.

Add the extracted bin/ folder to the Windows PATH environment variable.

5. Install and Configure Ollama
Install Ollama from: https://ollama.com

Start the Ollama server:
ollama run llama2:7b-chat
Make sure it is accessible at http://localhost:11434/

6. Place Voice Reference File
Record a 3–5 second clip of your own voice.

Save it in the root directory as zaki_voice_reference.wav.

Running the Bot
After all setup is complete, run the assistant:
python telugu_voicebot.py
Wait for the bot to say "Listening..."

Speak a query in Telugu or English.

If voice verification passes, it will transcribe, respond, translate to Telugu, and speak it aloud.

To exit, say "exit", "quit", or "వీడ్కోలు".

File Descriptions
telugu_voicebot.py -	Main script to run the Telugu voice assistant.
requirements.txt- List of required Python libraries.
README.md -	Project documentation and setup guide.
.gitignore - Specifies files and folders to be excluded from Git version control.
Akshaya_voice_reference.wav-A short recording of the authorized user's voice for speaker verification.

Notes
This bot uses Whisper in CPU mode and defaults to FP32 precision.

If the system does not have enough memory to run llama2:7b-chat, consider switching to a smaller model such as llama3.

Ensure network access is available for gTTS and Google Translate to function.

