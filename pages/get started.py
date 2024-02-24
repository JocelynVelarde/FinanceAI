import streamlit as st

with open('./styles/getstarted.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Get Started with your FinanceAI Chatbot ⭐")
st.divider()

st.markdown("<span style='margin-left: 70px; font-weight: 20px; font-size: 20px'>Follow this instructions to start chatting and solve all your questions immediately</span>", unsafe_allow_html=True)
st.write("1. Click the button to start chatting")
st.write("2. Ask about any potential issue or question you have")
st.write("3. Click on Get Solution to find the best solution for your issue")
st.write("4. You can also contact an agent to solve your issue and we will create the best match for you")

st.divider()
col1, col2, col3 = st.columns(3)

#with col1:
    #st.write("            ")

st.page_link("pages/user.py", label="Click this button to start chatting 🤖")

#with col2:
    #st.image('https://cdn-icons-png.flaticon.com/512/5356/5356355.png', width=500)
    
    

#with col3:
    #st.write('           ')


st.divider()
st.write("Thanks for using FinanceAI 🪙")
