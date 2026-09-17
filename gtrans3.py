from my_package import mod2_gtrans3, NAME, AUTHOR
if __name__ == "__main__":
    print(f"Пакет: {NAME} | Автор: {AUTHOR}")
    txt = "Доброго дня. Як справи?"
    print("Текст:", txt)
    print("Визначення мови:", mod2_gtrans3.LangDetect(txt, "all"))
    print("Переклад (en):", mod2_gtrans3.TransLate(txt, "auto", "en"))
    print("CodeLang('English'):", mod2_gtrans3.CodeLang("English"))
    print("\nТаблиця мов:")
    print(mod2_gtrans3.LanguageList("screen", "Добрий день"))
