import pandas as pd

class BasicPortfolio:
    def __init__(self, data, signals, initial_capital):
        self.data = data
        self.signals = signals
        self.initial_capital = initial_capital
        self.positions = pd.DataFrame(index=signals.index)
        self.positions['holdings'] = self.signals['positions'].cumsum() * 100
        self.positions['cash'] = self.initial_capital - (self.signals['positions'] * 100 * self.data['close_last']).cumsum()
        self.positions['total'] = self.positions['cash'] + self.positions['holdings'] * self.data['close_last']
