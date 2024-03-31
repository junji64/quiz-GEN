# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
import streamlit_scrollable_textbox as stx

  
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
st.title("Quiz Generator")
content = stx.scrollableTextbox('Context for Quizes')

if st.button("Make Quizes"):
    with st.spinner("Making quizes ..."):
        prompt = "Create a quiz based on the context of " + content + \
                 ". Include a variety of question types such as multiple choice, true/false, and short answer" + \
                 " to test the participants understanding and knowledge depth."\
                 "Put the answer at the end of each quiz."
        result = chat_model.predict(prompt) 
    st.write(result)