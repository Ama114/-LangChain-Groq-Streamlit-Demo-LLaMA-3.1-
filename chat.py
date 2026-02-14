 

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from config import SYSTEM_PROMPT, USER_AVATAR, ASSISTANT_AVATAR
from utils import format_chat_history

def display_chat_history():
    """ display the old chats    """

    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else ASSISTANT_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])


def get_ai_response(prompt_input, model_option, temperature, api_key):
    """
    generate the AI response
    
    Args:
        prompt_input: User ගේ message
        model_option: Selected AI model
        temperature: Creativity level
        api_key: Groq API key
        
    Returns:
        AI response text
    """
    # Initialize LLM
    llm = ChatGroq(
        model=model_option,
        groq_api_key=api_key,
        temperature=temperature
    )
    
    # Format chat history
    chat_history = format_chat_history(st.session_state.messages[:-1])
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("placeholder", "{chat_history}"), 
        ("user", "{question}")
    ])
    
    # Create chain
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # Get response
    response = chain.invoke({
        "question": prompt_input,
        "chat_history": chat_history
    })
    
    return response


def handle_chat_input(model_option, temperature, api_key):
    """
    User input handle and   generate AI response 
    
    Args:
        model_option: Selected model
        temperature: Temperature value
        api_key: API key
    """
    if prompt_input := st.chat_input("Type your message here..."):
        
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt_input})
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(prompt_input)

        # Get AI response
        try:
            with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
                with st.spinner("Thinking..."):
                    response = get_ai_response(
                        prompt_input, 
                        model_option, 
                        temperature, 
                        api_key
                    )
                    st.markdown(response)
                    
            # Save response
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response
            })

        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.info("💡 Tip: Check if your API key is valid and you have internet connection.")