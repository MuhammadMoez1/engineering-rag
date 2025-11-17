#!/bin/bash
# Status check script for Engineering AI Assistant

echo "📊 Engineering AI Assistant - Status Check"
echo "=========================================="
echo ""

# Check backend
echo "🔧 Backend (FastAPI):"
BACKEND_PID=$(lsof -ti:8000)
if [ ! -z "$BACKEND_PID" ]; then
    echo "   ✅ Running (PID: $BACKEND_PID, Port: 8000)"
    echo "   🌐 http://localhost:8000"
    echo "   📚 http://localhost:8000/docs"
else
    echo "   ❌ Not running"
fi

echo ""

# Check frontend
echo "🎨 Frontend (Streamlit):"
FRONTEND_PID=$(lsof -ti:8501)
if [ ! -z "$FRONTEND_PID" ]; then
    echo "   ✅ Running (PID: $FRONTEND_PID, Port: 8501)"
    echo "   🌐 http://localhost:8501"
else
    echo "   ❌ Not running"
fi

echo ""
echo "=========================================="

# Check if both are running
if [ ! -z "$BACKEND_PID" ] && [ ! -z "$FRONTEND_PID" ]; then
    echo "✅ All services are running"
    echo ""
    echo "Ready to use! Open: http://localhost:8501"
elif [ ! -z "$BACKEND_PID" ] || [ ! -z "$FRONTEND_PID" ]; then
    echo "⚠️  Some services are not running"
    echo "Run: ./start.sh to start all services"
else
    echo "❌ No services are running"
    echo "Run: ./start.sh to start all services"
fi

echo ""

# Check logs
if [ -f logs/backend.log ]; then
    BACKEND_LOG_SIZE=$(du -h logs/backend.log | cut -f1)
    echo "📝 Backend log: logs/backend.log ($BACKEND_LOG_SIZE)"
fi

if [ -f logs/frontend.log ]; then
    FRONTEND_LOG_SIZE=$(du -h logs/frontend.log | cut -f1)
    echo "📝 Frontend log: logs/frontend.log ($FRONTEND_LOG_SIZE)"
fi

echo ""

# Check disk usage
if [ -d data ]; then
    DATA_SIZE=$(du -sh data 2>/dev/null | cut -f1)
    echo "💾 Data directory: $DATA_SIZE"
    
    if [ -d data/uploads ]; then
        UPLOADS=$(ls data/uploads 2>/dev/null | wc -l)
        echo "   📄 Uploaded files: $UPLOADS"
    fi
    
    if [ -d data/chroma_db ]; then
        CHROMA_SIZE=$(du -sh data/chroma_db 2>/dev/null | cut -f1)
        echo "   🗄️  Vector DB size: $CHROMA_SIZE"
    fi
fi

