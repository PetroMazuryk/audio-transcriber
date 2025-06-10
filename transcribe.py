import os
import re
import whisper

AUDIO_FILE_PATH = r"E:\Python\audio-transcriber\sound\R20230701-121818G.wav"


def remove_repeated_words(text):
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', text, flags=re.IGNORECASE)

def remove_repeated_phrases(text):
    words = text.split()
    result = []
    prev_chunk = []
    for word in words:
        prev_chunk.append(word)
        if len(prev_chunk) > 5:
            chunk = " ".join(prev_chunk[-5:])
            if text.count(chunk) > 3:
                break
        result.append(word)
    return " ".join(result)


def remove_foreign_characters(text):
    return re.sub(r"[^\u0400-\u04FFa-zA-Z0-9\s.,!?–\-]", "", text)


def remove_mostly_english_lines(text):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        cyrillic_count = len(re.findall(r"[а-яА-ЯіІїЇєЄґҐ]", line))
        latin_count = len(re.findall(r"[a-zA-Z]", line))
        if cyrillic_count >= latin_count:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def clean_transcription(text):
    text = remove_repeated_words(text)
    text = remove_repeated_phrases(text)
    text = remove_foreign_characters(text)
    text = remove_mostly_english_lines(text)
    return text.strip()


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
        cleaned_text = clean_transcription(text)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(f"✅ Розпізнаний текст збережено у файл: {output_file}")
        return cleaned_text

    except Exception as e:
        print(f"❌ Сталася помилка: {e}")


if __name__ == "__main__":
    transcribed_text = transcribe_audio(AUDIO_FILE_PATH)
    if transcribed_text:
        print("\n📝 Розпізнаний текст:")
        print(transcribed_text)
