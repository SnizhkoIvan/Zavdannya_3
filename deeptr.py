from my_package import mod3_deeptr, NAME, AUTHOR
if __name__ == "__main__":
    print(f"Пакет: {NAME} | Автор: {AUTHOR}")
    txt = "Доброго дня. Як справи?"
    print("Текст:", txt)
    print("Визначення мови:", mod3_deeptr.LangDetect(txt, "all"))
    print("Переклад (en):", mod3_deeptr.TransLate(txt, "auto", "en"))
    print("CodeLang('uk'):", mod3_deeptr.CodeLang("uk"))
    print("\nТаблиця мов:")
    print(mod3_deeptr.LanguageList("screen", "Добрий день"))
