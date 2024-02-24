import streamlit as st
import tempfile



st.title("Welcome to the admin page")
st.divider()

st.write("This page is for the admin to upload the PDF and CSV files")

uploaded_file = st.file_uploader('Upload your PDF Document', type='pdf')

def get_pdf_file():
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file.read())
        print(tfile.name)
        return tfile.name  # return file path


uploaded_file_csv = st.file_uploader('Upload your CSV File', type='csv')

def get_csv_file():  
    if uploaded_file_csv is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file_csv.read())
        return tfile.name 


