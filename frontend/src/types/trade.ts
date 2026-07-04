export interface Trade {
  id: number;
  symbol: string;
  side: 'BUY' | 'SELL';
  quantity: number;
  price: number;
  timestamp: string;
}

export interface TradeStats {
  buy_count: number;
  sell_count: number;
  total_trades: number;
}
