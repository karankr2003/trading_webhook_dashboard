# Quick Start Guide

Get the Trading Dashboard running in 5 minutes!

## Prerequisites Checklist

- [ ] Node.js 18+ installed (`node --version`)
- [ ] Python 3.9+ installed (`python --version`)
- [ ] PostgreSQL 12+ installed and running
- [ ] Git (optional, for cloning)

## Quick Setup

### 1. Create Database (2 minutes)

```bash
# Open PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE trading_db;

# Exit
\q
```

### 2. Backend Setup (2 minutes)

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate # Windows bash

# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload
```

**Backend is now running on:** http://localhost:8000

### 3. Frontend Setup (1 minute)

Open a **new terminal**:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Frontend is now running on:** http://localhost:3000

## You're Ready!

1. **Open Dashboard:** http://localhost:3000
2. **View API Docs:** http://localhost:8000/docs

## Test It Out

### Option 1: Use the Test Script

```bash
# In a new terminal
python test_webhook.py
```

### Option 2: Use cURL

```bash
curl -X POST http://localhost:8000/webhook \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "AAPL",
 "side": "BUY",
 "quantity": 10,
 "price": 210.50
 }'
```

### Option 3: Use Swagger UI

1. Go to http://localhost:8000/docs
2. Click on `POST /webhook`
3. Click "Try it out"
4. Enter trade data
5. Click "Execute"

## View Results

Refresh your dashboard at http://localhost:3000 to see:
- Trade history table
- BUY/SELL statistics
- Real-time updates (auto-refreshes every 5 seconds)

## Common Issues

### Database Connection Failed
```bash
# Check PostgreSQL is running
pg_ctl status

# Or restart it
pg_ctl restart
```

### Port Already in Use
```bash
# Backend: Use different port
uvicorn main:app --port 8001 --reload

# Frontend: Edit vite.config.ts and change port
```

### Module Not Found (Backend)
```bash
# Ensure virtual environment is activated
source venv/Scripts/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Module Not Found (Frontend)
```bash
# Reinstall node modules
rm -rf node_modules
npm install
```

## Next Steps

- Read [README.md](README.md) for detailed documentation
- Explore API documentation at http://localhost:8000/docs
- Check database schema and validation rules
- Test edge cases and error handling

## Assignment Checklist

Core Requirements:
- [x] REST API with POST /webhook endpoint
- [x] JSON payload validation (Symbol, Side, Quantity, Price)
- [x] PostgreSQL database storage
- [x] React dashboard with trade table
- [x] BUY/SELL order statistics
- [x] Request validation with error messages
- [x] README with setup instructions

Bonus Features:
- [ ] Docker containerization (optional)
- [ ] WebSocket live updates (optional)
- [ ] Profit/loss calculations (optional)

## Tips

1. **Auto-reload is enabled** - code changes automatically restart servers
2. **API docs are interactive** - test endpoints directly in browser
3. **Check browser console** - for frontend errors and logs
4. **Check terminal logs** - for backend errors and requests
5. **Database persists data** - trades remain after server restart

## Need Help?

1. Check the troubleshooting section in README.md
2. Verify all prerequisites are installed
3. Ensure PostgreSQL is running
4. Check that both servers are running on correct ports
5. Look for error messages in terminal or browser console

Happy coding! 
