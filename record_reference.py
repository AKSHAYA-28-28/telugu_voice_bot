import sounddevice as sd
import soundfile as sf

fs = 16000
duration = 5  # seconds

print(" Please speak now to save your reference voice")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

sf.write("Akshaya_voice_reference.wav", recording, fs)
print("✅ Saved as Akshaya_voice_reference.wav")
