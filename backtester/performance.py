import numpy as np
import pandas as pd

def calculate_sharpe_ratio(returns, periods=252):
    return np.sqrt(periods) * (returns.mean() / returns.std())

def calculate_max_drawdown(portfolio_values):
    peak = portfolio_values.expanding(min_periods=1).max()
    drawdown = (portfolio_values - peak) / peak
    return drawdown.min()

def calculate_cagr(portfolio_values):
    years = (portfolio_values.index[-1] - portfolio_values.index[0]).days / 365.25
    if years <= 0:
        return 0
    return (portfolio_values.iloc[-1] / portfolio_values.iloc[0]) ** (1 / years) - 1

def calculate_volatility(returns, periods=252):
    return returns.std() * np.sqrt(periods)
