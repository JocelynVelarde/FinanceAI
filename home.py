import streamlit as st

st.set_page_config(
        page_title="Asistente Virtual",
        page_icon=":robot_face:",
)
st.title("Welcome to FinanceAI 🪙")
st.divider()
st.write("We have multiple amazing features for administrators and users.")
admin_col, user_col = st.columns(2)

with admin_col:
	st.markdown("<span style='text-align: center; font-weight: 20px; font-size: 40px'>Admin</span>", unsafe_allow_html=True)
	st.write('- Upload your own knowledge base about relevant information in your company.')
	st.write('- Additioanlly include a personalized data base with employee information so people can ask about who can solve their problems and be in contact with them.')
	st.write('- With our data vecotirization information can be secure and not wide spread.')
	st.write('- You can also observe metrics on prompt costs and assistant performance.')
	st.write('- Use of personalized agents to determine actions in base of existing data to avoid hallusinations.')

with user_col:
	st.markdown("<span style='text-align: center; font-weight: 20px; font-size: 40px'>User</span>", unsafe_allow_html=True)
	st.markdown("<span style='text-align: left; font-weight: 20px; font-size: 40px'>- Start a conversation with the chatbot.</span>", unsafe_allow_html=True)
	st.markdown('- Ask about relevant information in your company.')
	st.markdown('- Ask about who can solve your problems and be in contact with them.')
	st.markdown('- Receive personalized information about your company and problem solving.')
      
st.divider()

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
    
    

st.divider()

st.write("Thanks for using FinanceAI 🪙")

