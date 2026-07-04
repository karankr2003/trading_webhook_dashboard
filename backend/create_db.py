"""
Database initialization script
Run this to manually create the database tables
"""
from sqlalchemy import create_engine
from main import Base, DATABASE_URL

def init_db():
 """Initialize database tables"""
 print(" Initializing database...")
 print(f" Database URL: {DATABASE_URL}")
 
 try:
 engine = create_engine(DATABASE_URL)
 Base.metadata.create_all(bind=engine)
 print(" Database tables created successfully!")
 print("\nTables created:")
 print(" - trades (id, symbol, side, quantity, price, timestamp)")
 except Exception as e:
 print(f" Error creating database tables: {e}")
 print("\nTroubleshooting:")
 print("1. Ensure PostgreSQL is running")
 print("2. Verify database 'trading_db' exists")
 print("3. Check DATABASE_URL in .env file")
 print("4. Verify PostgreSQL credentials")

if __name__ == "__main__":
 init_db()
