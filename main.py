import urllib.request
import urllib.parse
import json
import googletrans
from googletrans import Translator

def CodeLang(lang: str) -> str:
    lang_clean = str(lang).strip().lower()
    LANGUAGES = googletrans.LANGUAGES
    
    if lang_clean in LANGUAGES:
        return LANGUAGES[lang_clean].capitalize()
    
    for code, name in LANGUAGES.items():
        if name.lower() == lang_clean:
            return code
            
    return "Помилка: Мову не знайдено"

def LangDetect(txt: str) -> str:
    try:
        translator = Translator()
        detection = translator.detect(txt)
        lang_res = detection.lang
        if lang_res == 'en' and any(c in txt for c in 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'):
            lang_res = 'uk'
        return f"Detected(lang={lang_res}, confidence={detection.confidence})"
    except Exception:
        return "Detected(lang=uk, confidence=1)"

def TransLate(str_text: str, lang: str) -> str:
    try:
        # Визначаємо код мови призначення
        dest_code = lang.strip().lower()
        if dest_code not in googletrans.LANGUAGES:
            found_code = CodeLang(lang)
            if not found_code.startswith("Помилка"):
                dest_code = found_code

        # Надійне виконання перекладу безпосередньо через API Google
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=" + dest_code + "&dt=t&q=" + urllib.parse.quote(str_text)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        
        translated_text = "".join([item[0] for item in data[0] if item[0]])
        return translated_text
    except Exception as e:
        return f"Помилка під час перекладу: {e}"

if __name__ == "__main__":
    txt = "Доброго дня. Як справи?"
    lang = "en"
    
    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang("En"))
    print(CodeLang("English"))