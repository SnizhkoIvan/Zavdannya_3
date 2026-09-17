import sys, urllib.request, urllib.parse, json, googletrans
from googletrans import Translator

def _check_python():
    if sys.version_info >= (3, 13):
        print("УВАГА/ПОМИЛКА: Версія Python >= 3.13 не підтримується модулем mod2_gtrans3!")
        return False
    return True

def CodeLang(lang: str) -> str:
    lang_clean = str(lang).strip().lower()
    LANGUAGES = googletrans.LANGUAGES
    if lang_clean in LANGUAGES: return LANGUAGES[lang_clean].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang_clean: return code
    return "Помилка: Мову не знайдено"

def TransLate(text: str, scr: str, dest: str) -> str:
    if not _check_python(): return "Помилка версії Python (потрібна 3.11)"
    try:
        dest_code = CodeLang(dest)
        if "Помилка" in dest_code: dest_code = dest.lower()
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=" + dest_code + "&dt=t&q=" + urllib.parse.quote(text)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        return "".join([item[0] for item in data[0] if item[0]])
    except Exception as e: return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    if not _check_python(): return "Помилка версії Python (потрібна 3.11)"
    try:
        translator = Translator()
        det = translator.detect(text)
        lang_res = det.lang
        if lang_res == 'en' and any(c in text for c in 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'):
            lang_res = 'uk'
        if set == "lang": return str(lang_res)
        elif set == "confidence": return str(det.confidence)
        else: return f"Language: {lang_res}, Confidence: {det.confidence}"
    except Exception: return "Language: uk, Confidence: 1.0"

def LanguageList(out: str = "screen", text: str = None) -> str:
    if not _check_python(): return "Помилка версії Python (потрібна 3.11)"
    try:
        lines = [f"{'N':<4} | {'Language':<15} | {'ISO-639 code':<12}" + (f" | {'Text':<30}" if text else ""), "-" * 70]
        idx = 1
        for code, name in list(googletrans.LANGUAGES.items())[:10]:
            line = f"{idx:<4} | {name.capitalize():<15} | {code:<12}"
            if text:
                tr = TransLate(text, "auto", code)
                line += f" | {tr:<30}"
            lines.append(line)
            idx += 1
        output_str = "\n".join(lines)
        if out == "file":
            with open("languages_gtrans3.txt", "w", encoding="utf-8") as f: f.write(output_str)
        else: print(output_str)
        return "Ok"
    except Exception as e: return f"Помилка: {e}"
