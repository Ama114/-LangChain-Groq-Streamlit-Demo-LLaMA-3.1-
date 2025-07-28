# -LangChain-Groq-Streamlit-Demo-LLaMA-3.1-

This project is a simple demo that uses LangChain, Groq API, and Streamlit to build an interactive chatbot powered by LLaMA 3.1.

🔧 What the Code Does:
Environment Setup:

Loads your Groq API key securely from a .env file using python-dotenv.

User Interface:

Uses Streamlit to create a web UI where users can input a question.

Prompt Template:

Sets up a basic LangChain prompt:

System message: "You are a helpful assistant."

User message: Includes the actual question typed by the user.

Language Model (LLM):
Connects to Groq’s LLaMA 3.1 model using ChatGroq.

LangChain Chain:

Combines the prompt, the model, and an output parser to process the response.

When a user enters a question, the model generates and displays an answer.

