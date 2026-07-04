import type { Trade, TradeStats } from '../types/trade';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = {
  async getTrades(): Promise<Trade[]> {
    const response = await fetch(`${API_BASE_URL}/trades`);
    if (!response.ok) {
      throw new Error('Failed to fetch trades');
    }
    return response.json();
  },

  async getStats(): Promise<TradeStats> {
    const response = await fetch(`${API_BASE_URL}/stats`);
    if (!response.ok) {
      throw new Error('Failed to fetch stats');
    }
    return response.json();
  },
};
