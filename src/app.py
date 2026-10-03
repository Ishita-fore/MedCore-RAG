import chromadb
import streamlit as st

from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MedCore | Knowledge Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROFESSIONAL THEME
# ============================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background-color: #f4f8fb;
    }

    /* Main content width */
    .main .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #dce6ed;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #123b56;
    }

    /* Normal headings */
    h1, h2, h3 {
        color: #163e57;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        border: 1px solid #d4e3eb;
        background-color: white;
        color: #175b78;
        font-weight: 600;
        min-height: 42px;
    }

    .stButton > button:hover {
        border-color: #087da1;
        color: #087da1;
        background-color: #f4fbfd;
    }

    /* Primary button */
    .stButton > button[kind="primary"] {
        background-color: #087da1;
        color: white;
        border: none;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #dce7ee;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 3px 12px rgba(20, 60, 80, 0.04);
    }

    /* Expanders */
    div[data-testid="stExpander"] {
        background-color: white;
        border: 1px solid #dce7ee;
        border-radius: 12px;
    }

    /* Text area */
    textarea {
        border-radius: 12px !important;
        border: 1px solid #cfdfe8 !important;
    }

    /* Chat input */
    div[data-testid="stChatInput"] {
        border-color: #cfdfe8;
    }

    /* Horizontal divider */
    hr {
        border-color: #dce7ee;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RAG ENGINE
# ============================================================

@st.cache_resource
def load_rag():

    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )

    Settings.llm = Ollama(
        model="gpt-oss:20b-cloud",
        request_timeout=120.0,
    )

    chroma_client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = chroma_client.get_collection(
        name="medcore_rag"
    )

    vector_store = ChromaVectorStore(
        chroma_collection=collection
    )

    index = VectorStoreIndex.from_vector_store(
        vector_store
    )

    return index.as_query_engine(
        similarity_top_k=5
    )


# ============================================================
# LOAD RAG
# ============================================================

try:
    query_engine = load_rag()
    rag_ready = True
    rag_error = None

except Exception as error:
    query_engine = None
    rag_ready = False
    rag_error = str(error)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🏥 MedCore")

    st.caption(
        "Healthcare Knowledge Assistant"
    )

    st.divider()

    st.subheader("🏢 Departments")

    departments = [
        "🩺 Clinical Operations",
        "👥 Patient Services",
        "₹ Finance & Billing",
        "👔 HR & Administration",
        "⚖️ Legal & Compliance",
        "📦 Procurement",
        "🔐 IT & Security",
    ]

    for department in departments:
        st.write(department)

    st.divider()

    st.subheader("⚙️ RAG Architecture")

    st.write("📄 **Parser:** Docling")
    st.write("🧠 **Framework:** LlamaIndex")
    st.write("🗄️ **Vector Store:** Chroma")
    st.write("🔎 **Embeddings:** BGE-small")
    st.write("🤖 **LLM:** Ollama Cloud")

    st.divider()

    if rag_ready:
        st.success("RAG Engine Connected")
    else:
        st.error("RAG Engine Unavailable")

    st.caption(
        "Academic Project • Synthetic Data"
    )


# ============================================================
# TOP HEADER
# ============================================================

header_left, header_right = st.columns(
    [5, 1]
)

with header_left:

    st.title("🏥 MedCore Knowledge Assistant")

    st.caption(
        "Internal healthcare knowledge platform for "
        "clinical, administrative, financial, legal, "
        "procurement and IT documentation."
    )

with header_right:

    if rag_ready:
        st.success("● Online")
    else:
        st.error("● Offline")


st.divider()


# ============================================================
# WELCOME SECTION
# ============================================================

st.subheader("Welcome to MedCore")

st.info(
    "Ask questions about hospital policies, SOPs, "
    "guidelines, rates, procedures and departmental "
    "documentation. Answers are generated using "
    "retrieved MedCore documents."
)


# ============================================================
# SYSTEM OVERVIEW
# ============================================================

st.subheader("Knowledge Platform")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        label="Departmental Documents",
        value="37",
        help="Processed MedCore Markdown documents",
    )

with m2:
    st.metric(
        label="Departments",
        value="7",
        help="Clinical and administrative departments",
    )

with m3:
    st.metric(
        label="Vector Database",
        value="Chroma",
        help="Persistent local vector store",
    )

with m4:
    st.metric(
        label="AI Model",
        value="Ollama Cloud",
        help="Cloud-hosted LLM used for answer generation",
    )


# ============================================================
# ASK SECTION
# ============================================================

st.subheader("💬 Ask a Question")

st.caption(
    "Search the MedCore knowledge base using natural language."
)


