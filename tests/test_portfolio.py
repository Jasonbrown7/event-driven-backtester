import unittest
import pandas as pd
from backtester.portfolio import BasicPortfolio

class TestPortfolio(unittest.TestCase):
    def test_positions_calculation(self):
        # Create a sample signals DataFrame with a buy and a sell signal
        signals_index = pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03'])
        signals_data = {'positions': [1.0, 0.0, -1.0]}
        signals = pd.DataFrame(data=signals_data, index=signals_index)

        # Create a dummy data DataFrame
        data = pd.DataFrame(index=signals_index)
        data['close_last'] = [100, 101, 102]

        # Instantiate the portfolio
        portfolio = BasicPortfolio(data=data, signals=signals, initial_capital=100000.0)

        # Assert that the final holding is 0
        final_holding = portfolio.positions['holdings'].iloc[-1]
        self.assertEqual(final_holding, 0)

if __name__ == '__main__':
    unittest.main() 