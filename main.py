import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
st.title("퀴즈/문제 생성기")
content = st.text_area('퀴즈 생성에 사용될 공부내용','퀴즈 생성에 사용될 공부내용을 입력 또는 복사해서 붙여넣으세요 ...')

if st.button("Make Quizes"):
    with st.spinner("Making Quizes ..."):
        prompt = f'''
        Create a quiz based on the context of {content}. 
        Include a variety of question types such as multiple choice, true/false, and short answer
        to test the participants understanding and knowledge depth.
        Put the answer at the end of each quiz. After finishing to generate quizes, translate them into Korean for print.
        '''
        result = chat_model.predict(prompt) 
    st.write(result)

from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


pdf_docs = st.file_uploader("PDF 문서 여러개 업로드 가능.", accept_multiple_files=True, type=["pdf"])

if st.button("벡터 변환"):
    with st.spinner("변환 중"):
        raw_text = get_pdf_text(pdf_docs)




if st.button("Check"):
    with st.spinner("Checking ..."):
        prompt = f'''
        아래의 삼중백틱으로 구분된 보고서의 내용이 다음과 같은 4가지 맥락평가, 과정평가, 산출평가, 환류 항목에서 
        
        맥락평가 : 세부과제의 목표 및 과제는 내·외부환경 분석, 이해관계자 의견수렴 및 중장기 발전계획을 고려하여 적절히 설정하였는가?
        과정평가 : 세부과제의 구성 및 내용은 계획대비 적절히 이행하였는가? 수립한 계획에 따라 예산을 적절히 집행하였는가?
        산출평가 : 세부과제의 성과지표를 달성하였는가?
        환류 : 우수성과와 개선점을 적절히 도출하였고, 구체적인 확산 및 개선 방안을 도출하였는가?

        살펴본 후에, 적절성을 "매우 그렇지 않다, 그렇지 않다, 중간이다, 그렇다, 매우 그렇다" 중에서 판단하여 다음과 같이 1,2,3,4,5 로 표시하고,
        
        맥락성: 5
        과정평가: 5
        산출평가: 4
        환류: 5  

        최종적으로 검토의견을 한줄로 정리해주세요

```{text}```

        '''
        result = chat_model.predict(prompt) 
    st.write(result)