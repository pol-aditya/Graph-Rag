# 🚀 AI Compliance Auditor - Setup & Run Guide

## 📋 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Download Spacy Model
This is needed for entity extraction:
```bash
python -m spacy download en_core_web_sm
```

### Step 3: Verify Environment
Make sure your `.env` file has:
```
OPENROUTER_API_KEY=your_api_key_here
NEO4J_URI=your_neo4j_uri
NEO4J_USER=your_neo4j_user
NEO4J_PASSWORD=your_neo4j_password
```

### Step 4: Run the Dashboard
```bash
streamlit run app.py
```

This will:
- 🌐 Open your browser automatically
- 📊 Launch the dashboard at `http://localhost:8501`
- 🎨 Show the beautiful compliance auditor UI

---

## 📊 What Your Dashboard Does

### Upload Section
- 📄 Upload Privacy Policy PDF
- 💻 Upload Source Code (txt, py, java, js, swift)

### Analysis Pipeline
1. **File Loading** - Extracts text from PDF & code
2. **Chunking** - Splits documents into manageable pieces
3. **Scoring** - Ranks chunks by relevance
4. **Embeddings** - Converts chunks to vectors
5. **Storage** - Saves to ChromaDB
6. **Analysis** - Runs compliance checks via LLM
7. **Graph** - Queries Neo4j for relationships

### Results Display
- 📱 **Detected Permissions** - What the app accesses
- 🔗 **Graph Knowledge** - Relationships & context
- ⚠️ **Compliance Risks** - Privacy/security issues
- 💡 **Recommendations** - How to fix issues

---

## 🔥 Features

✅ File upload with drag & drop
✅ Beautiful responsive UI
✅ Real-time processing
✅ Error handling
✅ Session state management
✅ Result caching
✅ Sidebar information
✅ Clear results button

---

## 🛠️ Troubleshooting

### Issue: Streamlit not found
```bash
pip install streamlit --upgrade
```

### Issue: Spacy model not found
```bash
python -m spacy download en_core_web_sm
```

### Issue: Environment variables not loaded
Make sure `.env` file is in the same directory as `app.py`

### Issue: ChromaDB errors
```bash
pip install chromadb --upgrade
```

### Issue: Neo4j connection fails
Check that:
- Neo4j is running
- Credentials in `.env` are correct
- Network connection is available

---

## 📚 Project Structure

```
rag-compliance-ai/
├── app.py                  # 🎯 Main Streamlit dashboard
├── requirements.txt        # 📦 Dependencies
├── pdf_loader.py          # 📄 Loads PDFs
├── code_loader.py         # 💻 Loads source code
├── rag_pipeline.py        # 🔄 Chunking logic
├── embeddings.py          # 🧠 Vector embeddings
├── chroma_store.py        # 💾 Vector storage
├── llm.py                 # 🤖 LLM integration
├── entity_extractor.py    # 🏷️ Entity extraction
├── neo4j_graph.py         # 🔗 Graph database
├── audit_retrieval.py     # 📊 Chunk scoring
└── uploads/               # 📁 Uploaded files
```

---

## 🚀 Next Steps

After running the dashboard:

1. **Test with sample files**
   - Use `sample.pdf` as privacy policy
   - Use `sample_app_code.txt` as source code

2. **Customize analysis**
   - Add more compliance questions
   - Integrate with your LLM
   - Connect your Neo4j database

3. **Deploy to production**
   - Use Streamlit Cloud
   - Use Docker
   - Use AWS/GCP/Azure

---

## 💡 Usage Tips

### Best File Formats
- **Privacy Policies**: PDF format
- **Source Code**: Plain text files
- **Supported Languages**: Python, Java, Swift, JavaScript

### For Best Results
- Use clear, well-formatted documents
- Keep privacy policies under 50 pages
- Use readable source code

### Performance Tips
- Analyze smaller documents first (< 10 pages)
- Use the same document for multiple queries
- Cache results for repeated analyses

---

## 🆘 Need Help?

Check:
1. All files exist in the directory
2. Virtual environment is activated
3. All dependencies installed: `pip list`
4. `.env` file has all keys
5. Neo4j is running (if using graph DB)

---

**Built with ❤️ using Streamlit + GraphRAG**
