import os
import whisper
import torch
import requests
import tempfile
import time
import sounddevice as sd
import soundfile as sf
from gtts import gTTS
from googletrans import Translator
from speechbrain.pretrained import SpeakerRecognition

#  Prevent symlink and permission errors
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"  
os.environ["HF_HUB_ENABLE_HARDLINKS"] = "0"
os.environ["SPEECHBRAIN_LOCAL_DOWNLOAD"] = "True"
os.environ["SPEECHBRAIN_FORCE_DOWNLOAD"] = "True"

# Constants
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2:7b-chat"
REFERENCE_VOICE = "zaki_voice_reference.wav"

#  Load models
whisper_model = whisper.load_model("base")

#  Load speaker verification model (will now download & copy instead of symlink)
verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec"
)

#  Translator
translator = Translator()

def record_audio(duration=4, fs=16000):
    print("🎙️ Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    temp_path = tempfile.mktemp(suffix=".wav")
    sf.write(temp_path, recording, fs)
    return temp_path

def is_verified(audio_path):
    score, _ = verification.verify_files(REFERENCE_VOICE, audio_path)
    score_value = score.item()  # Convert tensor to float
    print(f" Voice match score: {score_value:.4f}")
    return score_value > 0.5

def transcribe(audio_path):
    result = whisper_model.transcribe(audio_path, language="te")
    print("🗣 You said:", result["text"])
    return result["text"]

def ask_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        print(" Raw Ollama response:", response.text)
        data = response.json()
        return data.get("response", "Ollama didn’t respond.")
    except Exception as e:
        print(" Ollama error:", e)
        return "Sorry, I couldn't process that."


def translate_to_telugu(text):
    translated = translator.translate(text, dest='te')
    return translated.text

def speak_telugu(text):
    tts = gTTS(text=text, lang='te')
    filename = tempfile.mktemp(suffix=".mp3")
    tts.save(filename)
    os.system(f'start {filename}' if os.name == 'nt' else f'mpg123 {filename}')

def main():
    print("🤖 Telugu Voice Bot is Ready!")
    while True:
        audio_path = record_audio()
        if not is_verified(audio_path):
            print(" Voice not recognized.")
            continue

        user_input = transcribe(audio_path)

        if not user_input.strip():
            print("❌ Could not understand your voice input.")
            speak_telugu("మీ వాణిని గుర్తించలేకపోయాను. దయచేసి మళ్లీ ప్రయత్నించండి.")
            continue


        if any(x in user_input.lower() for x in ["exit", "quit", "వీడ్కోలు"]):
            speak_telugu("వీడ్కోలు!")
            break

        response = ask_ollama(user_input)
        response_te = translate_to_telugu(response)
        print("🤖 Bot:", response_te)
        speak_telugu(response_te)

if __name__ == "__main__":
    main()
