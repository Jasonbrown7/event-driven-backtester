import numpy as np
import pandas as pd

def calculate_sharpe_ratio(returns, periods=252):
    return np.sqrt(periods) * (returns.mean() / returns.std())

def calculate_max_drawdown(portfolio_values):
    peak = portfolio_values.expanding(min_periods=1).max()
    drawdown = (portfolio_values - peak) / peak
    return drawdown.min()
