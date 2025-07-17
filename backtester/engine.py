from .data import CsvDataHandler
from .strategy import MovingAverageCrossoverStrategy
from .portfolio import BasicPortfolio
from .performance import calculate_sharpe_ratio, calculate_max_drawdown, calculate_cagr, calculate_volatility

class Backtester:
    def __init__(self, csv_path, short_window, long_window, initial_capital):
        self.data_handler = CsvDataHandler(csv_path)
        self.strategy = MovingAverageCrossoverStrategy(self.data_handler.data, short_window, long_window)
        self.portfolio = BasicPortfolio(self.data_handler.data, self.strategy.signals, initial_capital)

    def run_backtest(self):
        returns = self.portfolio.positions['total'].pct_change().dropna()
        self.sharpe_ratio = calculate_sharpe_ratio(returns)
        self.max_drawdown = calculate_max_drawdown(self.portfolio.positions['total'])
        self.cagr = calculate_cagr(self.portfolio.positions['total'])
        self.volatility = calculate_volatility(returns)
        print("Backtest complete.")
