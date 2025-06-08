import wave
import numpy as np

def generate_test_wav(filename="test.wav", duration=1, freq=440, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * freq * t)

    audio = (tone * 32767).astype(np.int16)

    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)  # моно
        wav_file.setsampwidth(2)  # 16 біт
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio.tobytes())

if __name__ == "__main__":
    generate_test_wav()
    print("Файл test.wav створено")