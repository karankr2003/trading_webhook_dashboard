# Environment Configuration Guide

This document explains all environment variables used in the Trading Dashboard application.

## Environment Files

The application uses three separate `.env` files for different components:

```
trading-dashboard/
 .env # Root level (for test scripts)
 backend/.env # Backend configuration
 frontend/.env # Frontend configuration
```

## Configuration Details

### Root `.env` (Test Scripts)

**Location:** `/.env` 
**Template:** `/.env.example`

```bash
# Backend API URL for test scripts
API_URL=http://localhost:8000
```

**Variables:**
- `API_URL`: The base URL of your backend API
 - **Default:** `http://localhost:8000`
 - **When to change:** If backend runs on different port or host

---

### Backend `.env`

**Location:** `/backend/.env` 
**Template:** `/backend/.env.example`

```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/trading_db
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

**Variables:**

#### `DATABASE_URL`
- **Purpose:** PostgreSQL database connection string
- **Format:** `postgresql://[user]:[password]@[host]:[port]/[database]`
- **Default:** `postgresql://postgres:postgres@localhost:5432/trading_db`
- **When to change:**
 - Different PostgreSQL port (e.g., 5433)
 - Different username/password
 - Remote database host
 - Different database name

**Examples:**
```bash
# Local PostgreSQL on port 5433
DATABASE_URL=postgresql://postgres:mypassword@localhost:5433/trading_db

# Remote PostgreSQL
DATABASE_URL=postgresql://user:pass@db.example.com:5432/trading_db

# Using SQLite instead (for development)
DATABASE_URL=sqlite:///./trading.db
```

#### `CORS_ORIGINS`
- **Purpose:** Allowed origins for Cross-Origin Resource Sharing
- **Format:** Comma-separated list of URLs (no spaces)
- **Default:** `http://localhost:3000,http://localhost:5173`
- **When to change:**
 - Frontend runs on different port
 - Deploying to production with different domain
 - Adding additional allowed origins

**Examples:**
```bash
# Custom frontend port
CORS_ORIGINS=http://localhost:4000,http://localhost:5173

# Production domains
CORS_ORIGINS=https://dashboard.example.com,https://app.example.com

# Allow all (NOT recommended for production)
CORS_ORIGINS=*
```

---

### Frontend `.env`

**Location:** `/frontend/.env` 
**Template:** `/frontend/.env.example`

```bash
VITE_API_URL=http://localhost:8000
```

**Variables:**

#### `VITE_API_URL`
- **Purpose:** Backend API base URL for frontend API calls
- **Format:** Full URL including protocol
- **Default:** `http://localhost:8000`
- **When to change:**
 - Backend runs on different port
 - Backend on different host
 - Production deployment

**Examples:**
```bash
# Backend on port 8001
VITE_API_URL=http://localhost:8001

# Backend on different host
VITE_API_URL=http://192.168.1.100:8000

# Production API
VITE_API_URL=https://api.example.com
```

**Note:** Vite requires environment variables to be prefixed with `VITE_` to be exposed to the client-side code.

---

## Setup Instructions

### First Time Setup

```bash
# 1. Root level (for test scripts)
cp .env.example .env

# 2. Backend
cd backend
cp .env.example .env
cd ..

# 3. Frontend
cd frontend
cp .env.example .env
cd ..
```

### Editing Environment Variables

**Windows:**
```bash
# Use any text editor
notepad .env
notepad backend/.env
notepad frontend/.env
```

**Mac/Linux:**
```bash
# Use nano, vim, or any editor
nano .env
nano backend/.env
nano frontend/.env
```

---

## Security Best Practices

### DO NOT Commit `.env` Files

The `.gitignore` file excludes all `.env` files:
```gitignore
.env
.env.local
.env.*.local
```

### DO Commit `.env.example` Files

Template files should be committed to version control:
- `.env.example`
- `backend/.env.example`
- `frontend/.env.example`

### Production Considerations

1. **Use strong passwords** in DATABASE_URL
2. **Restrict CORS_ORIGINS** to specific domains
3. **Use HTTPS** for production URLs
4. **Store secrets** in secure secret management systems (AWS Secrets Manager, Azure Key Vault, etc.)
5. **Never expose** `.env` files publicly

---

## Testing Different Configurations

### Test with Different Database Port

```bash
# In backend/.env
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/trading_db

# Restart backend
cd backend
uvicorn main:app --reload
```

### Test with Different Frontend Port

```bash
# In frontend/vite.config.ts (already configured)
server: {
 port: 3000
}

# In backend/.env (add to CORS_ORIGINS)
CORS_ORIGINS=http://localhost:3000,http://localhost:4000,http://localhost:5173
```

### Test Backend on Different Port

```bash
# Start backend on port 8001
cd backend
uvicorn main:app --port 8001 --reload

# Update frontend/.env
VITE_API_URL=http://localhost:8001

# Update .env (for test scripts)
API_URL=http://localhost:8001

# Restart frontend
cd frontend
npm run dev
```

---

## Troubleshooting

### "Can't connect to database"
- Check `DATABASE_URL` in `backend/.env`
- Verify PostgreSQL is running: `pg_ctl status`
- Check port number matches your PostgreSQL installation

### "CORS Error" in browser console
- Check `CORS_ORIGINS` in `backend/.env` includes your frontend URL
- Make sure there are no spaces in the comma-separated list
- Restart backend after changing CORS settings

### "Failed to fetch" in frontend
- Check `VITE_API_URL` in `frontend/.env` matches backend URL
- Verify backend is running: `curl http://localhost:8000`
- Restart frontend after changing `.env` file

### Test script fails
- Check `API_URL` in root `.env` matches backend URL
- Install python-dotenv: `pip install python-dotenv`
- Verify backend is accessible: `curl $API_URL`

---

## Default Configuration Summary

**For local development, defaults work out of the box:**

| Component | Variable | Default Value |
|-----------|----------|---------------|
| Root | API_URL | http://localhost:8000 |
| Backend | DATABASE_URL | postgresql://postgres:postgres@localhost:5432/trading_db |
| Backend | CORS_ORIGINS | http://localhost:3000,http://localhost:5173 |
| Frontend | VITE_API_URL | http://localhost:8000 |

**You only need to change these if:**
- PostgreSQL runs on a different port
- You changed default PostgreSQL credentials
- Frontend or backend run on custom ports
- Deploying to production/staging environments
