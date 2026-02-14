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
├── .env            # API key (⚠️ DO NOT commit to Git!)
└── requirements.txt
```

### What Each File Does

| File | Purpose |
|------|---------|
| `app.py` | Main controller - brings everything together (Boss 👑) |
| `config.py` | Settings - models list, colors, messages (Settings Book 📖) |
| `utils.py` | Helper functions - API validation, export, stats (Tool Box 🧰) |
| `sidebar.py` | Sidebar UI - model selection, temperature (Control Panel ⚙️) |
| `chat.py` | Chat logic - generates AI responses (Brain 🧠) |
| `styles.py` | CSS styling - colors, buttons (Paint 🎨) |

---

## 🚀 Setup & Run

### 1️⃣ Installation
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ API Key Setup (Secure)

**Step 1:** Get a Groq API key (Free!)
- Go to https://console.groq.com
- Create an account
- Generate an API key

**Step 2:** Create `.env` file
```bash
# Create .env file in project folder
New-Item -ItemType File -Path .env    # Windows
touch .env                            # Mac/Linux
```

**Step 3:** Add your API key

Open `.env` file and add:
```env
GROQ_API_KEY=your_actual_api_key_here
```

⚠️ **Security:**
- **NEVER commit `.env` to Git**
- Check that `.env` is in `.gitignore`
- Don't share your API key with anyone

### 3️⃣ Run the App
```bash
streamlit run app.py
```

✅ Opens in browser at `http://localhost:8501`!

---

## 💡 How to Use

1. **Select Model** - Choose an AI model from the sidebar
2. **Set Temperature** - 0.0 (accurate) to 1.0 (creative)
3. **Chat** - Type your message and press send
4. **Export** - Download chat history with "Export Chat" button
5. **Clear** - Reset conversation with "Clear Chat History" button

---

## ⚙️ Customization

### Change Colors
`styles.py`:
```python
PRIMARY_COLOR = "#1E88E5"      # Your color
SECONDARY_COLOR = "#1565C0"
```

### Add Models
`config.py`:
```python
MODELS = {
    "llama-3.1-8b-instant": "LLaMA 3.1 8B ⚡",
    "your-model": "Your Model Name 🚀"
}
```

### Change Messages
`config.py`:
```python
APP_TITLE = "🤖 Your Title"
WELCOME_MESSAGE = "Your welcome message"
```

---

## 🐛 Common Errors & Solutions

**❌ Module not found**
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

**❌ API key not found**
- Is `.env` file in project root?
- Correct format? → `GROQ_API_KEY=your_key`
- No spaces? → Remove spaces!

**❌ Port already in use**
```bash
streamlit run app.py --server.port 8502
```

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

**Made with ❤️**
