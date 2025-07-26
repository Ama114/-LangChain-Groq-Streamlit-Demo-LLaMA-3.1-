import os
from dotenv import load_dotenv

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Set Groq API Key from .env file
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Streamlit UI
st.title("LangChain Demo with Groq - LLaMA3.1")
input_text = st.text_input("What question do you have in mind?")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

# Groq LLM (LLaMA 3.1)
llm = ChatGroq(
    model="llama3-8b-8192",  # You can also try "mixtral-8x7b-32768" or "gemma-7b-it"
    api_key=os.environ["GROQ_API_KEY"]
)

# Chain setup
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Run when user submits input
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
