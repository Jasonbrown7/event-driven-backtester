from backtester.engine import Backtester

if __name__ == "__main__":
    csv_path = "data/SPY.csv"
    short_window = 50
    long_window = 200
    initial_capital = 100000.0

    backtester = Backtester(csv_path, short_window, long_window, initial_capital)
    backtester.run_backtest()

    final_value = backtester.portfolio.positions['total'].iloc[-1]
    sharpe_ratio = backtester.sharpe_ratio
    max_drawdown = backtester.max_drawdown
    cagr = backtester.cagr
    volatility = backtester.volatility

    print(f"Backtest Results:")
    print(f"-----------------")
    print(f"Final Portfolio Value: ${final_value:,.2f}")
    print(f"CAGR: {cagr:.2%}")
    print(f"Annualized Volatility: {volatility:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")
