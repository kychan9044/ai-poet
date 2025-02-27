# from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI
import streamlit as st

# load_dotenv()

model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요.")
if st.button("시 작성 요청"):
    with st.spinner('시 작성 중...'):
        result = model.invoke(content + "에 대한 시를 써줘")
        st.write(result.content)