import os
import threading
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from deep_translator import GoogleTranslator
from google.transliteration import transliterate_text
import keyboard  # To detect keypresses

# Create a dictionary of language names and codes
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "German": "de",
    "French": "fr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa"
}

def get_language_code(prompt):
    print(prompt)
    for idx, (lang, code) in enumerate(language_codes.items(), 1):
        print(f"{idx}. {lang}")

    while True:
        choice = int(input("Choose language by number: "))
        if 1 <= choice <= len(language_codes):
            return list(language_codes.values())[choice - 1]
        else:
            print("Invalid choice, please try again.")

def update_translation(input_lang, output_lang):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Now!\n")
        audio = r.listen(source)
        
        try:
            speech_text = r.recognize_google(audio)
            print(f"Recognized Speech: {speech_text}")

            # Transliterate if necessary
            speech_text_transliteration = transliterate_text(speech_text, lang_code=input_lang) if input_lang not in ('auto', 'en') else speech_text
            print(f"Transliterated Text: {speech_text_transliteration}")

            translated_text = GoogleTranslator(source=input_lang, target=output_lang).translate(text=speech_text_transliteration)
            print(f"Translated Text: {translated_text}")

            # Convert text to speech and play it
            voice = gTTS(translated_text, lang=output_lang)
            voice.save('voice.mp3')
            playsound('voice.mp3')
            os.remove('voice.mp3')
        
        except sr.UnknownValueError:
            print("Could not understand the audio!")
        except sr.RequestError:
            print("Error with the Google API!")

def run_translator():
    input_lang = get_language_code("Select Input Language:")
    output_lang = get_language_code("Select Output Language:")

    print(f"Input Language: {input_lang}, Output Language: {output_lang}")

    while True:
        if keyboard.is_pressed('esc'):  # Check if 'esc' key is pressed
            print("Esc pressed, exiting...")
            break
        
        update_translation(input_lang, output_lang)

if __name__ == "__main__":
    run_translator()
1