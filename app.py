import streamlit as st
from api_calling import note_generator
from PIL import Image

from api_calling import audio_transcription
from api_calling import quiz_generator


st.title("Note Summary ands WUiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quzzies")


with st.sidebar:
    st.header("Controls")

    #images
    images=st.file_uploader(
        label="Upload the photos of your note",
        type=['jpg','jpeg','png','HEIC'],
        accept_multiple_files=True
    )
    pil_images=[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if pil_images:
        if len(pil_images) > 3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Your Uploaded Images")
            col = st.columns(len(images))
            
            for i , img in enumerate(images):
                with col[i]:
                    st.image(img)


    #difficulty
    selected=st.selectbox(
        "Enter The Difficulty of your quiz",
        ("easy","medium","hard"),
        index=None
    )
    # if selected:
    #     st.markdown(f" You selected **{selected}** as your difficulty level")
    # else:
    #     st.error("Your must selected a option")

    preesed=st.button("CLick the button to initiate AI",type='primary')

if preesed:
    if not images:
        st.error("You must upload atleast 1 image")
    if not selected:
        st.error("Your must select a difficulty")
         
    if images and selected:

        # ! note er jonno

        with st.container(border=True):
            st.subheader("Your Note")

            #spinner show korar jonno

            with st.spinner("AI is writing notes for you"):
                            
                generated_note=note_generator(pil_images)
                st.markdown(generated_note)



 

        # !audio transcription er jonno
        with st.container(border=True):
            st.subheader("Audio Transcription")
            
            st.text("Audio Will Be Available here")
           
            with st.spinner("AI converting your text to audio,Please Wait"):
               #clearing the markdown
               generated_note = generated_note.replace("#","")
               generated_note = generated_note.replace("*","")
               generated_note = generated_note.replace("-","")
               generated_note = generated_note.replace("'","")

               audio_transscript=audio_transcription(generated_note)

               st.audio(audio_transscript)

        # !quiz er jonno
        with st.container(border=True):
                
                st.subheader(f"Quiz-> {selected} <-label")


                with st.spinner("Ai is generating your quizes"):

                  quizzes=quiz_generator(pil_images,selected)
                  st.text("Quiz Will be shown here")
                  st.markdown(quizzes)