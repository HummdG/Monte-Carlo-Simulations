import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def get_stock_prices(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Close'].values

def monte_carlo_simulation(starting_prices, num_simulations, num_days, returns_std):
    simulations = np.zeros((num_simulations, num_days))
    simulations[:, 0] = starting_prices

    for i in range(1, num_days):
        daily_returns = np.random.normal(0, returns_std, num_simulations)
        simulations[:, i] = simulations[:, i - 1] * (1 + daily_returns)

    return simulations

# Set parameters
ticker = 'AAPL'  # Apple stock symbol
start_date = '2022-01-01'
end_date = '2023-01-01'
historical_prices = get_stock_prices(ticker, start_date, end_date)

num_simulations = 100  # Number of simulations
num_days = 250  # Number of trading days in a year

starting_prices = historical_prices[-num_simulations:]  # Use the last prices for the initial simulations
returns_std = np.std(np.diff(np.log(historical_prices)))  # Use historical daily log returns standard deviation

# Run the simulation
simulations = monte_carlo_simulation(starting_prices, num_simulations, num_days, returns_std)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot simulations
for i in range(num_simulations):
    plt.plot(simulations[i, :], color='blue', alpha=0.1)

# Highlight actual stock prices in a different color
plt.plot(historical_prices, color='red', label='Actual Stock Price')

plt.title('Monte Carlo Simulation of Daily Stock Prices for AAPL')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
