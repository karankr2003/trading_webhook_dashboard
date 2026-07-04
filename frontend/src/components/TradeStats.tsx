import type { TradeStats as TradeStatsType } from '../types/trade';
import './TradeStats.css';

interface TradeStatsProps {
  stats: TradeStatsType;
}

export const TradeStats = ({ stats }: TradeStatsProps) => {
  return (
    <div className="stats-container">
      <div className="stat-card buy">
        <h3>BUY Orders</h3>
        <p className="stat-value">{stats.buy_count}</p>
      </div>
      <div className="stat-card sell">
        <h3>SELL Orders</h3>
        <p className="stat-value">{stats.sell_count}</p>
      </div>
      <div className="stat-card total">
        <h3>Total Trades</h3>
        <p className="stat-value">{stats.total_trades}</p>
      </div>
    </div>
  );
};
