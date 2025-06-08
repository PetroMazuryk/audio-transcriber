import os
import whisper

# Шлях до аудіофайлу
AUDIO_FILE_PATH = r"E:\Python\audio-transcriber\R20230701-141838G.wav"

# Функція для видалення повторюваних рядків
def remove_repetitions(text):
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped and (not cleaned or stripped != cleaned[-1].strip()):
            cleaned.append(line)
    return "\n".join(cleaned)

# Основна функція розпізнавання
def transcribe_audio(file_path, output_file="transcription.txt"):
    try:
        print("Поточна директорія:", os.getcwd())
        print(f"Передаю на розпізнавання файл: {file_path}")

        if not os.path.exists(file_path):
            print(f"‼️ Помилка: Файл '{file_path}' не знайдено.")
            return

        model = whisper.load_model("small")
        result = model.transcribe(file_path, language="uk")

        segments = result["segments"]
        text = "\n".join([seg["text"] for seg in segments])
        cleaned_text = remove_repetitions(text)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(f"✅ Розпізнаний текст збережено у файл: {output_file}")
        return cleaned_text

    except Exception as e:
        print(f"❌ Сталася помилка: {e}")

# Точка входу
if __name__ == "__main__":
    transcribed_text = transcribe_audio(AUDIO_FILE_PATH)
    if transcribed_text:
        print("\n📝 Розпізнаний текст:")
        print(transcribed_text)
