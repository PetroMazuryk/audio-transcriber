import os
import whisper

print("Поточна директорія:", os.getcwd())

def transcribe_audio(file_path, output_file="transcription.txt"):
    try:
        print(f"Передаю на розпізнавання файл: {file_path}")
        
        if not os.path.exists(file_path):
            print(f"‼️ Помилка: Файл '{file_path}' не знайдено.")
            return

        model = whisper.load_model("base")
        result = model.transcribe(file_path, language="uk")

        # Отримуємо текст з поділом на сегменти
        segments = result["segments"]
        text = "\n".join([seg["text"] for seg in segments])

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Розпізнаний текст збережено у файл: {output_file}")
        return text

    except Exception as e:
        print(f"❌ Сталася помилка: {e}")

if __name__ == "__main__":
    audio_file = r"E:\Python\open\R20230701-101802G.wav"
    transcribed_text = transcribe_audio(audio_file)
    if transcribed_text:
        print("\n📝 Розпізнаний текст:")
        print(transcribed_text)