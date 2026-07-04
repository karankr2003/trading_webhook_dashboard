# Trading Dashboard

A full-stack trading dashboard application that receives trade alerts via REST API and displays them in a real-time web interface.

## Tech Stack

**Frontend:**
- React 18 with TypeScript
- Vite (Build tool)
- CSS3 (No external UI libraries)

**Backend:**
- FastAPI (Python)
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- Pydantic (Validation)

## Prerequisites

Before running this application, ensure you have the following installed:

- **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.9 or higher) - [Download](https://www.python.org/)
- **PostgreSQL** (v12 or higher) - [Download](https://www.postgresql.org/)
- **npm** or **yarn** (comes with Node.js)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/karankr2003/trading_webhook_dashboard.git
cd trading_webhook_dashboard
```

### 2. Database Setup

**Create PostgreSQL Database:**

```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE trading_db;

# Exit psql
\q
```

**Or using pgAdmin or any PostgreSQL client:**
- Create a new database named `trading_db`

### 3. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (bash):
source venv/Scripts/activate

# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from template
cp .env.example .env

# Edit .env if needed (update DATABASE_URL and CORS_ORIGINS if your setup differs)
# DATABASE_URL=postgresql://postgres:postgres@localhost:5432/trading_db
# CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

**Environment Variables (backend/.env):**
- `DATABASE_URL`: PostgreSQL connection string (default: postgresql://postgres:postgres@localhost:5432/trading_db)
- `CORS_ORIGINS`: Comma-separated list of allowed origins (default: http://localhost:3000,http://localhost:5173)

**Note:** The application will automatically create the required database tables on first run.

### 4. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create .env file from template
cp .env.example .env

# Edit .env if backend runs on different port (optional)
# VITE_API_URL=http://localhost:8000
```

**Environment Variables (frontend/.env):**
- `VITE_API_URL`: Backend API base URL (default: http://localhost:8000)

## Running the Application

### Start Backend Server

```bash
# In the backend directory with virtual environment activated
cd backend
source venv/Scripts/activate # Windows bash
uvicorn main:app --reload

# Backend will run on: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

### Start Frontend Server

```bash
# In a new terminal, navigate to frontend directory
cd frontend
npm run dev

# Frontend will run on: http://localhost:3000
```

### Access the Application

- **Dashboard UI:** http://localhost:3000
- **API Docs (Swagger):** http://localhost:8000/docs
- **API Docs (ReDoc):** http://localhost:8000/redoc

## API Endpoints

### POST /webhook
Receive trade alerts and store them in the database.

**Request Body:**
```json
{
 "symbol": "AAPL",
 "side": "BUY",
 "quantity": 10,
 "price": 210.50
}
```

**Response:**
```json
{
 "id": 1,
 "symbol": "AAPL",
 "side": "BUY",
 "quantity": 10,
 "price": 210.50,
 "timestamp": "2026-07-03T10:30:00.000Z"
}
```

**Validation Rules:**
- `symbol`: Required string (min 1 character)
- `side`: Must be either "BUY" or "SELL"
- `quantity`: Must be a positive number
- `price`: Must be a positive number

### GET /trades
Retrieve all trades in reverse chronological order.

**Response:**
```json
[
 {
 "id": 2,
 "symbol": "GOOGL",
 "side": "SELL",
 "quantity": 5,
 "price": 2800.00,
 "timestamp": "2026-07-03T10:31:00.000Z"
 },
 {
 "id": 1,
 "symbol": "AAPL",
 "side": "BUY",
 "quantity": 10,
 "price": 210.50,
 "timestamp": "2026-07-03T10:30:00.000Z"
 }
]
```

### GET /stats
Get trade statistics (BUY/SELL counts).

**Response:**
```json
{
 "buy_count": 15,
 "sell_count": 8,
 "total_trades": 23
}
```

## Testing the API

### Using Python Test Script

```bash
# Create root .env file (if not exists)
cp .env.example .env

# Run the test script
python test_webhook.py
```

**Environment Variables (root .env):**
- `API_URL`: Backend API URL for testing (default: http://localhost:8000)

### Using cURL

```bash
# Send a BUY trade
curl -X POST http://localhost:8000/webhook \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "AAPL",
 "side": "BUY",
 "quantity": 10,
 "price": 210.50
 }'

# Send a SELL trade
curl -X POST http://localhost:8000/webhook \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "TSLA",
 "side": "SELL",
 "quantity": 5,
 "price": 850.25
 }'

# Get all trades
curl http://localhost:8000/trades

# Get statistics
curl http://localhost:8000/stats
```

### Using Postman or Thunder Client

1. Create a new POST request to `http://localhost:8000/webhook`
2. Set header: `Content-Type: application/json`
3. Add JSON body as shown in the cURL examples
4. Send the request

### Using FastAPI Swagger UI

1. Navigate to http://localhost:8000/docs
2. Click on `/webhook` endpoint
3. Click "Try it out"
4. Enter the trade data
5. Click "Execute"

## Project Structure

```
trading-dashboard/
 backend/
 main.py # FastAPI application
 requirements.txt # Python dependencies
 .env.example # Environment variables template
 .env # Local environment config (create from .env.example)
 venv/ # Virtual environment (created)
 frontend/
 src/
 components/
 TradeTable.tsx # Trade table component
 TradeTable.css
 TradeStats.tsx # Statistics component
 TradeStats.css
 services/
 api.ts # API service layer
 types/
 trade.ts # TypeScript types
 App.tsx # Main app component
 App.css
 main.tsx # Entry point
 package.json
 tsconfig.json
 vite.config.ts
 .env.example # Environment variables template
 .env # Local environment config (create from .env.example)
 .env.example # Root environment variables (for test scripts)
 .env # Root local config (create from .env.example)
 README.md
```

## Features

### Core Features
- REST API webhook endpoint (`POST /webhook`)
- JSON payload validation
- PostgreSQL database storage
- React dashboard with TypeScript
- Trade history table
- BUY/SELL order statistics
- Request validation with error messages
- Comprehensive documentation

### Additional Features
- Auto-refresh (polls every 5 seconds)
- Manual refresh button
- Responsive design
- Error handling
- Loading states
- Empty state handling
- Type-safe frontend with TypeScript
- FastAPI automatic API documentation
- CORS enabled for local development

## Troubleshooting

### Database Connection Issues

**Error:** `could not connect to server`

**Solution:**
1. Ensure PostgreSQL is running: `pg_ctl status` or check services
2. Verify database exists: `psql -U postgres -l`
3. Check credentials in backend/.env match your PostgreSQL setup

### Port Already in Use

**Backend (Port 8000):**
```bash
# Find process using port
netstat -ano | findstr :8000 # Windows
lsof -i :8000 # Mac/Linux

# Kill the process or use different port
uvicorn main:app --port 8001 --reload
```

**Frontend (Port 3000):**
```bash
# Kill the process or edit vite.config.ts to use different port
```

### CORS Issues

If you see CORS errors in browser console:
1. Ensure backend is running
2. Check that frontend origin is allowed in `main.py` CORS settings
3. Clear browser cache

### Module Not Found

**Backend:**
```bash
# Ensure virtual environment is activated
source venv/Scripts/activate # Windows bash
pip install -r requirements.txt
```

**Frontend:**
```bash
# Ensure dependencies are installed
npm install
```

## Database Schema

**trades table:**
| Column | Type | Constraints |
|-----------|-----------|-----------------------|
| id | INTEGER | PRIMARY KEY, AUTO |
| symbol | VARCHAR | NOT NULL |
| side | VARCHAR | NOT NULL (BUY/SELL) |
| quantity | FLOAT | NOT NULL, > 0 |
| price | FLOAT | NOT NULL, > 0 |
| timestamp | TIMESTAMP | DEFAULT NOW() |

## Development

### Backend Development

```bash
# Run with auto-reload
uvicorn main:app --reload

# Run with specific host/port
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Development

```bash
# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

## Notes

- The application uses polling (5-second intervals) for updates. For production, consider implementing WebSockets for real-time updates.
- Database tables are automatically created on first run using SQLAlchemy.
- All timestamps are stored in UTC.
- The frontend includes basic error handling and retry mechanisms.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review FastAPI docs at http://localhost:8000/docs
3. Check browser console for frontend errors
4. Check terminal logs for backend errors

## License

This project is created as a technical assignment.
