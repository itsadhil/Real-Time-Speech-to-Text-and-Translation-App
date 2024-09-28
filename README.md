# Real-Time Speech-to-Text and Translation App

## Overview
This is a Python-based GUI application for **real-time speech recognition**, **language translation**, and **text-to-speech synthesis**. The app allows users to input spoken language via a microphone, recognize the speech, translate it to a target language, and then speak the translated text back. The app uses several libraries, including Google Speech Recognition, Google Text-to-Speech (gTTS), and Google Translator.

## Features
- **Real-time speech recognition**: Recognizes spoken words using Google's speech recognition API.
- **Language translation**: Translates the recognized text into multiple languages.
- **Text-to-speech synthesis**: Converts the translated text back into speech.
- **Graphical User Interface (GUI)**: Built with Tkinter for ease of use.
- **Support for multiple languages**: Choose from a variety of input and output languages.
- **Transliteration**: Option to transliterate non-Latin characters into their respective scripts.

## Prerequisites
To run this project, ensure that you have Python 3.6+ installed, as well as the following Python libraries:

### Required Libraries
Install the necessary Python dependencies using the command:
```bash
pip install gtts tkinter speechrecognition playsound deep-translator googletrans==4.0.0-rc1
