#!/bin/bash
# Stop script for Engineering AI Assistant

echo "🛑 Stopping Engineering AI Assistant..."
echo ""

# Check if PID files exist
if [ ! -f .backend.pid ] && [ ! -f .frontend.pid ]; then
    echo "⚠️  No running services found (PID files missing)"
    echo ""
    echo "Attempting to find and kill processes by port..."
    
    # Try to kill by port
    BACKEND_PID=$(lsof -ti:8000)
    FRONTEND_PID=$(lsof -ti:8501)
    
    if [ ! -z "$BACKEND_PID" ]; then
        echo "Found backend on port 8000 (PID: $BACKEND_PID)"
        kill $BACKEND_PID 2>/dev/null && echo "✅ Backend stopped" || echo "❌ Failed to stop backend"
    fi
    
    if [ ! -z "$FRONTEND_PID" ]; then
        echo "Found frontend on port 8501 (PID: $FRONTEND_PID)"
        kill $FRONTEND_PID 2>/dev/null && echo "✅ Frontend stopped" || echo "❌ Failed to stop frontend"
    fi
    
    exit 0
fi

# Read PIDs from files
if [ -f .backend.pid ]; then
    BACKEND_PID=$(cat .backend.pid)
    if ps -p $BACKEND_PID > /dev/null 2>&1; then
        echo "Stopping backend (PID: $BACKEND_PID)..."
        kill $BACKEND_PID 2>/dev/null
        sleep 1
        if ps -p $BACKEND_PID > /dev/null 2>&1; then
            echo "   Force killing backend..."
            kill -9 $BACKEND_PID 2>/dev/null
        fi
        echo "   ✅ Backend stopped"
    else
        echo "   ⚠️  Backend not running"
    fi
    rm .backend.pid
fi

if [ -f .frontend.pid ]; then
    FRONTEND_PID=$(cat .frontend.pid)
    if ps -p $FRONTEND_PID > /dev/null 2>&1; then
        echo "Stopping frontend (PID: $FRONTEND_PID)..."
        kill $FRONTEND_PID 2>/dev/null
        sleep 1
        if ps -p $FRONTEND_PID > /dev/null 2>&1; then
            echo "   Force killing frontend..."
            kill -9 $FRONTEND_PID 2>/dev/null
        fi
        echo "   ✅ Frontend stopped"
    else
        echo "   ⚠️  Frontend not running"
    fi
    rm .frontend.pid
fi

echo ""
echo "✅ All services stopped"

