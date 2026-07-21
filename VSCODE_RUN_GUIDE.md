# 🚀 Run KPRCAS Chatbot in VS Code - Complete Guide

## Step-by-Step Instructions

---

## 📥 **Step 1: Extract the Downloaded Zip File**

### Windows:
1. Download `KPRCAS_VC_Final.zip`
2. Right-click on the zip file
3. Select **"Extract All..."** (or use 7-Zip/WinRAR)
4. Choose where to extract (e.g., Desktop, Documents, Downloads)
5. A folder named `Coffee RAG` will be created

**Example Path After Extraction:**
```
C:\Users\YourName\Downloads\Coffee RAG\
C:\Users\YourName\Desktop\Coffee RAG\
```

### Mac/Linux:
1. Double-click the zip file (auto-extracts)
2. Or use terminal:
```bash
unzip KPRCAS_VC_Final.zip
```

---

## 📂 **Step 2: Folder Structure (Verify)**

After extraction, your folder should look like this:

```
Coffee RAG/
├── app.py                    ← Main file to run
├── KPRCAS.pdf               ← College document
├── chroma_db/               ← Vector database (ready to use)
│   └── chroma.sqlite3
├── uploads/                 ← For new uploads
├── utils/
│   └── rag_pipeline.py      ← RAG logic
├── templates/
│   └── index.html           ← Chat UI
├── static/
│   ├── kprcas_logo.png      ← Logo (watermark)
│   ├── style.css            ← Styling
│   └── script.js            ← Frontend logic
└── venv/                    ← Virtual environment (already exists)
```

---

## 🎯 **Step 3: Open Project in VS Code**

### Option A: Drag & Drop
1. Open VS Code
2. Drag the `Coffee RAG` folder into VS Code window
3. It will open automatically

### Option B: File Menu
1. Open VS Code
2. Click **File** → **Open Folder**
3. Navigate to `Coffee RAG` folder
4. Click **Select Folder**

### Option C: Terminal (Advanced)
```bash
# Navigate to your extraction location
cd C:\Users\YourName\Downloads\Coffee RAG

# Open in VS Code
code .
```

**You should see the folder structure on the left side of VS Code** ✅

---

## 🔐 **Step 4: Create `.env` File**

### Method 1: Using VS Code UI (Recommended)
1. In VS Code, look at the left panel (File Explorer)
2. Right-click in the empty space below `venv/`
3. Select **"New File"**
4. Name it: `.env` (exactly this, with the dot)
5. Press **Enter**

### Method 2: Manual
1. In left panel, click the **"New File"** icon (looks like a page with a plus)
2. Type `.env`
3. Click anywhere outside to create

### After Creating `.env`:
1. Click on `.env` file to open it
2. Copy and paste this:

```
GOOGLE_API_KEY=YOUR_API_KEY
```

3. Replace `AQ.Ab8RN6...` with **your actual API key**
4. Press **Ctrl+S** (or Cmd+S on Mac) to save

**Important:** Your `.env` file should be in the root folder of `Coffee RAG`, not in a subfolder.

---

## 📦 **Step 5: Open Terminal in VS Code**

### Method 1 (Easiest):
1. Press **Ctrl + `** (backtick key, below Esc)
2. A terminal appears at the bottom of VS Code

### Method 2:
1. Click **Terminal** menu at top
2. Click **New Terminal**

**You should now see a terminal at the bottom of VS Code with path like:**
```
C:\Users\YourName\Downloads\Coffee RAG>
```

---

## 🐍 **Step 6: Activate Virtual Environment (Optional but Recommended)**

### Windows:
```bash
venv\Scripts\activate
```

You should see `(venv)` at the start of your terminal line.

### Mac/Linux:
```bash
source venv/bin/activate
```

---

## 📥 **Step 7: Install Required Packages**

### Copy and paste this entire command in terminal:

```bash
pip install flask python-dotenv langchain-core langchain-chroma langchain-google-genai langchain-community langchain-text-splitters chromadb pypdf
```

**Press Enter and wait** (takes 2-5 minutes)

You'll see text like:
```
Collecting flask...
Downloading flask-...
Installing collected packages...
Successfully installed...
```

When it's done, you should see:
```
Successfully installed flask python-dotenv langchain-core ...
```

✅ **If you see this, packages are installed correctly!**

---

## ▶️ **Step 8: Run the Chatbot**

In the same terminal, type:

```bash
python app.py
```

Press **Enter**

You should see:

```
📦 Loading ChromaDB...
✅ ChromaDB loaded.
[auto_ingest] Vector store already has 847 chunks. Skipping auto-ingest.
 * Running on http://localhost:5000
 * Press CTRL+C to quit
```

**This means your server is running!** ✅

---

## 🌐 **Step 9: Open in Browser**

1. Open any web browser (Chrome, Firefox, Safari, Edge)
2. Go to: **http://localhost:5000**
3. Your beautiful KPRCAS chatbot appears! 🎓

---

## 💬 **Step 10: Test the Chatbot**

Try asking questions like:
- "What programs does KPRCAS offer?"
- "Tell me about admissions"
- "What are campus facilities?"

The chatbot will answer based on the KPRCAS.pdf document! 🤖

---

## 📋 **Full Terminal Commands Reference**

```bash
# 1. Activate virtual environment (Windows)
venv\Scripts\activate

# 1. Activate virtual environment (Mac/Linux)
source venv/bin/activate

# 2. Install packages
pip install flask python-dotenv langchain-core langchain-chroma langchain-google-genai langchain-community langchain-text-splitters chromadb pypdf

