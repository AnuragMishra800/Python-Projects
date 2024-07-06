from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def main():
    print("Simple Translator")
    print("Supported languages: en (English), es (Spanish), fr (French), de (German), hi (Hindi)")
    
    while True:
        text = input("Enter text to translate (enter 'quit' to exit): ")
        
        if text.strip().lower() == 'quit':
            print("Exiting the translator program.")
            break
        
        dest_language = input("Enter destination language code: ")
        
        if dest_language not in ['en', 'es', 'fr', 'de', 'hi']:
            print("Unsupported language code!")
            continue
        
        try:
            translated_text = translate_text(text, dest_language)
            print(f"Translated text: {translated_text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
