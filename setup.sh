#!/bin/bash
# Setup script for Engineering AI Assistant

echo "🔧 Setting up Engineering AI Assistant..."

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Download spaCy models
echo "🌍 Downloading spaCy language models..."
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p data/uploads
mkdir -p data/temp
mkdir -p data/chroma_db
mkdir -p logs

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️ IMPORTANT: Please edit .env file with your API keys!"
else
    echo "✅ .env file already exists"
fi

# Initialize database
echo "🗄️ Initializing database..."
python app/database/init_db.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your API keys (OpenAI, Azure)"
echo "2. Start backend: python run_backend.py"
echo "3. Start frontend: python run_frontend.py"
echo "4. Open browser: http://localhost:8501"
echo ""
echo "📖 Default credentials:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "🚀 Happy coding!"

