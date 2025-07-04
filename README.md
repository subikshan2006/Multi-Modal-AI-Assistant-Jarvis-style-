# 🤖 Offline AI Assistant using Voice, Vision & LLaMA (Jarvis-Style)

Hi, I’m Subikshan P, an AIML undergrad at Saveetha Engineering College 👋  
This is a project I built during my 2nd year — my own version of **JARVIS**, a fully offline AI assistant that:

- Listens to your voice 🎙️  
- Sees using webcam and OCR 👁️  
- Answers from documents using local LLaMA 🧠  
- Speaks responses using TTS 🗣️  
- Runs commands like opening apps ⚙️

---

## 💡 Why I Built This

I was inspired by Iron Man’s JARVIS and wanted to see how far I could go with just open-source tools — no OpenAI API, no cloud.  
Everything works 100% offline using Python and a locally loaded LLaMA 2 model.

---

## 🔧 Features

- 🎤 Voice input (SpeechRecognition)
- 🧠 Local document Q&A with LLaMA 2 + LangChain + FAISS
- 📷 Read text from webcam using OCR (Tesseract + OpenCV)
- 🗨️ Speak back using pyttsx3
- ⚙️ Voice-controlled system commands (e.g. open Notepad)

---

## 🧠 Tech Stack

| Task                | Library/Tool                       |
|---------------------|------------------------------------|
| Voice Input         | `speech_recognition`               |
| TTS Output          | `pyttsx3`                          |
| PDF QA              | `LangChain`, `FAISS`, `ctransformers`, `sentence-transformers` |
| OCR from Camera     | `OpenCV`, `Pillow`, `pytesseract`  |
| System Control      | `subprocess` (for launching apps)  |

Runs on **Python 3.11**  
Tested on **Windows 11**

---

## 🛠 How to Set Up

### 1. Install Libraries

```bash
pip install pyttsx3 speechrecognition pytesseract opencv-python pillow langchain faiss-cpu sentence-transformers ctransformers
Also install Tesseract OCR (Windows)

2. Add These Files in Folder
main.py (the assistant)

data.pdf (any PDF you want it to read from)

llama-2-7b-chat.ggmlv3.q4_0.bin (download from Hugging Face — 3GB)

3. Run It
bash
Copy
Edit
python main.py
Then speak your query like:

“What is AI?”

“Open Notepad”

“Read screen”

“Exit”

🔍 Sample Use Cases
Ask it questions from your college notes PDF

Capture a page using your webcam and make it read aloud

Launch desktop apps via voice

🧪 Things I Learned
How vector databases (FAISS) store and retrieve semantic chunks

LLaMA is super slow without optimization — lowered tokens

Mic input is tricky on noisy laptops 😅

How to integrate 3 AI models into one working system

📈 To Improve Later
Switch from Google STT to Whisper

Add facial unlock or emotion detection

Add Streamlit or Tkinter GUI

Try connecting with Arduino for hardware control

```

👨‍💻 Author

Subikshan P

B.Tech Artificial Intelligence & Machine Learning (Class of 2027)

Saveetha Engineering College, Chennai
