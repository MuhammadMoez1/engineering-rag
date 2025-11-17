#!/usr/bin/env python3
"""Installation verification script for Engineering AI Assistant."""

import sys
import importlib
from pathlib import Path


def check_python_version():
    """Check if Python version is adequate."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} (requires 3.10+)")
        return False


def check_package(package_name, import_name=None):
    """Check if a package is installed."""
    if import_name is None:
        import_name = package_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"   ✅ {package_name} ({version})")
        return True
    except ImportError:
        print(f"   ❌ {package_name} not found")
        return False


def check_packages():
    """Check if required packages are installed."""
    print("\n📦 Checking required packages...")
    
    packages = [
        ("fastapi", "fastapi"),
        ("uvicorn", "uvicorn"),
        ("streamlit", "streamlit"),
        ("openai", "openai"),
        ("chromadb", "chromadb"),
        ("langchain", "langchain"),
        ("sqlalchemy", "sqlalchemy"),
        ("pypdf", "pypdf"),
        ("python-docx", "docx"),
        ("openpyxl", "openpyxl"),
        ("pillow", "PIL"),
        ("sentence-transformers", "sentence_transformers"),
    ]
    
    results = []
    for package_name, import_name in packages:
        results.append(check_package(package_name, import_name))
    
    return all(results)


def check_optional_packages():
    """Check optional packages."""
    print("\n🔧 Checking optional packages...")
    
    packages = [
        ("spacy", "spacy"),
        ("azure-ai-formrecognizer", "azure.ai.formrecognizer"),
        ("pytesseract", "pytesseract"),
    ]
    
    for package_name, import_name in packages:
        check_package(package_name, import_name)


def check_directories():
    """Check if required directories exist."""
    print("\n📁 Checking directories...")
    
    directories = [
        "app",
        "ui",
        "tests",
        "data",
        "data/uploads",
        "data/temp",
        "data/chroma_db",
        "logs",
    ]
    
    all_exist = True
    for directory in directories:
        path = Path(directory)
        if path.exists():
            print(f"   ✅ {directory}/")
        else:
            print(f"   ❌ {directory}/ (will be created)")
            all_exist = False
    
    return all_exist


def check_config_file():
    """Check if .env file exists."""
    print("\n⚙️  Checking configuration...")
    
    env_file = Path(".env")
    example_file = Path(".env.example")
    
    if env_file.exists():
        print("   ✅ .env file exists")
        
        # Check if OpenAI key is configured
        with open(env_file, 'r') as f:
            content = f.read()
            if "your-openai-api-key-here" in content or "sk-proj-" not in content:
                print("   ⚠️  Warning: OPENAI_API_KEY may not be configured")
            else:
                print("   ✅ OPENAI_API_KEY appears to be set")
        
        return True
    elif example_file.exists():
        print("   ⚠️  .env file not found (template exists)")
        print("      Run: cp .env.example .env")
        return False
    else:
        print("   ❌ Neither .env nor .env.example found")
        return False


def check_spacy_models():
    """Check if spaCy models are downloaded."""
    print("\n🌍 Checking spaCy language models...")
    
    try:
        import spacy
        
        models = ["en_core_web_sm", "fr_core_news_sm"]
        results = []
        
        for model in models:
            try:
                spacy.load(model)
                print(f"   ✅ {model}")
                results.append(True)
            except OSError:
                print(f"   ❌ {model} (run: python -m spacy download {model})")
                results.append(False)
        
        return all(results)
    except ImportError:
        print("   ⚠️  spaCy not installed")
        return False


def test_imports():
    """Test if core modules can be imported."""
    print("\n🔍 Testing core module imports...")
    
    modules = [
        "app.core.config",
        "app.core.security",
        "app.core.embeddings",
        "app.services.document_processor",
        "app.services.vector_store",
        "app.services.rag_service",
        "app.main",
    ]
    
    results = []
    for module in modules:
        try:
            importlib.import_module(module)
            print(f"   ✅ {module}")
            results.append(True)
        except Exception as e:
            print(f"   ❌ {module}: {str(e)[:50]}")
            results.append(False)
    
    return all(results)


def main():
    """Run all verification checks."""
    print("=" * 60)
    print("Engineering AI Assistant - Installation Verification")
    print("=" * 60)
    
    checks = [
        ("Python Version", check_python_version()),
        ("Required Packages", check_packages()),
        ("Configuration", check_config_file()),
        ("Directories", check_directories()),
        ("spaCy Models", check_spacy_models()),
        ("Module Imports", test_imports()),
    ]
    
    # Optional checks (don't affect overall status)
    check_optional_packages()
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for check_name, result in checks:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {check_name}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print("\n" + "=" * 60)
    
    if failed == 0:
        print("🎉 All checks passed! Installation is complete.")
        print("\nNext steps:")
        print("1. Configure .env file with your API keys")
        print("2. Run: python run_backend.py")
        print("3. Run: python run_frontend.py")
        print("4. Open: http://localhost:8501")
        return 0
    else:
        print(f"⚠️  {failed} check(s) failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("- Install missing packages: pip install -r requirements.txt")
        print("- Download spaCy models: python -m spacy download en_core_web_sm")
        print("- Create .env file: cp .env.example .env")
        return 1


if __name__ == "__main__":
    sys.exit(main())

