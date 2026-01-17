import os
#from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]


# Streamlit Page Config
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("LangChain Chat - LLaMA 3.1")

# 2. Session State එක initialize කිරීම (Chat history එක මතක තබා ගැනීමට)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. කලින් කරපු Chat history එක screen එකේ පෙන්වීම
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Input එක (ChatGPT වගේ පහළින් එන එක)
if prompt_input := st.chat_input("What is on your mind?"):
    
    # User ගේ message එක screen එකේ පෙන්වීම සහ save කිරීම
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.markdown(prompt_input)

    # 5. LLM Setup සහ Response එක ලබා ගැනීම
    try:
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            groq_api_key=api_key
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Please respond as an expert."),
            # මෙතනදී මුළු chat history එකම යැවීම වැදගත් (Context එක තබා ගැනීමට)
            ("placeholder", "{chat_history}"), 
            ("user", "{question}")
        ])
        
       # Mehema liyanna:
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        with st.chat_message("assistant"):
            # Response එක stream වෙනවා වගේ පෙන්වන්න පුළුවන්
            response = chain.invoke({
                "question": prompt_input,
                "chat_history": st.session_state.messages # දැනට තියෙන history එක
            })
            st.markdown(response)
            
        # Assistant ගේ response එක save කිරීම
        st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"Error: {e}")