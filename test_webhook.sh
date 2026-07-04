#!/bin/bash

echo " Testing Trading Dashboard Webhook"
echo "====================================="
echo ""

API_URL="http://localhost:8000"

# Test 1: Send BUY trade
echo " Test 1: Sending BUY trade for AAPL..."
curl -X POST "$API_URL/webhook" \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "AAPL",
 "side": "BUY",
 "quantity": 10,
 "price": 210.50
 }'
echo -e "\n"

sleep 1

# Test 2: Send SELL trade
echo " Test 2: Sending SELL trade for TSLA..."
curl -X POST "$API_URL/webhook" \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "TSLA",
 "side": "SELL",
 "quantity": 5,
 "price": 850.25
 }'
echo -e "\n"

sleep 1

# Test 3: Send BUY trade
echo " Test 3: Sending BUY trade for GOOGL..."
curl -X POST "$API_URL/webhook" \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "GOOGL",
 "side": "BUY",
 "quantity": 3,
 "price": 2800.00
 }'
echo -e "\n"

sleep 1

# Test 4: Send SELL trade
echo " Test 4: Sending SELL trade for MSFT..."
curl -X POST "$API_URL/webhook" \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "MSFT",
 "side": "SELL",
 "quantity": 15,
 "price": 380.75
 }'
echo -e "\n"

sleep 1

# Test 5: Invalid trade (missing field)
echo " Test 5: Testing validation (missing quantity - should fail)..."
curl -X POST "$API_URL/webhook" \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "AMZN",
 "side": "BUY",
 "price": 3400.00
 }'
echo -e "\n"

sleep 1

# Test 6: Invalid trade (invalid side)
echo " Test 6: Testing validation (invalid side - should fail)..."
curl -X POST "$API_URL/webhook" \
 -H "Content-Type: application/json" \
 -d '{
 "symbol": "NFLX",
 "side": "HOLD",
 "quantity": 8,
 "price": 450.00
 }'
echo -e "\n"

sleep 1

# Get all trades
echo " Fetching all trades..."
curl "$API_URL/trades"
echo -e "\n\n"

# Get statistics
echo " Fetching statistics..."
curl "$API_URL/stats"
echo -e "\n\n"

echo " Testing complete!"
echo ""
echo "Check your dashboard at http://localhost:3000 to see the results!"
