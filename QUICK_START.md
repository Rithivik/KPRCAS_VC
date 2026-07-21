# ⚡ Quick Start - KPRCAS Virtual Chatbot

## 3-Minute Setup

### 1️⃣ Extract & Create `.env`
```bash
# Extract KPRCAS_VC_Updated.zip
cd "Coffee RAG"

# Create .env file
echo "GOOGLE_API_KEY=YOUR_API_KEY_HERE" > .env
```

### 2️⃣ Install Packages
```bash
pip install flask python-dotenv langchain-core langchain-chroma langchain-google-genai langchain-community langchain-text-splitters chromadb pypdf
```

### 3️⃣ Run Server
```bash
python app.py
```

### 4️⃣ Open Browser
Visit: **http://localhost:5000**

---

## Done! 🎉

Your KPRCAS chatbot is live. Try asking:
- "What programs does KPR College offer?"
- "How do I apply?"
- "Tell me about campus facilities"

---

## Troubleshooting Quick Links

| Problem | Solution |
|---------|----------|
| `Google API Key not found` | Check `.env` file in project root |
| `ModuleNotFoundError` | Run pip install command above |
| `Port 5000 in use` | Change port in app.py: `app.run(..., port=8000)` |
| `Empty database` | Make sure `chroma_db/` folder exists |
| No response from chatbot | Check internet connection for API |

---

## File Locations

```
Coffee RAG/
├── .env                    ← Create this with your API key
├── app.py                  ← Main Flask server
├── utils/rag_pipeline.py   ← RAG logic
├── templates/index.html    ← Chat UI
├── static/
│   ├── script.js          ← Frontend logic
│   └── style.css          ← Styling
└── chroma_db/             ← Database (already populated)
```

---

## API Test
```bash
curl -X POST http://localhost:5000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What programs does KPR College offer?"}'
```

---

Need more help? → Read **SETUP_GUIDE.md**
