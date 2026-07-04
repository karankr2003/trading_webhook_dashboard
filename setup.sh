#!/bin/bash

echo " Trading Dashboard Setup Script"
echo "=================================="
echo ""

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
 echo " PostgreSQL is not installed. Please install PostgreSQL first."
 exit 1
fi

echo " PostgreSQL found"
echo ""

# Create database
echo " Creating database..."
psql -U postgres -c "CREATE DATABASE trading_db;" 2>/dev/null
if [ $? -eq 0 ]; then
 echo " Database 'trading_db' created successfully"
else
 echo " Database might already exist (this is okay)"
fi
echo ""

# Backend setup
echo " Setting up backend..."
cd backend

if [ ! -d "venv" ]; then
 echo "Creating virtual environment..."
 python -m venv venv
fi

echo "Activating virtual environment..."
source venv/Scripts/activate || source venv/bin/activate

echo "Installing Python dependencies..."
pip install -r requirements.txt

if [ ! -f ".env" ]; then
 echo "Creating .env file..."
 cp .env.example .env
fi

cd ..
echo " Backend setup complete"
echo ""

# Frontend setup
echo " Setting up frontend..."
cd frontend

if [ ! -d "node_modules" ]; then
 echo "Installing npm dependencies..."
 npm install
fi

if [ ! -f ".env" ]; then
 echo "Creating .env file..."
 cp .env.example .env
fi

cd ..
echo " Frontend setup complete"
echo ""

echo " Setup complete!"
echo ""
echo "To start the application:"
echo ""
echo "1⃣ Start Backend (in one terminal):"
echo " cd backend"
echo " source venv/Scripts/activate # Windows bash"
echo " uvicorn main:app --reload"
echo ""
echo "2⃣ Start Frontend (in another terminal):"
echo " cd frontend"
echo " npm run dev"
echo ""
echo "3⃣ Access the dashboard:"
echo " Frontend: http://localhost:3000"
echo " API Docs: http://localhost:8000/docs"
echo ""
