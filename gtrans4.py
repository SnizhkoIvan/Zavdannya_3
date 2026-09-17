import asyncio
from my_package import mod1_gtrans4, NAME, AUTHOR
async def main():
    print(f"Пакет: {NAME} | Автор: {AUTHOR}")
    txt = "Доброго дня. Як справи?"
    print("Текст:", txt)
    print("Визначення мови:", await mod1_gtrans4.LangDetect(txt, "all"))
    print("Переклад (en):", await mod1_gtrans4.TransLate(txt, "auto", "en"))
    print("CodeLang('En'):", mod1_gtrans4.CodeLang("En"))
if __name__ == "__main__":
    try: asyncio.run(main())
    except Exception as e: print("Помилка:", e)
