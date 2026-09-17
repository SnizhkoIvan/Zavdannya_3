import os, json, re
from my_package import mod2_gtrans3, mod3_deeptr

def process_file():
    config_file = "config.json"
    if not os.path.exists(config_file):
        print("Помилка: Конфігураційний файл відсутній!")
        return
    with open(config_file, "r", encoding="utf-8") as f: config = json.load(f)

    input_filename = config.get("text_file")
    target_lang = config.get("target_lang")
    module_name = config.get("module_name")
    output_type = config.get("output_type")
    max_sentences = config.get("max_sentences", 4)

    if not os.path.exists(input_filename):
        print(f"Помилка: Файл '{input_filename}' відсутній!")
        return

    with open(input_filename, "r", encoding="utf-8") as f: content = f.read()
    sentences = [s.strip() for s in re.split(r'[.!?]+', content) if s.strip()]

    mod = mod3_deeptr if module_name == "mod3_deeptr" else mod2_gtrans3
    detected_lang = mod.LangDetect(content, "lang")

    print(f"--- Інформація про файл ---")
    print(f"Назва файлу: {input_filename}")
    print(f"Розмір файлу: {os.path.getsize(input_filename)} байт")
    print(f"Кількість символів: {len(content)}")
    print(f"Кількість речень: {len(sentences)}")
    print(f"Мова тексту: {detected_lang}\n")

    selected_sentences = sentences[:max_sentences]
    text_to_translate = ". ".join(selected_sentences) + "."
    translated_text = mod.TransLate(text_to_translate, "auto", target_lang)

    if output_type == "screen":
        print("--- Результат перекладу ---")
        print(f"Мова перекладу: {target_lang}")
        print(f"Використаний модуль: {module_name}")
        print(f"Перекладений текст:\n{translated_text}")
    elif output_type == "file":
        out_filename = f"{os.path.splitext(input_filename)[0]}_{target_lang}.txt"
        with open(out_filename, "w", encoding="utf-8") as f: f.write(translated_text)
        print("Ok")

if __name__ == "__main__":
    process_file()
