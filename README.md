# 🚀 AI Compliance Auditor Dashboard

> **GraphRAG-powered Privacy & Compliance Analysis Platform**

Transform your compliance auditing with AI. Upload privacy policies and source code to get instant analysis of permissions, compliance risks, and recommendations.

---

## ⚡ Quick Start (Windows)

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2️⃣ Run the Dashboard
**Option A: Double-click**
```
run.bat
```

**Option B: Terminal**
```bash
streamlit run app.py
```

### 3️⃣ Use the Dashboard
- 🌐 Browser opens automatically at `http://localhost:8501`
- 📄 Upload privacy policy PDF
- 💻 Upload source code
- 🔥 Click "Analyze App"
- 📊 View results

---

## 🎯 Dashboard Features

### 📤 Upload Section
- Drag-and-drop PDF upload
- Multi-format source code support (txt, py, java, js, swift)
- Real-time file validation

### 🔍 Analysis Pipeline
```
PDF + Code
   ↓
Chunking (500 chars)
   ↓
Chunk Scoring (importance ranking)
   ↓
Embedding Generation (ChromaDB)
   ↓
Semantic Retrieval
   ↓
Entity Extraction
   ↓
Graph Context (Neo4j)
   ↓
LLM Analysis (OpenRouter)
   ↓
Results Display
```

### 📊 Results Shown
1. **📱 Detected Permissions**
   - Camera, Location, Contacts, etc.
   - Ranked by importance

2. **🔗 Graph Knowledge**
   - Relationships to GDPR, Privacy Laws
   - Entity connections
   - Compliance frameworks

3. **⚠️ Compliance Risks**
   - Privacy vulnerabilities
   - Missing disclosures
   - Data handling issues

4. **💡 Recommendations**
   - How to fix issues
   - Best practices
   - Required notices

---

## 📁 Project Structure

```
rag-compliance-ai/
│
├── app.py                    # 🎯 Main Streamlit dashboard
├── requirements.txt          # 📦 Python dependencies
├── run.bat                   # 🪟 Windows startup script
├── run.sh                    # 🐧 Linux/Mac startup script
├── SETUP_GUIDE.md           # 📚 Detailed setup instructions
├── README.md                # 📖 This file
│
├── Core RAG Components:
├── rag_pipeline.py          # Text chunking logic
├── embeddings.py            # Vector embedding generation
├── chroma_store.py          # Vector database (ChromaDB)
│
├── Data Loading:
├── pdf_loader.py            # Extract text from PDFs
├── code_loader.py           # Load source code files
│
├── Analysis:
├── entity_extractor.py      # NER (Named Entity Recognition)
├── audit_retrieval.py       # Chunk importance scoring
├── llm.py                   # LLM integration (OpenRouter)
│
├── Graph Database:
├── neo4j_graph.py           # Neo4j connections & queries
├── knowledge_graph.py       # Graph relationships
│
├── Testing:
├── test_rag.py              # RAG pipeline tests
├── test_embedding.py        # Embedding tests
├── test_neo4j.py            # Neo4j connection tests
│
├── Sample Files:
├── sample_app_code.txt      # Example source code
├── sample.pdf              # Example privacy policy
│
└── uploads/                # Directory for uploaded files
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit 1.32 |
| **Backend** | Python 3.8+ |
| **Vector DB** | ChromaDB |
| **Graph DB** | Neo4j |
| **Embeddings** | Sentence Transformers |
| **LLM** | OpenRouter (GPT-3.5-turbo) |
| **NER** | SpaCy |

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
# OpenRouter API (Get from https://openrouter.ai)
OPENROUTER_API_KEY=your_api_key_here

# Neo4j Graph Database
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

# ChromaDB (usually automatic)
CHROMA_DB_PATH=./chroma_data
```

---

## 🚀 Usage Guide

### Basic Workflow

1. **Prepare Files**
   - Privacy Policy (PDF format recommended)
   - Source Code (any common format)

