# Event-Driven Backtesting Engine

## Project Overview

This project is a lightweight, event-driven backtesting engine written in Python. It is designed to simulate trading strategies against historical market data, allowing for the analysis of strategy performance before live deployment. The engine is modular, making it easy to swap out different data sources, strategies, or portfolio management techniques.

## Core Features

- **Event-Driven Architecture**: Simulates trading on a bar-by-bar basis for a more realistic test environment.
- **MA Crossover Strategy**: Includes a classic momentum-based strategy (Moving Average Crossover) as a sample implementation.
- **Performance Metrics**: Calculates key metrics like Sharpe Ratio, Maximum Drawdown, CAGR, and Annualized Volatility to evaluate strategy effectiveness and risk.

## System Design & Architecture

The backtester is composed of four main components that work together to run a simulation:

- `data.py` (**Data Handler**): Responsible for loading historical market data from a source (currently CSV files). It standardizes column names and prepares the data for the strategy.
- `strategy.py` (**Strategy**): Contains the logic for generating trading signals (buy/sell). It takes market data as input and produces a series of signals based on its internal rules.
- `portfolio.py` (**Portfolio**): Simulates the execution of trades based on the signals from the Strategy. It manages the portfolio's state, tracking cash, holdings, and the total market value over time.
- `engine.py` (**Backtester Engine**): The core orchestrator. It initializes all components, injects the data into the strategy, passes signals to the portfolio, and runs the main simulation. After the simulation, it calculates and reports the final performance metrics.

## Performance Metrics

The engine currently calculates the following metrics to help evaluate the performance and risk of a trading strategy:

- **Sharpe Ratio**: Measures the risk-adjusted return of the portfolio. A higher Sharpe Ratio indicates better performance for the amount of risk taken.
- **Maximum Drawdown**: Represents the largest peak-to-trough decline in portfolio value, providing an indicator of the potential downside risk of the strategy.
- **CAGR (Compound Annual Growth Rate)**: The annualized rate of return that would be required for an investment to grow from its beginning balance to its ending balance.
- **Annualized Volatility**: A measure of the dispersion of returns for a given security or market index, serving as a common measure of risk.

## How to Run

Follow these steps to set up and run the backtesting engine.

### 1. Environment Setup

First, create and activate a Python virtual environment to manage dependencies.

```bash
# Create the virtual environment
python3 -m venv venv

# Activate it (on macOS/Linux)
source venv/bin/activate

```

Next, install the required packages.

```bash
pip install -r requirements.txt
```

### 2. Prepare Data

Place your historical market data in the `data/` directory. The file should be in CSV format and contain at least a `Date` column and a price column (e.g., `Close/Last`). The script is currently configured to use `data/SPY.csv`.

### 3. Run Unit Tests (Optional)

To ensure all components are working correctly, you can run the suite of unit tests.

```bash
python3 -m unittest discover tests -v
```

### 4. Run the Backtest

Execute the main script to run the backtest with the default parameters defined in `main.py`.

```bash
python3 main.py
```

The script will print a formatted summary of the results to your console. 