from deep_translator import GoogleTranslator
import langdetect

LANGUAGES_DICT = {'uk': 'Ukrainian', 'en': 'English', 'de': 'German', 'fr': 'French', 'es': 'Spanish'}

def CodeLang(lang: str) -> str:
    lang_clean = str(lang).strip().lower()
    if lang_clean in LANGUAGES_DICT: return LANGUAGES_DICT[lang_clean]
    for code, name in LANGUAGES_DICT.items():
        if name.lower() == lang_clean: return code
    return "Помилка: Мову не знайдено"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = langdetect.detect(text)
        if set == "lang": return lang
        elif set == "confidence": return "1.0"
        else: return f"Language: {lang}, Confidence: 1.0"
    except Exception as e: return f"Помилка: {e}"

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        dest_code = CodeLang(dest)
        if "Помилка" in dest_code: dest_code = dest.lower()
        translated = GoogleTranslator(source='auto', target=dest_code).translate(text)
        return translated
    except Exception as e: return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        lines = [f"{'N':<4} | {'Language':<15} | {'ISO-639 code':<12}" + (f" | {'Text':<30}" if text else ""), "-" * 70]
        idx = 1
        for code, name in LANGUAGES_DICT.items():
            line = f"{idx:<4} | {name:<15} | {code:<12}"
            if text:
                tr = GoogleTranslator(source='auto', target=code).translate(text)
                line += f" | {tr:<30}"
            lines.append(line)
            idx += 1
        output_str = "\n".join(lines)
        if out == "file":
            with open("languages_deeptr.txt", "w", encoding="utf-8") as f: f.write(output_str)
        else: print(output_str)
        return "Ok"
    except Exception as e: return f"Помилка: {e}"
