#!/bin/bash
# Quick startup script for AI Compliance Auditor

echo "🚀 AI Compliance Auditor - Starting..."
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found"

# Check if in virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Not in virtual environment. Activating..."
    # Windows
    if [[ "$OS" == "Windows_NT" ]]; then
        if [ -d "venv/Scripts" ]; then
            source venv/Scripts/activate
        else
            echo "❌ Virtual environment not found. Create with: python -m venv venv"
            exit 1
        fi
    # Linux/Mac
    else
        if [ -d "venv/bin" ]; then
            source venv/bin/activate
        else
            echo "❌ Virtual environment not found. Create with: python -m venv venv"
            exit 1
        fi
    fi
fi

echo "✅ Virtual environment activated"

# Install requirements
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt --quiet

echo "✅ Dependencies installed"

# Download spacy model
echo ""
echo "🧠 Downloading Spacy model..."
python -m spacy download en_core_web_sm --quiet

echo "✅ Spacy model downloaded"

# Check .env file
echo ""
if [ -f ".env" ]; then
    echo "✅ .env file found"
else
    echo "⚠️  .env file not found. Create one with your API keys"
    echo "   Example:"
    echo "   OPENROUTER_API_KEY=your_key_here"
    echo "   NEO4J_URI=bolt://localhost:7687"
fi

# Start streamlit
echo ""
echo "🔥 Starting Streamlit dashboard..."
echo "📊 Dashboard will open at: http://localhost:8501"
echo ""

streamlit run app.py
