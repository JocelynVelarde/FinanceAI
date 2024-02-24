import streamlit as st
from PyPDF2 import PdfReader
from api.processing import process_text, create_agent
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.llms import OpenAI
import tempfile

st.write("Welcome to the admin page")
st.divider()

pdf = st.file_uploader('Upload your PDF Document', type='pdf')
uploaded_file = st.file_uploader('Upload your CSV File', type='csv')

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file.flush()
        agent = create_agent(tmp_file.name)

    
if pdf is not None:
        pdf_reader = PdfReader(pdf)
        # Text variable will store the pdf text
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Create the knowledge base object
        knowledgeBase = process_text(text)
        
        query = st.text_input('Ask a question to the PDF')
        cancel_button = st.button('Cancel')
        
        if cancel_button:
            st.stop()
        
        if query:
            docs = knowledgeBase.similarity_search(query)
            response = agent.run(query)
            st.write(response)
        
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type='stuff')
                
            with get_openai_callback() as cost:
                response = chain.run(input_documents=docs, question=query)
                print(cost)
            
            st.write(response)


st.divider()
st.write("Thanks for using FinanceAI!")