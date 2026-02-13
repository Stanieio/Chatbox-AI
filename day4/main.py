import os
from fastapi import FastAPI
#from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
#import unicorn
app=FastAPI()
llm=ChatGroq(model="llama-3.1-8b-instant",groq_api_key="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")
add_routes(app,llm,path="/chat")