# ⚡ KPRCAS Chatbot - VS Code Quick Start (5 Minutes)

## 🎯 The Quick Version

### 1️⃣ Extract ZIP
- Right-click `KPRCAS_VC_Final.zip`
- Click "Extract All"
- You get `Coffee RAG` folder

### 2️⃣ Open in VS Code
- Drag `Coffee RAG` folder into VS Code
- Or: File → Open Folder → Select `Coffee RAG`

### 3️⃣ Create `.env` File
- Right-click in left panel → New File
- Name: `.env`
- Paste this:
```
GOOGLE_API_KEY=YOUR_API_KEY
```
- Replace the key with YOUR key
- Ctrl+S to save

### 4️⃣ Open Terminal
- Press `Ctrl + `` (backtick below Esc)
- Terminal appears at bottom

### 5️⃣ Install Packages
- Copy-paste this into terminal:
```bash
pip install flask python-dotenv langchain-core langchain-chroma langchain-google-genai langchain-community langchain-text-splitters chromadb pypdf
```
- Press Enter
- Wait for ✅ completion

### 6️⃣ Run Server
- Type in terminal:
```bash
python app.py
```
- Press Enter
- Wait for: `Running on http://localhost:5000`

### 7️⃣ Open Browser
- Go to: **http://localhost:5000**
- 🎉 Your chatbot is live!

---

## 🖥️ Visual Layout in VS Code

```
┌─────────────────────────────────────────────────────────┐
│ FILE  EDIT  VIEW  TERMINAL                              │
├──────────────────┬──────────────────────────────────────┤
│ Coffee RAG (📁)  │                                      │
│ ├─ app.py (🐍)   │      EDITOR                         │
│ ├─ .env (🔑)     │   (open app.py or .env)           │
│ ├─ KPRCAS.pdf    │                                      │
│ ├─ chroma_db     │                                      │
│ ├─ templates     │                                      │
│ ├─ static        │                                      │
│ ├─ utils         │                                      │
│ └─ venv          │                                      │
├──────────────────┴──────────────────────────────────────┤
│ Terminal:                                               │
│ C:\...\Coffee RAG> python app.py                       │
│  * Running on http://localhost:5000                    │
│  * Press CTRL+C to quit                               │
└─────────────────────────────────────────────────────────┘
```

---

## 📝 Terminal Commands (Copy-Paste)

### Install packages:
```bash
pip install flask python-dotenv langchain-core langchain-chroma langchain-google-genai langchain-community langchain-text-splitters chromadb pypdf
```

### Run server:
```bash
python app.py
```

### Stop server:
```
Ctrl+C
```

---

## ✅ Signs It's Working

### Terminal should show:
```
📦 Loading ChromaDB...
✅ ChromaDB loaded.
[auto_ingest] Vector store already has 847 chunks. Skipping auto-ingest.
 * Running on http://localhost:5000
 * Press CTRL+C to quit
```

### Browser should show:
```
🎓 KPRCAS VC (online)
KPR College Virtual Assistant

[Chat window with watermark logo]

[Programs] [Admissions] [Campus]

Type a message... [➜]
```

---

## 🐛 Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| "python not found" | Install Python from python.org, restart VS Code |
| "No module named flask" | Run pip install command again |
| Port 5000 in use | Change port in app.py: `port=8000` |
| "Google API Key not found" | Check .env file, Ctrl+S save, restart server |
| Blank screen in browser | Ctrl+Shift+Delete clear cache, refresh |
| "KPRCAS.pdf not found" | Make sure PDF is in root folder |

---

## 📂 Folder Locations

```
Downloads/
└── Coffee RAG/          ← Open THIS in VS Code
    ├── app.py           ← Run this: python app.py
    ├── .env             ← Create this with API key
    ├── KPRCAS.pdf       ← Document (already here)
    ├── chroma_db/       ← Database (already here)
    ├── static/
    │   └── kprcas_logo.png
    ├── templates/
    │   └── index.html
    └── utils/
        └── rag_pipeline.py
```

---

## 🔗 Access Your Chatbot

**Locally:**
- http://localhost:5000

**From another device (same WiFi):**
- http://192.168.x.x:5000
- (Replace x.x with your computer's IP from `ipconfig`)

---

## 🚀 Full Step-by-Step Summary

```
1. Extract ZIP                    → Coffee RAG folder ✅
2. Drag to VS Code               → Folder opens ✅
3. Create .env                   → Add API key ✅
4. Open Terminal (Ctrl+`)        → Terminal ready ✅
5. pip install (packages)        → Packages installed ✅
6. python app.py                 → Server running ✅
7. Open localhost:5000           → Chatbot loaded ✅
8. Type message                  → Bot responds ✅
```

---

## 📞 When You Need Help

**Stuck on Step 3 (creating .env)?**
- Read: VSCODE_RUN_GUIDE.md → Step 4

**Issues with packages?**
- Read: VSCODE_RUN_GUIDE.md → Step 7

**Chatbot not responding?**
- Read: VSCODE_RUN_GUIDE.md → Troubleshooting

**Colors or design different?**
- Read: COLOR_SCHEME_GUIDE.md

---

## ⏱️ Time Breakdown

```
Extract ZIP           →  1 min  ⏱️
Open VS Code          →  1 min  ⏱️
Create .env           →  1 min  ⏱️
Install packages      →  3-5 min ⏱️
Run server            →  30 sec ⏱️
─────────────────────────────────
Total:                → ~7 minutes
```

---

## 🎉 You're All Set!

Your KPRCAS Virtual Chatbot is ready to run!

**Download, Extract, Create .env, pip install, python app.py, Open Browser**

That's it! 🚀

---

**Need detailed help?** → Check **VSCODE_RUN_GUIDE.md** for complete instructions!
