import streamlit as st
from api.assistant_openai import ask_gpt
from api.vision_openai import analyze_image

def file_uploader():
    return st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

st.title("Vision out 💡")

if "messages" in st.session_state:
    # Recurring session
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    message_container = st.container()
    uploaded_file = file_uploader()
else:
    # First time
    st.session_state.messages = []
    uploaded_file = file_uploader()
    message_container = st.container()

if uploaded_file is not None:
    result = analyze_image(uploaded_file)
    with message_container.chat_message("assistant"):
        st.markdown(result)
    st.session_state.messages.append(
        {"role": "assistant", "content": result})
    
if prompt := st.chat_input("Tell me your problem or upload an image to get started! 📸", max_chars=2000):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with message_container.chat_message("user"):
        st.markdown(prompt)

    response = ask_gpt(prompt)

    with message_container.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})