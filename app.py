# from neo4j_graph import get_graph_context

# graph_data[entity] = get_graph_context(entity)


# context += f"\n\nGraph Knowledge:\n{graph_data}"

import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv
import tempfile

# Import your RAG components
from pdf_loader import load_pdf
from code_loader import load_code_file
from rag_pipeline import chunk_text
from embeddings import generate_embeddings, generate_query_embedding
from chroma_store import store_chunks, retrieve_chunks
from entity_extractor import extract_entities
from neo4j_graph import get_graph_context
from audit_retrieval import calculate_chunk_score
from llm import ask_llm

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Compliance Auditor",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.2em;
    }
    .success-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .risk-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .info-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    </style>
""", unsafe_allow_html=True)

# Title and header
st.title("🚀 AI Compliance Auditor")
st.markdown("---")
st.write("Upload privacy policy and source code to analyze compliance risks using GraphRAG")

# Initialize session state
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None


def run_rag_analysis(pdf_text, code_text):
    """Run the complete RAG pipeline"""
    try:
        with st.spinner("🔄 Processing files..."):
            # Step 1: Combine texts
            combined_text = pdf_text + "\n\n" + code_text
            
            # Step 2: Chunk text
            st.info("📦 Chunking documents...")
            chunks = chunk_text(combined_text)
            st.write(f"✅ Created {len(chunks)} chunks")
            
            # Step 3: Score chunks
            st.info("📊 Scoring chunks by relevance...")
            scored_chunks = []
            for chunk in chunks:
                score = calculate_chunk_score(chunk, "privacy_policy.pdf")
                scored_chunks.append((chunk, score))
            
            scored_chunks.sort(key=lambda x: x[1], reverse=True)
            top_chunks = [chunk for chunk, score in scored_chunks[:10]]
            st.write(f"✅ Selected top {len(top_chunks)} chunks")
            
            # Step 4: Generate embeddings
            st.info("🧠 Generating embeddings...")
            embeddings = generate_embeddings(top_chunks)
            st.write("✅ Embeddings generated")
            
            # Step 5: Store in ChromaDB
            st.info("💾 Storing in ChromaDB...")
            store_chunks(top_chunks, embeddings)
            st.write("✅ Chunks stored")
            
            # Step 6: Query for compliance issues
            st.info("🔍 Running compliance analysis...")
            
            compliance_questions = [
                "What privacy risks exist in this app?",
                "What permissions are requested?",
                "What tracking mechanisms are present?",
                "What GDPR compliance issues exist?",
                "What data collection practices need disclosure?"
            ]
            
            results = {
                "permissions": [],
                "risks": [],
                "graph_knowledge": [],
                "recommendations": []
            }
            
            for question in compliance_questions:
                query_embedding = generate_query_embedding(question)
                retrieved_results = retrieve_chunks(query_embedding)
                
                if retrieved_results and retrieved_results.get('documents'):
                    retrieved_docs = retrieved_results['documents'][0]
                    context = "\n".join(retrieved_docs)
                    
                    # Extract entities
                    entities = extract_entities(context)
                    
                    # Get graph context
                    for entity in entities:
                        try:
                            graph_data = get_graph_context(entity)
                            results["graph_knowledge"].append({
                                "entity": entity,
                                "context": graph_data
                            })
                        except:
                            pass
                    
                    # Get LLM answer
                    answer = ask_llm(context, question)
                    
                    if "risk" in question.lower():
                        results["risks"].append(answer)
                    elif "permission" in question.lower():
                        results["permissions"].append(answer)
                    else:
                        results["recommendations"].append(answer)
            
            return results
            
    except Exception as e:
        st.error(f"❌ Error during analysis: {str(e)}")
        return None


def display_results(results):
    """Display analysis results in a beautiful format"""
    
    if not results:
        return
    
    col1, col2 = st.columns(2)
    
    # Detected Permissions
    with col1:
        st.subheader("📱 Detected Permissions")
        if results["permissions"]:
            for i, perm in enumerate(results["permissions"], 1):
                st.markdown(f"""
                <div class="info-box">
                <strong>Permission {i}:</strong><br/>
                {perm}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No specific permissions detected")
    
    # Graph Knowledge
    with col2:
        st.subheader("🔗 Graph Knowledge")
        if results["graph_knowledge"]:
            for item in results["graph_knowledge"]:
                with st.expander(f"📌 {item['entity']}"):
                    st.write(item['context'])
        else:
            st.info("No graph relationships detected")
    
    st.markdown("---")
    
    # Compliance Risks
    st.subheader("⚠️ Compliance Risks")
    if results["risks"]:
        for i, risk in enumerate(results["risks"], 1):
            st.markdown(f"""
            <div class="risk-box">
            <strong>Risk {i}:</strong><br/>
            {risk}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("✅ No major risks detected!")
    
    st.markdown("---")
    
    # Recommendations
    st.subheader("💡 Recommendations")
    if results["recommendations"]:
        for i, rec in enumerate(results["recommendations"], 1):
            st.markdown(f"""
            <div class="success-box">
            <strong>Recommendation {i}:</strong><br/>
            {rec}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No recommendations at this time")


# Main content
st.markdown("### 📤 Upload Files")

col1, col2 = st.columns(2)

with col1:
    pdf_file = st.file_uploader(
        "📄 Upload Privacy Policy (PDF)",
        type=["pdf"],
        key="pdf_uploader"
    )

with col2:
    code_file = st.file_uploader(
        "💻 Upload Source Code",
        type=["txt", "py", "java", "js", "swift"],
        key="code_uploader"
    )

st.markdown("---")

# Analyze button
if st.button("🔥 Analyze App", use_container_width=True):
    if pdf_file is None:
        st.error("❌ Please upload a Privacy Policy PDF")
    elif code_file is None:
        st.error("❌ Please upload Source Code")
    else:
        # Save uploaded files temporarily
        with tempfile.TemporaryDirectory() as tmpdir:
            # Save PDF
            pdf_path = os.path.join(tmpdir, "privacy_policy.pdf")
            with open(pdf_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            
            # Save code
            code_path = os.path.join(tmpdir, f"code_file{Path(code_file.name).suffix}")
            with open(code_path, "wb") as f:
                f.write(code_file.getbuffer())
            
            # Load files
            try:
                pdf_text = load_pdf(pdf_path)
                code_text = load_code_file(code_path)
                
                st.success("✅ Files loaded successfully!")
                
                # Run analysis
                results = run_rag_analysis(pdf_text, code_text)
                
                if results:
                    st.session_state.analysis_complete = True
                    st.session_state.analysis_results = results
                    st.success("✅ Analysis Complete!")
                    
            except Exception as e:
                st.error(f"❌ Error loading files: {str(e)}")

# Display results if analysis is complete
if st.session_state.analysis_complete and st.session_state.analysis_results:
    st.markdown("---")
    st.markdown("### 📊 Analysis Results")
    display_results(st.session_state.analysis_results)

# Sidebar info
with st.sidebar:
    st.markdown("### ℹ️ About This Tool")
    st.write("""
    **AI Compliance Auditor** uses GraphRAG to:
    
    - 📖 Read privacy policies
    - 💾 Analyze source code
    - 🔍 Extract compliance risks
    - 🤖 Generate recommendations
    
    **Technology Stack:**
    - Frontend: Streamlit
    - Backend: Python GraphRAG
    - Vector DB: ChromaDB
    - Graph DB: Neo4j
    - LLM: OpenRouter GPT-3.5
    """)
    
    st.markdown("---")
    
    if st.button("🔄 Clear Results"):
        st.session_state.analysis_complete = False
        st.session_state.analysis_results = None
        st.rerun()
