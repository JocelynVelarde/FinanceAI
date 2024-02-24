import streamlit as st

with open('./styles/getstarted.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Get Started")
st.write("Click the button to start chatting")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.page_link("pages/user.py", label="START CHAT")

with col2:
    st.image('https://cdn-icons-png.flaticon.com/512/5356/5356355.png', width=500)
    
    

with col3:
    st.write(' ')
st.write("Thanks for using FinanceAI!")
