# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
st.title("Quiz Generator")
content = st.text_input("Context fo a Quiz")

if st.button("Make a Quiz"):
    with st.spinner("Making a quiz ..."):
        prompt = "Create a quiz based on the context of " + content + 
                 ". Include a variety of question types such as multiple choice, true/false, and short answer" + 
                 " to test the participants understanding and knowledge depth."
        result = chat_model.predict(prompt) 
    st.write(result)