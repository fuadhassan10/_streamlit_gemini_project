from google import genai

from dotenv import load_dotenv
from gtts import gTTS
import streamlit as st
import os
import io


#loading the enviroment variable

load_dotenv()

api_key=os.getenv("Gemini_api_key")

#initializing a client

client=genai.Client(api_key=api_key)


#note generator


def note_generator(images):
    prompt=""""Summarize the picture in note format at max 100 words, make sure to add necessary markdown to differentiate different section"""
    response = client.models.generate_content(
                   model="gemini-3.5-flash-lite",
                   contents=[images,prompt]
                   )
    return response.text

    

def audio_transcription(text):
    speech=gTTS(text,lang='en',slow=False)
    audio_buffer=io.BytesIO()

    speech.write_to_fp(audio_buffer)
    st.audio(audio_buffer)

# !Quiz generator

def quiz_generator(image,difficulty):
    prompt=f"Generate 3 quizzes based on the {difficulty}.Make sure to add markdown.Make sure to add currect answer and also i will tick the answer and then you will show the currect answer"

    response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[image,prompt]
    )
    return response.text
