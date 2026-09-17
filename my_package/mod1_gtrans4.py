import sys, googletrans
from googletrans import Translator

def _check_python():
    if sys.version_info < (3, 13):
        raise RuntimeError("Модуль призначений для Python 3.13 і вище!")

def CodeLang(lang: str) -> str:
    lang_clean = str(lang).strip().lower()
    LANGUAGES = googletrans.LANGUAGES
    if lang_clean in LANGUAGES: return LANGUAGES[lang_clean].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang_clean: return code
    return "Помилка: Мову не знайдено"

async def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        _check_python()
        translator = Translator()
        dest_code = CodeLang(dest)
        if "Помилка" in dest_code: dest_code = dest.lower()
        res = await translator.translate(text, dest=dest_code)
        return res.text
    except Exception as e: return f"Помилка: {e}"

async def LangDetect(text: str, set: str = "all") -> str:
    try:
        _check_python()
        translator = Translator()
        det = await translator.detect(text)
        if set == "lang": return str(det.lang)
        elif set == "confidence": return str(det.confidence)
        else: return f"Language: {det.lang}, Confidence: {det.confidence}"
    except Exception as e: return f"Помилка: {e}"

async def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        _check_python()
        translator = Translator()
        lines = [f"{'N':<4} | {'Language':<15} | {'ISO-639 code':<12}" + (f" | {'Text':<30}" if text else ""), "-" * 70]
        idx = 1
        for code, name in list(googletrans.LANGUAGES.items())[:10]:
            line = f"{idx:<4} | {name.capitalize():<15} | {code:<12}"
            if text:
                tr = await translator.translate(text, dest=code)
                line += f" | {tr.text:<30}"
            lines.append(line)
            idx += 1
        output_str = "\n".join(lines)
        if out == "file":
            with open("languages_gtrans4.txt", "w", encoding="utf-8") as f: f.write(output_str)
        else: print(output_str)
        return "Ok"
    except Exception as e: return f"Помилка: {e}"