2. **Upload to Dashboard**
   - Click "Upload Privacy Policy"
   - Click "Upload Source Code"
   - Files are validated automatically

3. **Run Analysis**
   - Click "Analyze App" button
   - Wait for processing (1-2 minutes)
   - See results in real-time

4. **Review Results**
   - Permissions detected
   - Risk assessment
   - Graph relationships
   - Recommendations

### Advanced Usage

**Batch Analysis:**
```python
# See test_rag.py for programmatic usage
python test_rag.py
```

**Custom Questions:**
Edit `app.py` line ~120 to add more compliance checks:
```python
compliance_questions = [
    "Your custom question here?",
    "Another compliance check?",
]
```

---

## 🔧 Customization

### Change LLM Model
Edit `llm.py` line 24:
```python
model="openai/gpt-3.5-turbo",  # Change this
```

### Adjust Chunk Size
Edit `rag_pipeline.py` line 1:
```python
def chunk_text(text, chunk_size=500):  # Adjust 500
```

### Add More Compliance Questions
Edit `app.py` line ~120:
```python
compliance_questions = [
    "Your question 1?",
    "Your question 2?",
]
```

### Custom Styling
Edit CSS in `app.py` lines ~38-55

---

## 🐛 Troubleshooting

### Error: "Streamlit not found"
```bash
pip install streamlit --upgrade
```

### Error: "spacy model not found"
```bash
python -m spacy download en_core_web_sm
```

### Error: "OPENROUTER_API_KEY not found"
1. Get API key from https://openrouter.ai
2. Create `.env` file with the key
3. Restart Streamlit

### Error: "Neo4j connection failed"
1. Check Neo4j is running
2. Verify credentials in `.env`
3. Test with `test_neo4j.py`

### Error: "ChromaDB error"
```bash
pip install chromadb --upgrade
pip install pydantic --upgrade
```

---

## 📈 Performance Tips

- **Faster processing**: Use smaller documents (< 10 pages)
- **Better results**: Use clear, well-formatted PDFs
- **Caching**: Results are cached in session state
- **Batch analysis**: Process similar documents together

---

## 🔒 Security Notes

1. **API Keys**: Never commit `.env` file
2. **File Upload**: Files are processed in memory
3. **Neo4j**: Use strong passwords
4. **Data**: Clean up uploads/ directory regularly

---

## 📚 Learning Resources

### Understanding GraphRAG
- [RAG Basics](https://docs.llamaindex.ai/)
- [Vector Embeddings](https://huggingface.co/tasks/embeddings)
- [Graph Databases](https://neo4j.com/docs/)

### Streamlit Documentation
- [Getting Started](https://docs.streamlit.io/)
- [Widgets & Components](https://docs.streamlit.io/library/api-reference)

### OpenRouter API
- [API Docs](https://openrouter.ai/docs/api/introduction)
- [Models List](https://openrouter.ai/docs/models)

---

## 🚢 Deployment

### Option 1: Streamlit Cloud
```bash
git push
# Then connect to Streamlit Cloud
```

### Option 2: Docker
```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
```

### Option 3: AWS/GCP/Azure
Deploy as serverless function or containerized app

---

## 🤝 Contributing

Found a bug? Have an idea?
1. Create an issue
2. Fork the repository
3. Make improvements
4. Submit a pull request

---

## 📝 License

MIT License - Feel free to use and modify

---

## 💬 Support

**Need help?**
1. Check `SETUP_GUIDE.md` for detailed instructions
2. Review error messages carefully
3. Check test files for usage examples
4. Verify all dependencies installed

---

## 🎉 What's Next?

- ✅ Dashboard running
- 🔄 Custom compliance rules
- 📊 Export reports as PDF
- 🔗 Real-time graph visualization
- 🤖 Multi-document analysis
- 📈 Analytics dashboard
- 🌍 Deployment to cloud

---

**Built with ❤️ using Streamlit + GraphRAG + Neo4j**

*Making compliance auditing smarter, faster, and accessible to everyone.*
