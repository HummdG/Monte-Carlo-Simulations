import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(starting_price, num_simulations, num_days, revenue_growth_range, operating_margin_range, capital_ratio_range, cost_of_capital_range):
    simulations = np.zeros((num_simulations, num_days))
    simulations[:, 0] = starting_price

    for i in range(1, num_days):
        # Generate random numbers from triangular distributions
        revenue_growth = np.random.triangular(*revenue_growth_range, num_simulations)
        operating_margin = np.random.triangular(*operating_margin_range, num_simulations)
        capital_ratio = np.random.triangular(*capital_ratio_range, num_simulations)
        cost_of_capital = np.random.triangular(*cost_of_capital_range, num_simulations)

        # Calculate daily free cash flow
        daily_free_cash_flow = simulations[:, i - 1] * (1 + revenue_growth) * operating_margin - simulations[:, i - 1] * capital_ratio

        # Discount daily free cash flow to present value using cost of capital
        present_value = daily_free_cash_flow / (1 + cost_of_capital)

        # Update stock price based on the present value
        simulations[:, i] = simulations[:, i - 1] + present_value

    return simulations

# Set parameters
starting_price = 100  # Initial stock price
num_simulations = 100  # Number of simulations
num_days = 20  # Number of trading days in a year
revenue_growth_range = (-0.0001, 0.0005, 0.001)  # Triangle distribution for daily revenue growth
operating_margin_range = (-0.0005, 0.0005, 0.002)  # Triangle distribution for daily operating margin
capital_ratio_range = (0.0002, 0.0003, 0.001)  # Triangle distribution for daily capital ratio
cost_of_capital_range = (0.0001, 0.0002, 0.0005)  # Triangle distribution for daily cost of capital

# Run the simulation
simulations = monte_carlo_simulation(starting_price, num_simulations, num_days, revenue_growth_range, operating_margin_range, capital_ratio_range, cost_of_capital_range)

# Plot the results
plt.figure(figsize=(10, 6))
for i in range(num_simulations):
    plt.plot(simulations[i, :])

plt.title('Monte Carlo Simulation of Daily Stock Prices with Variable Factors (Triangle Distribution)')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.show()
