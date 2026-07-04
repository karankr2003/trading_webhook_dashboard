from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL must be set in the environment or .env file")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model
class Trade(Base):
    __tablename__ = "trades"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class TradeRequest(BaseModel):
    symbol: str = Field(..., min_length=1, description="Stock symbol")
    side: str = Field(..., description="Trade side (BUY or SELL)")
    quantity: float = Field(..., gt=0, description="Quantity must be positive")
    price: float = Field(..., gt=0, description="Price must be positive")
    
    @validator('side')
    def validate_side(cls, v):
        if v not in ['BUY', 'SELL']:
            raise ValueError('Side must be either BUY or SELL')
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "symbol": "AAPL",
                "side": "BUY",
                "quantity": 10,
                "price": 210.50
            }
        }

class TradeResponse(BaseModel):
    id: int
    symbol: str
    side: str
    quantity: float
    price: float
    timestamp: datetime
    
    class Config:
        from_attributes = True

class StatsResponse(BaseModel):
    buy_count: int
    sell_count: int
    total_trades: int

# FastAPI app
app = FastAPI(
    title="Trading Dashboard API",
    description="REST API for receiving and managing trade alerts",
    version="1.0.0"
)

# CORS middleware
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.post("/webhook", response_model=TradeResponse, status_code=201)
async def create_trade(trade_request: TradeRequest):
    """
    Receive trade webhook and store in database
    """
    db = SessionLocal()
    try:
        trade = Trade(
            symbol=trade_request.symbol,
            side=trade_request.side,
            quantity=trade_request.quantity,
            price=trade_request.price
        )
        db.add(trade)
        db.commit()
        db.refresh(trade)
        return trade
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        db.close()

@app.get("/trades", response_model=List[TradeResponse])
async def get_trades():
    """
    Get all trades in reverse chronological order
    """
    db = SessionLocal()
    try:
        trades = db.query(Trade).order_by(Trade.timestamp.desc()).all()
        return trades
    finally:
        db.close()

@app.get("/stats", response_model=StatsResponse)
async def get_stats():
    """
    Get trade statistics (BUY/SELL counts)
    """
    db = SessionLocal()
    try:
        buy_count = db.query(Trade).filter(Trade.side == "BUY").count()
        sell_count = db.query(Trade).filter(Trade.side == "SELL").count()
        total_trades = buy_count + sell_count
        
        return {
            "buy_count": buy_count,
            "sell_count": sell_count,
            "total_trades": total_trades
        }
    finally:
        db.close()

@app.get("/")
async def root():
    """
    Health check endpoint
    """
    return {
        "status": "ok",
        "message": "Trading Dashboard API is running",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
