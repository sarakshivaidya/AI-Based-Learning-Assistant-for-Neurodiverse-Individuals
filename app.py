
import streamlit as st
import tts_model
import stt_model
import flowchart


st.title("AI Learning Assistant")

option = st.selectbox(
    'Choose Feature',
    ('Text to Speech', 'Speech to Text', 'Text to Flowchart')
)

if option == 'Text to Speech':
    user_input = st.text_input("Enter Text:")
    if st.button("Convert"):
        tts_model.text_to_speech(user_input)

elif option == 'Speech to Text':
    if st.button("Start Listening"):
        text = stt_model.speech_to_text()
        st.write("You said: ", text)

elif option == 'Text to Flowchart':
    user_input = st.text_area("Enter Steps separated by . (dot)")
    if st.button("Generate Flowchart"):
        flowchart.generate_flowchart(user_input)
        st.image('flowchart.png')