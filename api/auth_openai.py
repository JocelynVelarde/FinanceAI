import streamlit as st

def getOpenAIkey():
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    return OPENAI_API_KEY

def getAssistant():
    ASSISTANT_ID = st.secrets["ASSISTANT_ID"]
    return ASSISTANT_ID