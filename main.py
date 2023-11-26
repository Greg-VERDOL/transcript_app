import streamlit as st
import whisper
import os

model = whisper.load_model("base")

def transcribe_file(file):
    abs_file = os.path.abspath(file)
    result = model.transcribe(abs_file)
    return result['text']

def save_uploadedfile(uploadedfile):
     with open(os.path.join("uploads", uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())

result = None
audio_bytes = None
button_gen = None

with st.sidebar:
    uploaded_file = st.file_uploader("Upload un fichier audio", type=("mp3", "wav", "mp4"))
    if uploaded_file is not None: 
        save_uploadedfile(uploaded_file)
        audio_bytes = uploaded_file.read()


if audio_bytes is not None:
    st.audio(audio_bytes, format='audio/ogg')
    button_gen = st.button("Générer la transcription")

if button_gen:     
    result = transcribe_file(f'uploads/{uploaded_file.name}')

if result is not None:
    st.success("Transcription reussie")
    st.write(result)