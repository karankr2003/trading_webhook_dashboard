import { useState, useEffect } from 'react';
import { TradeTable } from './components/TradeTable';
import { TradeStats } from './components/TradeStats';
import type { Trade, TradeStats as TradeStatsType } from './types/trade';
import { api } from './services/api';
import './App.css';

function App() {
  const [trades, setTrades] = useState<Trade[]>([]);
  const [stats, setStats] = useState<TradeStatsType>({
    buy_count: 0,
    sell_count: 0,
    total_trades: 0,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    try {
      setError(null);
      const [tradesData, statsData] = await Promise.all([
        api.getTrades(),
        api.getStats(),
      ]);
      setTrades(tradesData);
      setStats(statsData);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch data');
      console.error('Error fetching data:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    
    // Poll for updates every 5 seconds
    const interval = setInterval(fetchData, 5000);
    
    return () => clearInterval(interval);
  }, []);

  const handleRefresh = () => {
    setLoading(true);
    fetchData();
  };

  return (
    <div className="app">
      <header className="header">
        <div className="header-content">
          <div className="brand-block">
            <p className="eyebrow">Market intelligence</p>
            <h1>Trading Dashboard</h1>
            <p className="subtext">Monitor incoming buy and sell alerts with a clean, real-time view.</p>
          </div>
          <button 
            onClick={handleRefresh} 
            className="refresh-button"
            disabled={loading}
          >
            {loading ? 'Refreshing...' : 'Refresh'}
          </button>
        </div>
      </header>

      <main className="main-content">
        <section className="overview-card">
          <div>
            <span className="status-pill">● Live feed</span>
            <h2>Realtime trade monitoring</h2>
            <p>Every webhook event is captured instantly and reflected in the latest market activity feed.</p>
          </div>
          <div className="overview-meta">
            <span>Updated</span>
            <strong>{new Date().toLocaleTimeString()}</strong>
          </div>
        </section>

        {error && (
          <div className="error-banner">
            <p>Warning: {error}</p>
            <button onClick={handleRefresh}>Retry</button>
          </div>
        )}

        <TradeStats stats={stats} />
        
        <div className="trades-section">
          <div className="section-heading">
            <h2>Recent Trades</h2>
            <span className="section-chip">Live activity</span>
          </div>
          {loading && trades.length === 0 ? (
            <div className="loading">Loading trades...</div>
          ) : (
            <TradeTable trades={trades} />
          )}
        </div>
      </main>

      <footer className="footer">
        <p>Last updated: {new Date().toLocaleTimeString()}</p>
      </footer>
    </div>
  );
}

export default App;
