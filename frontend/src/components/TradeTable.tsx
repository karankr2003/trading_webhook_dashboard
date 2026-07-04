import type { Trade } from '../types/trade';
import './TradeTable.css';

interface TradeTableProps {
  trades: Trade[];
}

export const TradeTable = ({ trades }: TradeTableProps) => {
  const formatDate = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
    });
  };

  const formatPrice = (price: number) => {
    return `$${price.toFixed(2)}`;
  };

  if (trades.length === 0) {
    return (
      <div className="empty-state">
        <p>No trades yet. Waiting for webhook data...</p>
      </div>
    );
  }

  return (
    <div className="table-container">
      <table className="trade-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Symbol</th>
            <th>Side</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {trades.map((trade) => (
            <tr key={trade.id}>
              <td>{trade.id}</td>
              <td className="symbol">{trade.symbol}</td>
              <td>
                <span className={`side-badge ${trade.side.toLowerCase()}`}>
                  {trade.side}
                </span>
              </td>
              <td>{trade.quantity}</td>
              <td>{formatPrice(trade.price)}</td>
              <td className="timestamp">{formatDate(trade.timestamp)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
