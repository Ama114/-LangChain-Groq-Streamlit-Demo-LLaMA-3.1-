# sidebar.py
 

import streamlit as st
from datetime import datetime
from config import MODELS, DEFAULT_TEMPERATURE, MIN_TEMPERATURE, MAX_TEMPERATURE
from utils import get_chat_stats, export_chat_to_text

def render_sidebar():
    """
    render side bar
    
    Returns:
        model_option: Selected model
        temperature: Selected temperature
    """
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Model selection dropdown
        model_option = st.selectbox(
            "Select Model",
            options=list(MODELS.keys()),
            format_func=lambda x: MODELS[x],  # show the display names
            index=0
        )
        
        st.divider()
        
        # Temperature slider
        temperature = st.slider(
            "Temperature 🌡️",
            min_value=MIN_TEMPERATURE,
            max_value=MAX_TEMPERATURE,
            value=DEFAULT_TEMPERATURE,
            step=0.1,
            help="Higher values make output more creative"
        )
        
        st.divider()
        
        # Chat statistics
        if st.session_state.messages:
            st.subheader("📊 Chat Stats")
            stats = get_chat_stats(st.session_state.messages)
            st.metric("Total Messages", stats["total"])
            st.metric("Your Messages", stats["user"])
            st.metric("AI Responses", stats["assistant"])
        
        st.divider()
        
        # Export chat button
        if st.session_state.messages:
            if st.button("📥 Export Chat", use_container_width=True):
                chat_text = export_chat_to_text(st.session_state.messages)
                filename = f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                
                st.download_button(
                    label="💾 Download Chat",
                    data=chat_text,
                    file_name=filename,
                    mime="text/plain",
                    use_container_width=True
                )
        
        st.divider()
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.divider()
        
        # Info section
        with st.expander("ℹ️ About"):
            st.write("""
            This is an AI-powered chatbot using:
            - **LangChain** for AI orchestration
            - **Groq** for ultra-fast inference
            - **LLaMA 3.1** language model
            
            Ask me anything! 💬
            """)
    
    return model_option, temperature