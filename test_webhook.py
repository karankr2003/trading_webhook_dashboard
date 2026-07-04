#!/usr/bin/env python3
"""
Test script for Trading Dashboard webhook endpoint
"""
import requests
import json
import time
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")

def send_trade(trade_data: Dict[str, Any]) -> None:
    """Send a trade to the webhook endpoint"""
    try:
        response = requests.post(
            f"{API_URL}/webhook",
            json=trade_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 201:
            print(f"Success: {response.json()}")
        else:
            print(f"Error ({response.status_code}): {response.json()}")
    except Exception as e:
        print(f"Request failed: {e}")
    print()

def get_trades() -> None:
    """Fetch all trades"""
    try:
        response = requests.get(f"{API_URL}/trades")
        if response.status_code == 200:
            trades = response.json()
            print(f"Total trades: {len(trades)}")
            for trade in trades[:5]:  # Show first 5
                print(f"   {trade}")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Request failed: {e}")
    print()

def get_stats() -> None:
    """Fetch trade statistics"""
    try:
        response = requests.get(f"{API_URL}/stats")
        if response.status_code == 200:
            stats = response.json()
            print(f"Statistics:")
            print(f"   BUY orders: {stats['buy_count']}")
            print(f"   SELL orders: {stats['sell_count']}")
            print(f"   Total trades: {stats['total_trades']}")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Request failed: {e}")
    print()

def main():
    print("Testing Trading Dashboard Webhook")
    print("=" * 50)
    print()
    
    # Test 1: Valid BUY trade
    print("Test 1: Sending BUY trade for AAPL...")
    send_trade({
        "symbol": "AAPL",
        "side": "BUY",
        "quantity": 10,
        "price": 210.50
    })
    time.sleep(1)
    
    # Test 2: Valid SELL trade
    print("Test 2: Sending SELL trade for TSLA...")
    send_trade({
        "symbol": "TSLA",
        "side": "SELL",
        "quantity": 5,
        "price": 850.25
    })
    time.sleep(1)
    
    # Test 3: Valid BUY trade
    print("Test 3: Sending BUY trade for GOOGL...")
    send_trade({
        "symbol": "GOOGL",
        "side": "BUY",
        "quantity": 3,
        "price": 2800.00
    })
    time.sleep(1)
    
    # Test 4: Valid SELL trade
    print("Test 4: Sending SELL trade for MSFT...")
    send_trade({
        "symbol": "MSFT",
        "side": "SELL",
        "quantity": 15,
        "price": 380.75
    })
    time.sleep(1)
    
    # Test 5: Invalid trade - missing field
    print("Test 5: Testing validation (missing quantity - should fail)...")
    send_trade({
        "symbol": "AMZN",
        "side": "BUY",
        "price": 3400.00
    })
    time.sleep(1)
    
    # Test 6: Invalid trade - invalid side
    print("Test 6: Testing validation (invalid side - should fail)...")
    send_trade({
        "symbol": "NFLX",
        "side": "HOLD",
        "quantity": 8,
        "price": 450.00
    })
    time.sleep(1)
    
    # Test 7: Invalid trade - negative quantity
    print("Test 7: Testing validation (negative quantity - should fail)...")
    send_trade({
        "symbol": "META",
        "side": "BUY",
        "quantity": -5,
        "price": 350.00
    })
    time.sleep(1)
    
    # Test 8: Invalid trade - zero price
    print("Test 8: Testing validation (zero price - should fail)...")
    send_trade({
        "symbol": "NVDA",
        "side": "BUY",
        "quantity": 10,
        "price": 0
    })
    time.sleep(1)
    
    # Fetch all trades
    print("Fetching all trades...")
    get_trades()
    
    # Fetch statistics
    print("Fetching statistics...")
    get_stats()
    
    print("Testing complete!")
    print()
    print("Check your dashboard at http://localhost:3000 to see the results!")

if __name__ == "__main__":
    main()
