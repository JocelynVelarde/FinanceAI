import streamlit as st
from PyPDF2 import PdfReader
from api.processing import process_text, create_agent
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.llms import OpenAI
import tempfile
import time


def chat(pdf, uploaded_file):
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy un asistente virtual especializado en serivicios financieros ¿En qué puedo ayudarte? "}]

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    if query := st.chat_input():
        
        if pdf is not None:
            pdf_reader = PdfReader(pdf)
            # Text variable will store the pdf text
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            # Create the knowledge base object
            knowledgeBase = process_text(text)
            st.session_state["messages"].append({"role": "user", "content": query})
            st.chat_message("user").write(query)
            docs = knowledgeBase.similarity_search(query)
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type='stuff')

            with get_openai_callback() as cost:
                        response = chain.run(input_documents=docs, question=query)
                        print(cost)
            
            st.session_state["messages"].append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
            st.divider()
            st.write("Not happy with your answer?")
            # Apartado de la base de datos
            if st.button('Contact Agent'):
                st.write("hello")
                if uploaded_file is not None:
                    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_file.flush()
                        agent = create_agent(tmp_file.name)
                        agent_response = agent.run(query)
                        print("Agent response:", agent_response)
                        st.session_state["messages"].append({"role": "assistant", "content": agent_response})
                        st.chat_message("assistant").write(agent_response)
                        print("Agent response written to chat.")





def sidebar():
    pdf = st.sidebar.file_uploader('Upload your PDF Document', type='pdf')

    st.sidebar.divider()

    uploaded_file = st.sidebar.file_uploader('Upload your CSV File', type='csv')
    return pdf, uploaded_file


st.title("Type in your question and we will find the best solution for you! 🚀")
st.divider()


def main():
    pdf, uploaded_file=sidebar()
    chat(pdf, uploaded_file)


main()




             