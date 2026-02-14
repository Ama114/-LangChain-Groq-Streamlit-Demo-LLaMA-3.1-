 

PRIMARY_COLOR = "#1E88E5"
SECONDARY_COLOR = "#1565C0"

def get_custom_css():
      

    return f"""
    <style>
    /* Title's style */
    .main-title {{
        text-align: center;
        color: {PRIMARY_COLOR};
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }}
    
    /* Subtitle's style */
    .subtitle {{
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }}
    
    /* Chat messages style */
    .stChatMessage {{
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }}
    
    /* Button style */
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        border: none;
        font-weight: bold;
    }}
    
    .stButton>button:hover {{
        background-color: {SECONDARY_COLOR};
    }}
    </style>
    """