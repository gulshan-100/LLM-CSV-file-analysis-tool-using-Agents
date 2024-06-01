import langchain 
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd                  

import os
os.environ['GOOGLE_API_KEY'] = "api_key"


def input_query(data, query):
    df = pd.read_csv(data)
    llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash')
    result = create_pandas_dataframe_agent(llm, df)
    return result.invoke(query)

    
    