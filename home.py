import streamlit as st

st.set_page_config(
        page_title="Asistente Virtual",
        page_icon=":robot_face:",
)

with open('./styles/home.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title("Chat with your Financial Advisor")
st.caption("Solve all your questions immediately")

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

    st.page_link("pages/get started.py", label="GET STARTED")

with col2:
    st.image('https://static.vecteezy.com/system/resources/previews/029/726/220/non_2x/3d-purple-illustration-icon-of-smartphone-for-online-chatting-and-message-for-ui-ux-social-media-ads-design-free-png.png', width=500)
    
    

with col3:
    st.write(' ')

st.write("Thanks for using FinanceAI!")

