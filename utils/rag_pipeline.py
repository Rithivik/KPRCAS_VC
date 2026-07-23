import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

# -----------------------------------
# Load Environment Variables
# -----------------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise Exception("❌ GROQ_API_KEY not found in .env")

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "kprcas_vc_collection"

# -----------------------------------
# Module-level Caching (Coffee_RAG Style - Efficient!)
# -----------------------------------
_embeddings = None
_llm = None
_vectordb = None


def get_embeddings():
    """Use ChromaDB's default embeddings (built-in, no API key needed)"""
    global _embeddings

    if _embeddings is None:
        print("[Init] Loading ChromaDB Default Embeddings...")
        # ChromaDB uses sentence-transformers internally - it's already a dependency!
        _embeddings = None  # Use default
        print("[Init] ✅ Embeddings ready (using ChromaDB default)")

    return _embeddings


def get_llm():
    """Load Groq LLM"""
    global _llm

    if _llm is None:
        print("[Init] Loading Groq LLM...")

        _llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0.4
        )

        print("[Init] ✅ Groq Loaded")

    return _llm


def get_vectorstore():
    """Cache vectorstore globally - initialize once"""
    global _vectordb
    if _vectordb is None:
        print("[Init] Loading ChromaDB...")
        _vectordb = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=CHROMA_DIR
            # Removed embedding_function - uses ChromaDB default
        )
        print("[Init] ✅ ChromaDB loaded")
    return _vectordb

# -----------------------------------
# Document Loading & Ingestion
# -----------------------------------
def load_document(filepath):
    """Load PDF or TXT document"""
    if filepath.lower().endswith(".pdf"):
        loader = PyPDFLoader(filepath)
    else:
        loader = TextLoader(filepath, encoding="utf-8")
    return loader.load()


def split_documents(docs, chunk_size=400, chunk_overlap=60):
    """Split documents into chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)


def ingest_file(filepath):
    """Ingest a PDF or TXT file into the vector store"""
    print(f"[Ingest] Loading {filepath}...")
    docs = load_document(filepath)
    print(f"[Ingest] Splitting into chunks...")
    chunks = split_documents(docs)
    print(f"[Ingest] Adding {len(chunks)} chunks to vectorstore...")
    vectordb = get_vectorstore()
    vectordb.add_documents(chunks)
    print(f"[Ingest] ✅ Done!")
    return len(chunks)


# -----------------------------------
# KPRCAS Prompt
# -----------------------------------
KPRCAS_PROMPT = ChatPromptTemplate.from_template("""You are KPRCAS VC, the friendly virtual host of KPR College of Arts Science and Research.
Answer the student's question warmly and concisely using ONLY the context below.
If the answer isn't in the context, politely say you're not sure and suggest they contact the college.
Never make up information that isn't in the context.

Context:
{context}

Student question: {input}

KPRCAS answer:""")


# -----------------------------------
# Query & Answer Function (Optimized with Caching)
# -----------------------------------
def answer_query(question, k=4):
    """Answer a question using RAG with caching for efficiency"""
    try:
        # Get cached instances
        vectordb = get_vectorstore()
        retriever = vectordb.as_retriever(search_kwargs={"k": k})
        
        # Define format function
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        # Build chain
        qa_chain = RunnableParallel(
            answer=(
                {"context": retriever | format_docs, "input": RunnablePassthrough()}
                | KPRCAS_PROMPT
                | get_llm()
                | StrOutputParser()
            ),
            context=retriever
        )
        
        # Get answer with timeout
        result = qa_chain.invoke(question)
        
        # Extract sources
        sources = []
        for doc in result.get("context", []):
            sources.append({
                "source": doc.metadata.get("source", "unknown"),
                "page": doc.metadata.get("page", None)
            })
        
        return {
            "answer": result["answer"],
            "sources": sources
        }
    except Exception as e:
        print(f"[Error] Query failed: {e}")
        return {
            "answer": "Sorry, I encountered an error processing your question. Please try again.",
            "sources": []
        }