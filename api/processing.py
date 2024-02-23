import streamlit as st
from pathlib import Path
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
import pandas as pd
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent

OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

def limpiar_datos():
    datos = pd.read_csv("api/employee_data.csv")
    
    datos = datos.drop(["StartDate", "ExitDate", "BusinessUnit", "EmployeeStatus", "EmployeeType","PayZone","EmployeeClassificationType","TerminationType","TerminationDescription","DepartmentType","Division","DOB","State","GenderCode","LocationCode","RaceDesc","MaritalDesc","Performance Score","Current Employee Rating"], axis=1)


    print (datos.info())
    return datos

# faltan poner los datos ya procesados
def vectorizar_csv(datos):
    agent=create_csv_agent(llm=OpenAI(temperature=0),path=r"C:\Users\Poncho\Documents\FinanceAI\api\employee_data.csv",verbose=True,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    print(agent.run("Encuentra el appellido de alguien que se llama Amy"))


def vectorizar():
    datos = limpiar_datos()
    datos_procesados=vectorizar_csv(datos)
    pass


vectorizar()