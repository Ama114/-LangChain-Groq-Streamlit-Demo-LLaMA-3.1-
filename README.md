# 🤖 AI Chat Assistant

A real-time AI chatbot built with LangChain and Groq API.

---

## 🛠️ Technologies Used

- **Streamlit** - Web interface
- **LangChain** - AI framework
- **Groq API** - Fast AI inference
- **LLaMA 3.1** - AI model
- **Python 3.8+**

---

## 📂 Project Structure
```
ai-chat-assistant/
├── app.py          # Main file - runs the application
├── config.py       # Settings - models, colors, messages
├── utils.py        # Helper functions - API key, export, stats
├── sidebar.py      # Sidebar - settings panel UI
├── chat.py         # Chat logic - AI responses
├── styles.py       # CSS - UI styling
├── .env            # API key 
└── requirements.txt
```

### What Each File Does

| File | Purpose |
|------|---------|
| `app.py` | Main controller - brings everything together |
| `config.py` | Settings - models list, colors, messages  |
| `utils.py` | Helper functions - API validation, export, stats  |
| `sidebar.py` | Sidebar UI - model selection, temperature  |
| `chat.py` | Chat logic - generates AI responses  |
| `styles.py` | CSS styling - colors, buttons  |

---

## 🚀 Setup & Run

### 1️⃣ Installation
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt
 
# use `.env` file for protect the api key

 
 
---

## 📦 requirements.txt
```
streamlit
langchain
langchain-core
langchain-groq
python-dotenv
```

---
