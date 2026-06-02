@echo off
REM AI Compliance Auditor - Windows Startup Script

cls
echo.
echo 🚀 AI Compliance Auditor - Starting on Windows
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo ✅ Python found

REM Check for virtual environment
if exist "venv\Scripts\activate.bat" (
    echo ✅ Virtual environment found
    call venv\Scripts\activate.bat
) else (
    echo ⚠️  Virtual environment not found
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
)

echo.
echo 📦 Installing dependencies...
pip install -r requirements.txt --quiet

echo ✅ Dependencies installed

REM Download spacy model
echo.
echo 🧠 Downloading Spacy model...
python -m spacy download en_core_web_sm --quiet

echo ✅ Spacy model downloaded

REM Check .env file
echo.
if exist ".env" (
    echo ✅ .env file found
) else (
    echo ⚠️  .env file not found
    echo Create one with your API keys
    echo Example:
    echo   OPENROUTER_API_KEY=your_key_here
    echo   NEO4J_URI=bolt://localhost:7687
)

REM Start streamlit
echo.
echo 🔥 Starting Streamlit dashboard...
echo 📊 Dashboard will open at: http://localhost:8501
echo.

streamlit run app.py

pause
