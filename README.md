# Speech to Text (Python)

This is a simple Python project that converts your **speech into text** using the computer’s microphone.  
The recognized text is saved into a file (`output.txt`) and also displayed in the terminal.

---

## Features
- 🎙️ Listens to your microphone and converts speech into text.  
- 📝 Saves everything you say into `output.txt`.  
- ⚡ Handles errors (like background noise or unrecognized speech).  
- 🔁 Keeps running continuously until you stop it.  

---

## 🛠️Technical Stack
- Python 3.13 – Core programming language
- SpeechRecognition – Library to capture audio and convert speech → text
- PyAudio – Connects Python to your microphone (audio input)
- Pyttsx3 – Text-to-speech engine for spoken feedback
- Google Web Speech API (via SpeechRecognition) – Handles speech recognition (requires internet connection)

---

## 📚 Reference
- CS Coach: https://youtu.be/LEDpgye3bf4?si=BjL0U4ONYdUxRoDi
