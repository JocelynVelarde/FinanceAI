import streamlit as st
from PyPDF2 import PdfReader
from api.processing import process_text, create_agent
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.llms import OpenAI
import tempfile
from pages.admin import get_pdf_file, get_csv_file

st.write("Welcome to the admin page")
st.divider()

pdf = get_pdf_file()
csv = get_csv_file()


if csv is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(csv.getvalue())
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

