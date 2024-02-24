from langchain_openai import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import FAISS
from langchain_community.vectorstores.faiss import FAISS
from langchain.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.agents.agent_types import AgentType
from api.auth_openai import getOpenAIkey

#Hugging Face Prompt Injection

'''from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline

# Using https://huggingface.co/laiyer/deberta-v3-base-prompt-injection
model_path = "laiyer/deberta-v3-base-prompt-injection"
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.model_input_names = ["input_ids", "attention_mask"]  # Hack to run the model
model = ORTModelForSequenceClassification.from_pretrained(model_path, subfolder="onnx")

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    truncation=True,
    max_length=512,
)

from langchain_experimental.prompt_injection_identifier import (
    HuggingFaceInjectionIdentifier,
)

injection_identifier = HuggingFaceInjectionIdentifier(
    model=classifier,
)'''

ApiKey = getOpenAIkey()

def create_agent(file_path):
    # Create the agent using create_csv_agent() or a similar function
    agent = create_csv_agent(
        #tools=[injection_identifier],
        llm=OpenAI(temperature=0),
        path=file_path,
        verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
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
