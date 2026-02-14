 

import os
from dotenv import load_dotenv
import streamlit as st

# Import from our files
from config import APP_TITLE, APP_SUBTITLE, WELCOME_MESSAGE
from styles import get_custom_css
from utils import get_api_key
from sidebar import render_sidebar
from chat import display_chat_history, handle_chat_input

# Load environment variables
load_dotenv()
api_key = get_api_key()

# Page config
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Header
st.markdown(f'<h1 class="main-title">{APP_TITLE}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="subtitle">{APP_SUBTITLE}</p>', unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render sidebar and get settings
model_option, temperature = render_sidebar()

# Welcome message
if not st.session_state.messages:
    st.info(WELCOME_MESSAGE)

# Display chat history
display_chat_history()

# Handle chat input
handle_chat_input(model_option, temperature, api_key)

# Footer
st.divider()
st.markdown(
    "<p style='text-align: center; color: #666; font-size: 0.9rem;'>"
    "Made with AVD </p>",
    unsafe_allow_html=True
)
