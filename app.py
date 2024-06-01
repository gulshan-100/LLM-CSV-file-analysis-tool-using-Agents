import streamlit as st  
from query import input_query 
from dotenv import load_dotenv

load_dotenv()

#Application code 
st.header("CSV File analysis tool")

data = st.file_uploader("Upload the csv file", type='csv')

query = st.text_area("Enter your query")
button = st.button("Generate output")

if button:
    result = input_query(data, query)
    st.write(result)


