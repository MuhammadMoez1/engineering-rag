@echo off
REM Setup script for Engineering AI Assistant (Windows)

echo Setting up Engineering AI Assistant...

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Download spaCy models
echo Downloading spaCy language models...
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm

REM Create necessary directories
echo Creating directories...
if not exist "data\uploads" mkdir data\uploads
if not exist "data\temp" mkdir data\temp
if not exist "data\chroma_db" mkdir data\chroma_db
if not exist "logs" mkdir logs

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo IMPORTANT: Please edit .env file with your API keys!
) else (
    echo .env file already exists
)

REM Initialize database
echo Initializing database...
python app\database\init_db.py

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file with your API keys (OpenAI, Azure)
echo 2. Start backend: python run_backend.py
echo 3. Start frontend: python run_frontend.py
echo 4. Open browser: http://localhost:8501
echo.
echo Default credentials:
echo    Username: admin
echo    Password: admin123
echo.
echo Happy coding!
pause

