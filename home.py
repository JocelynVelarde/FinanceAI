import streamlit as st

st.set_page_config(
        page_title="Asistente Virtual",
        page_icon=":robot_face:",
        layout="wide",
)

st.title("Welcome to your financial assistant")

st.divider()

st.page_link("pages/get started.py", label="Click this button to Get Started", icon="🚀")

st.divider()
st.write("Thanks for using FinanceAI!")
