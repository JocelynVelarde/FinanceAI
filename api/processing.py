from langchain_openai import OpenAI
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain_community.callbacks import get_openai_callback
from langchain.agents.agent_types import AgentType

load_dotenv()
os.environ["OPENAI_API_KEY"] = "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"


# Función para crear el agente
def create_agent():
    # Crea el agente utilizando create_csv_agent() u otra función similar
    agent=create_csv_agent(llm=OpenAI(temperature=0),path=r"C:\Users\Poncho\Documents\FinanceAI\api\employee_data.csv",verbose=True,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    return agent

# Función para procesar el texto y crear la base de conocimientos
def process_text(text):
    # Split the text into chunks using langchain
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Convert the chunks of text into embeddings to form a knowledge base
    embeddings = OpenAIEmbeddings()
    knowledgeBase = FAISS.from_texts(chunks, embeddings)
    
    return knowledgeBase

def main():
    st.title("Respuesta de Ambos")
    
    pdf = st.file_uploader('Upload your PDF Document', type='pdf')
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
            agent = create_agent()
            agent_response=agent.run(query)
            docs = knowledgeBase.similarity_search(query)
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type='stuff')
            
            with get_openai_callback() as cost:
                knowledge_response = chain.run(input_documents=docs, question=query)
                print(cost)
            integrated_response = f"Agente: {agent_response}\n\nProcesador de Texto: {knowledge_response}"
        
            st.write(integrated_response)
            
            
main()