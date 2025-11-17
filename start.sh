#!/bin/bash
# Start script for Engineering AI Assistant
# Runs both backend and frontend services

echo "🚀 Starting Engineering AI Assistant..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found"
    echo "Please create .env file from .env.example and configure your API keys"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d venv ]; then
    echo "❌ Error: Virtual environment not found"
    echo "Please run ./setup.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if port 8000 is available
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Warning: Port 8000 is already in use"
    echo "Backend may already be running or another service is using the port"
else
    echo "✅ Port 8000 is available"
fi

# Check if port 8501 is available
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Warning: Port 8501 is already in use"
    echo "Frontend may already be running or another service is using the port"
else
    echo "✅ Port 8501 is available"
fi

echo ""
echo "Starting services..."
echo ""

# Start backend in background
echo "🔧 Starting FastAPI backend on port 8000..."
python run_backend.py > logs/backend.log 2>&1 &
BACKEND_PID=$!
echo "   Backend PID: $BACKEND_PID"

# Wait for backend to start
sleep 3

# Check if backend is running
if ps -p $BACKEND_PID > /dev/null; then
    echo "   ✅ Backend started successfully"
else
    echo "   ❌ Backend failed to start. Check logs/backend.log"
    exit 1
fi

# Start frontend in background
echo "🎨 Starting Streamlit frontend on port 8501..."
python run_frontend.py > logs/frontend.log 2>&1 &
FRONTEND_PID=$!
echo "   Frontend PID: $FRONTEND_PID"

# Wait for frontend to start
sleep 3

# Check if frontend is running
if ps -p $FRONTEND_PID > /dev/null; then
    echo "   ✅ Frontend started successfully"
else
    echo "   ❌ Frontend failed to start. Check logs/frontend.log"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

echo ""
echo "✅ All services started successfully!"
echo ""
echo "📋 Access points:"
echo "   🌐 Frontend (UI):  http://localhost:8501"
echo "   🔧 Backend (API):  http://localhost:8000"
echo "   📚 API Docs:       http://localhost:8000/docs"
echo ""
echo "🔐 Default credentials:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "📝 Process IDs:"
echo "   Backend:  $BACKEND_PID"
echo "   Frontend: $FRONTEND_PID"
echo ""
echo "To stop services:"
echo "   kill $BACKEND_PID $FRONTEND_PID"
echo "   or run: ./stop.sh"
echo ""
echo "📊 Logs:"
echo "   Backend:  logs/backend.log"
echo "   Frontend: logs/frontend.log"
echo ""
echo "Happy querying! 🎉"

# Save PIDs to file for stop script
echo $BACKEND_PID > .backend.pid
echo $FRONTEND_PID > .frontend.pid

