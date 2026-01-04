import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq


# load env variable
load_dotenv()

# Streamlit page Setup
st.set_page_config(
    page_title='🤖 Chat-Bot',
    page_icon='❄️',
    layout='centered'
)

st.title("🫧 Generative AI ChatBot")

# initiate chat history

if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]


for messages in st.session_state.chat_history:
    with st.chat_message(messages['role']):
        st.markdown(messages['content'])

# initiate LLMs

llm= ChatGroq(model='llama-3.3-70b-versatile',
    temperature=0.0
)

user_prompt=st.chat_input('Ask ChatBot...')

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({'role':'user','content':user_prompt})

    reponse=llm.invoke(
        [{'role':'system','content':'You are a good Assistant'},*st.session_state.chat_history]
    )

    assistant_response=reponse.content
    st.session_state.chat_history.append({'role':'assistant','content':assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)