# AI Assistant (Offline Voice+Vision Jarvis) - Created by Subikshan P
# Saveetha Engineering College - B.Tech AIML

import pyttsx3
import speech_recognition as sr
import pytesseract
import cv2
import os
import subprocess
from PIL import Image
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from ctransformers import AutoModelForCausalLM

# Text-to-speech function
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

# Recognize voice commands using Google STT (can replace with Whisper later)
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("🔍 Recognizing...")
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service error.")
        return ""

# OCR text reading using webcam + Tesseract
def read_text_from_camera():
    speak("Reading from camera, please hold still...")
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()
    if ret:
        img_path = "temp.jpg"
        cv2.imwrite(img_path, frame)
        text = pytesseract.image_to_string(Image.open(img_path))
        os.remove(img_path)
        return text
    return "Camera read failed."

# Load and split PDF
def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(pages)
    return texts

# Build LangChain retriever with FAISS
def setup_qa_system(docs):
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-Chat-GGML",
                                               model_file="llama-2-7b-chat.ggmlv3.q4_0.bin",
                                               model_type="llama",
                                               max_new_tokens=256,
                                               temperature=0.7)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

# Command handler
def handle_command(cmd, qa_bot):
    cmd = cmd.lower()
    if "read screen" in cmd or "read camera" in cmd:
        text = read_text_from_camera()
        print("📖 OCR Result:", text)
        speak(text)
    elif "open notepad" in cmd:
        subprocess.Popen(["notepad.exe"])
        speak("Opening Notepad.")
    elif "exit" in cmd or "quit" in cmd:
        speak("Goodbye Subikshan.")
        exit()
    else:
        # Assume it's a question to LLM
        print("🤖 Asking AI:", cmd)
        answer = qa_bot.run(cmd)
        print("🧠 AI Answer:", answer)
        speak(answer)

# Main assistant logic
def main():
    speak("Hi Subikshan, your AI assistant is ready.")
    pdf_path = "data.pdf"
    if not os.path.exists(pdf_path):
        speak("Missing data.pdf file.")
        return
    docs = process_pdf(pdf_path)
    qa_bot = setup_qa_system(docs)
    while True:
        command = listen_command()
        if command:
            handle_command(command, qa_bot)

if __name__ == "__main__":
    main()