# 3. Run the chatbot
python app.py

# 4. Stop the server (when done)
# Press Ctrl+C in terminal
```

---

## 🎨 **What You'll See**

### In VS Code Terminal:
```
📦 Loading ChromaDB...
✅ ChromaDB loaded.
[auto_ingest] Vector store already has 847 chunks. Skipping auto-ingest.
 * Running on http://localhost:5000
 * Press CTRL+C to quit
```

### In Browser (http://localhost:5000):
```
╔════════════════════════════════════╗
║ 🎓 KPRCAS VC          💚 Online   ║
║ KPR College Virtual Assistant     ║
╠════════════════════════════════════╣
║              [Logo Watermark]      ║
║                                    ║
║ 🎓 Hi! I'm KPRCAS VC...           ║
║ Just now                           ║
║                                    ║
║ [Programs] [Admissions] [Campus]   ║
╠════════════════════════════════════╣
║ Type a message...              [➜] ║
╚════════════════════════════════════╝
```

---

## ✅ **Quick Checklist**

- [ ] Downloaded `KPRCAS_VC_Final.zip`
- [ ] Extracted to `Coffee RAG` folder
- [ ] Opened folder in VS Code
- [ ] Created `.env` file with API key
- [ ] Opened terminal in VS Code
- [ ] Installed packages (pip install...)
- [ ] Ran `python app.py`
- [ ] Opened `http://localhost:5000` in browser
- [ ] Tested by typing a message

---

## 🐛 **Troubleshooting**

### ❌ Terminal says "python not found"
**Solution:**
- Make sure Python is installed: `python --version`
- If not installed, download from python.org
- Restart VS Code after installing Python

### ❌ `ModuleNotFoundError: No module named...`
**Solution:**
- Make sure all packages installed: Run pip install command again
- Make sure you're in the `Coffee RAG` folder in terminal

### ❌ Port 5000 already in use
**Solution:**
- Change port in `app.py`:
  ```python
  app.run(debug=True, port=8000)  # Change to 8000
  ```
- Then visit `http://localhost:8000`

### ❌ `.env` file not recognized
**Solution:**
- Make sure file is named exactly `.env` (with the dot)
- Make sure it's in the root `Coffee RAG` folder (not in a subfolder)
- Make sure your API key is correct (no extra spaces)

### ❌ Chatbot says "Google API Key not found"
**Solution:**
- Check your `.env` file
- Format should be: `GOOGLE_API_KEY=your_key_here`
- No quotes, no spaces around `=`
- Save file (Ctrl+S)
- Restart server (Ctrl+C, then `python app.py`)

### ❌ Logo or colors not showing
**Solution:**
- Clear browser cache (Ctrl+Shift+Delete)
- Refresh page (Ctrl+R or F5)
- Make sure `static/kprcas_logo.png` exists

### ❌ Database error / no responses
**Solution:**
- Make sure `chroma_db/` folder exists
- Make sure `KPRCAS.pdf` is in root folder
- Delete `chroma_db/` folder and restart server
- Server will recreate it with fresh data

---

## 🎯 **Complete Example Walkthrough**

**Say you extracted to Desktop:**

```
Desktop/Coffee RAG/
```

**In VS Code:**
1. Drag `Coffee RAG` folder into VS Code
2. Open terminal: Ctrl + `
3. Create `.env` file with your API key
4. In terminal type:
   ```bash
   pip install flask python-dotenv langchain-core langchain-chroma langchain-google-genai langchain-community langchain-text-splitters chromadb pypdf
   ```
5. Press Enter, wait for installation
6. Type:
   ```bash
   python app.py
   ```
7. Open browser: `http://localhost:5000`
8. Chat with your KPRCAS bot! 🎓

---

## 🛑 **When Done - How to Stop**

1. In VS Code terminal, press **Ctrl+C**
2. Terminal will show: `KeyboardInterrupt`
3. Server stops ✅

To run again:
```bash
python app.py
```

---

## 📱 **View on Phone/Other Devices (Same Network)**

If your computer IP is `192.168.x.x`:

Instead of `http://localhost:5000`, visit:
```
http://192.168.x.x:5000
```

Find your IP:
- **Windows**: `ipconfig` in terminal, look for "IPv4 Address"
- **Mac**: System Preferences → Network
- **Linux**: `ifconfig` in terminal

---

## 🎓 **Next Steps**

1. ✅ Run the chatbot
2. ✅ Test it with questions
3. ✅ Show it to your friends
4. ✅ Add more college documents (if desired)
5. ✅ Deploy to web (Heroku, AWS, etc. - optional)

---

## 💡 **Pro Tips**

### Tip 1: Keep Terminal Visible
Keep VS Code terminal open while working so you can see any errors.

### Tip 2: Edit CSS Colors
Want to change colors? Edit `static/style.css` and refresh browser.

### Tip 3: View Real-Time Logs
Terminal shows every question asked - good for debugging.

### Tip 4: Add Your Docs
Place PDF files in the `uploads/` folder and upload via API.

---

## 📚 **File You'll Use Most**

- **`app.py`** - Main server (the file you run)
- **`.env`** - Your API key (keep secret!)
- **`templates/index.html`** - Chat UI
- **`static/style.css`** - Colors and design
- **`static/script.js`** - Chat logic

---

## 🎉 **You're Ready!**

Follow these steps and your KPRCAS Virtual Chatbot will be running in VS Code! 

If you get stuck on any step, check the **Troubleshooting** section above.

**Good luck!** 🚀✨
