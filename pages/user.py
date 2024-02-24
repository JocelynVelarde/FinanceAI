import streamlit as st
from PyPDF2 import PdfReader
from api.processing import process_text, create_agent
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.llms import OpenAI
import tempfile
from pages.admin import get_pdf_file, get_csv_file


st.title("Welcome to the user page")
st.divider()

pdf = st.sidebar.file_uploader('Upload your PDF Document', type='pdf')

st.sidebar.divider()

uploaded_file = st.sidebar.file_uploader('Upload your CSV File', type='csv')

query = st.text_input('Ask a question to the PDF')


contact_agent = st.button('Contact Agent')
if contact_agent:
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file.flush()
            agent = create_agent(tmp_file.name)
            response = agent.run(query)
            st.write("" + response)
        
         
cancel_button = st.button('Find solution')
if cancel_button:
    if pdf is not None:
            pdf_reader = PdfReader(pdf)
            # Text variable will store the pdf text
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            # Create the knowledge base object
            knowledgeBase = process_text(text)
            

            if query:
                docs = knowledgeBase.similarity_search(query)
            
                llm = OpenAI()
                chain = load_qa_chain(llm, chain_type='stuff')
                    
                with get_openai_callback() as cost:
                    response = chain.run(input_documents=docs, question=query)
                    print(cost)
                
                st.write(response)


st.divider()
st.write("Thanks for using FinanceAI!")