# ============================================================
# SUGGESTED QUESTIONS
# ============================================================

st.write("**Suggested questions**")

q1, q2, q3 = st.columns(3)

selected_question = None

with q1:

    if st.button(
        "💳 General Ward billing limit",
        use_container_width=True,
    ):

        selected_question = (
            "What is the maximum billable quantity "
            "for a General Ward Bed?"
        )


with q2:

    if st.button(
        "🩺 Patient admission procedure",
        use_container_width=True,
    ):

        selected_question = (
            "What is the patient admission procedure?"
        )


with q3:

    if st.button(
        "🔐 IT incident response",
        use_container_width=True,
    ):

        selected_question = (
            "What is the IT incident response procedure?"
        )


# ============================================================
# CHAT INPUT
# ============================================================

question_from_chat = st.chat_input(
    "Ask about a MedCore policy, SOP, guideline, rate or procedure..."
)

question = selected_question or question_from_chat


# ============================================================
# ANSWER
# ============================================================

if question:

    st.divider()

    st.subheader("🔎 Retrieved Answer")

    st.info(
        "✓ This response is generated using information "
        "retrieved from the MedCore knowledge base."
    )

    st.markdown("**Your Question**")

    st.write(question)

    if not rag_ready:

        st.error(
            "The RAG engine is currently unavailable."
        )

        with st.expander("Technical Details"):
            st.code(rag_error)

    else:

        with st.spinner(
            "Searching MedCore documents and generating answer..."
        ):

            try:

                response = query_engine.query(
                    question
                )

                st.markdown("### Answer")

                st.write(str(response))

                st.markdown("### 📚 Source Documents")

                seen_sources = set()

                for source in response.source_nodes:

                    metadata = source.node.metadata

                    department = metadata.get(
                        "department",
                        "Unknown",
                    )

                    filename = metadata.get(
                        "file_name",
                        "Unknown",
                    )

                    document_type = metadata.get(
                        "document_type",
                        "Document",
                    )

                    chunk_number = metadata.get(
                        "chunk_number",
                        "—",
                    )

                    source_key = (
                        department,
                        filename,
                    )

                    if source_key in seen_sources:
                        continue

                    seen_sources.add(source_key)

                    with st.expander(
                        f"📄 {filename}"
                    ):

                        col_a, col_b, col_c = st.columns(3)

                        with col_a:

                            st.caption(
                                "DEPARTMENT"
                            )

                            st.write(
                                department
                            )

                        with col_b:

                            st.caption(
                                "DOCUMENT TYPE"
                            )

                            st.write(
                                document_type
                            )

                        with col_c:

                            st.caption(
                                "CHUNK"
                            )

                            st.write(
                                chunk_number
                            )

                        st.divider()

                        st.markdown(
                            source.node.text[:2500]
                        )

            except Exception as error:

                st.error(
                    "Unable to generate the answer."
                )

                with st.expander(
                    "Technical Details"
                ):

                    st.code(
                        str(error)
                    )


# ============================================================
# EMPTY STATE / CAPABILITIES
# ============================================================

if not question:

    st.subheader("What can I ask?")

    st.caption(
        "Examples of information available in the "
        "MedCore knowledge base."
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        with st.container(border=True):

            st.markdown("### 🩺 Clinical Operations")

            st.write(
                "Admission, discharge, emergency care, "
                "ICU operations and patient transfer procedures."
            )

    with c2:

        with st.container(border=True):

            st.markdown("### 💼 Business Operations")

            st.write(
                "Billing, insurance, refunds, procurement, "
                "HR policies and employee procedures."
            )

    with c3:

        with st.container(border=True):

            st.markdown("### 🔐 Compliance & Tech")

            st.write(
                "Patient consent, privacy, information security "
                "and IT incident response."
            )


# ============================================================
# ARCHITECTURE
# ============================================================

with st.expander("🏗️ View RAG Architecture"):

    st.write(
        "The MedCore RAG pipeline follows this architecture:"
    )

    st.code(
        """
Documents
    ↓
Docling Document Parsing
    ↓
Markdown / Structured Text
    ↓
Table-Aware Chunking
    ↓
BGE-small Embeddings
    ↓
Chroma Vector Database
    ↓
LlamaIndex Retrieval
    ↓
Ollama Cloud LLM
    ↓
Grounded Answer + Source Documents
    """,
        language="text",
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "MedCore Hospitals & Healthcare Services Pvt. Ltd. "
    "• Internal Knowledge Assistant • Academic RAG Project • "
    "Synthetic Organizational Data"
)

st.caption(
    "This application is designed for organizational "
    "knowledge retrieval and is not a patient diagnosis "
    "or treatment system."
)
