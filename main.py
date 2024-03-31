# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

  
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
st.title("퀴즈/문제 생성기")
content = st.text_area('퀴즈 생성에 사용될 공부내용','퀴즈 생성에 사용될 공부내용을 입력 또는 복사해서 붙여넣으세요 ...')

if st.button("Make Quizes"):
    with st.spinner("Making Quizes ..."):
        prompt = "Create a quiz based on the context of " + content + \
                 ". Include a variety of question types such as multiple choice, true/false, and short answer" + \
                 " to test the participants understanding and knowledge depth."\
                 "Put the answer at the end of each quiz. After finishing to generate quizes, translate them into Korean for print."
        result = chat_model.predict(prompt) 
    st.write(result)