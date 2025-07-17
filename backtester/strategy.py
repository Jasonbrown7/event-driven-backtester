import pandas as pd

class MovingAverageCrossoverStrategy:
    def __init__(self, data, short_window, long_window):
        self.data = data
        self.short_window = short_window
        self.long_window = long_window
        self.signals = pd.DataFrame(index=self.data.index)
        self.signals['short_ma'] = self.data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        self.signals['long_ma'] = self.data['Close'].rolling(window=self.long_window, min_periods=1).mean()
        self.signals['signal'] = 0.0
        self.signals.loc[self.signals['short_ma'] > self.signals['long_ma'], 'signal'] = 1.0
        self.signals['positions'] = self.signals['signal'].diff()
