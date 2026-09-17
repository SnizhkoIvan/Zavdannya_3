import os
import re
import locale

# Встановлюємо українську локаль для правильного сортування алфавіту
try:
    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'Ukrainian_Ukraine.1251')
    except locale.Error:
        pass

def ukr_then_en_key(word):
    # Прибираємо розділові знаки для сортування
    clean_word = re.sub(r'[^a-zA-Zа-яА-ЯєЄіІїЇґҐ_]', '', word)
    first_char = clean_word[0] if clean_word else ''
    
    # Визначаємо, чи це кирилиця (українські літери)
    is_ukr = bool(re.match(r'[а-яА-ЯєЄіІїЇґҐ]', first_char))
    
    if is_ukr:
        # 0 = Першочергово українські слова
        return (0, locale.strxfrm(clean_word.lower()))
    else:
        # 1 = Латинські слова
        return (1, clean_word.lower())

def main():
    filename = "text_lab5.txt"
    
    # Завжди перезаписуємо файл з правильним ПІБ
    content = (
        "Сніжко Іван Олександрович\n"
        "Snizhko Ivan\n"
        "Найпопулярнішими продуктами корпорації є операційні системи Microsoft Windows та "
        "єдиний офісний пакет Microsoft Office. Microsoft володіє значними компаніями в інших "
        "частинах ринку, як от кабельна телевізійна мережа MSNBC, інтернет-портал MSN і "
        "мультимедійна енциклопедія Microsoft Encarta."
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    print("--- Вихідний текст ---")
    print(text)
    print("\n----------------------")

    # Розбиваємо текст на окремі слова
    words = re.findall(r'[a-zA-Zа-яА-ЯєЄіІїЇґҐ_]+', text)
    
    # Сортуємо слова (Українські -> Латинські)
    sorted_words = sorted(list(set(words)), key=ukr_then_en_key)

    print("\n--- Відсортований список слів (Українські -> Латинські) ---")
    print(sorted_words)

if __name__ == "__main__":
    main()