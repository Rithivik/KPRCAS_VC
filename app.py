import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()

from utils.rag_pipeline import ingest_file, answer_query, get_vectorstore

app = Flask(__name__)

UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {".pdf", ".txt"}

# Filename(s) to auto-ingest on startup if the collection is empty.
AUTO_INGEST_FILES = ["KPRCAS.pdf"]

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs("chroma_db", exist_ok=True)


def allowed_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS


def auto_ingest_startup():
    """
    Runs once at server startup. If the vector store is empty,
    automatically ingest any files listed in AUTO_INGEST_FILES.
    Safe to call on every restart -- it only ingests when the
    collection is empty, so it won't create duplicate chunks.
    """
    try:
        vectordb = get_vectorstore()
        count = vectordb._collection.count()
    except Exception as e:
        print(f"[auto_ingest] Could not check vector store: {e}")
        return

    if count > 0:
        print(f"[auto_ingest] Vector store already has {count} chunks. Skipping auto-ingest.")
        return

    for fname in AUTO_INGEST_FILES:
        candidate_paths = [fname, os.path.join(UPLOAD_DIR, fname)]
        filepath = next((p for p in candidate_paths if os.path.exists(p)), None)

        if not filepath:
            print(f"[auto_ingest] '{fname}' not found in project root or uploads/. Skipping.")
            continue

        try:
            num_chunks = ingest_file(filepath)
            print(f"[auto_ingest] Ingested '{filepath}': {num_chunks} chunks added.")
        except Exception as e:
            print(f"[auto_ingest] Failed to ingest '{filepath}': {e}")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health():
    try:
        vectordb = get_vectorstore()
        count = vectordb._collection.count()
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 500
    return jsonify({"status": "ok", "chunks_in_store": count})


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Only .pdf and .txt files are supported"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_DIR, filename)
    file.save(filepath)

    try:
        num_chunks = ingest_file(filepath)
    except Exception as e:
        return jsonify({"error": f"Ingestion failed: {str(e)}"}), 500

    return jsonify({
        "message": "File ingested successfully",
        "filename": filename,
        "chunks_added": num_chunks
    })


@app.route("/query", methods=["POST"])
def query():
    data = request.get_json(silent=True)

    if not data or "question" not in data:
        return jsonify({"error": "Request body must include 'question'"}), 400

    question = data["question"]
    k = data.get("k", 4)

    try:
        result = answer_query(question, k=k)
    except Exception as e:
        return jsonify({"error": f"Query failed: {str(e)}"}), 500

    return jsonify(result)


# Run auto-ingest once when the module loads
auto_ingest_startup()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
