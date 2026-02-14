 

import os
from datetime import datetime
import streamlit as st

def get_api_key():
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("❌ GROQ_API_KEY not found in .env file!")
        st.info("💡 Please add your API key to the .env file")
        st.stop()
    return api_key


def export_chat_to_text(messages):
    """
    convert Chat history to  text file 
    
    Args:
        messages: Chat messages list
        
    Returns:
        Text format එකේ chat history
    """
    export_text = f"Chat Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    export_text += "=" * 60 + "\n\n"
    
    for msg in messages:
        role = msg["role"].upper()  # USER or ASSISTANT
        content = msg["content"]
        export_text += f"{role}:\n{content}\n\n"
        export_text += "-" * 60 + "\n\n"
    
    return export_text


def get_chat_stats(messages):
    """
   calculate Chat statistics  
    
    Args:
        messages: Chat messages list
        
    Returns:
        Dictionary with total, user, assistant counts
    """
    user_count = len([m for m in messages if m["role"] == "user"])
    assistant_count = len(messages) - user_count
    
    return {
        "total": len(messages),
        "user": user_count,
        "assistant": assistant_count
    }


def format_chat_history(messages):
    """
    Chat history එක LangChain format එකට convert කරනවා
    
    Args:
        messages: Chat messages list
        
    Returns:
        List of tuples (role, content)
    """
    return [(msg["role"], msg["content"]) for msg in messages]