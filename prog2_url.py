import urllib.parse
import pyperclip

def decode_url(encoded_url: str) -> str:
    # Декодуємо URL з формату %D0%A8... в читабельну кирилицю
    decoded_url = urllib.parse.unquote(encoded_url)
    return decoded_url

def main():
    # Приклад URL із закодованою кирилицею
    encoded_url = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"
    
    print("Вхідне закодоване посилання:")
    print(encoded_url)
    
    decoded_url = decode_url(encoded_url)
    
    print("\nПеретворене посилання (з кирилицею):")
    print(decoded_url)
    
    # Копіюємо результат у буфер обміну
    try:
        pyperclip.copy(decoded_url)
        print("\nРезультат успішно скопійовано в буфер обміну!")
    except Exception as e:
        print(f"\nНе вдалося скопіювати в буфер обміну: {e}")

if __name__ == "__main__":
    main()