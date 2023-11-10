import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(starting_price, num_simulations, num_days, revenue_growth_mean, revenue_growth_std, 
                            operating_margin_mean, operating_margin_std, 
                            capital_ratio_mean, capital_ratio_std, 
                            cost_of_capital_mean, cost_of_capital_std):
    simulations = np.zeros((num_simulations, num_days))
    simulations[:, 0] = starting_price

    for i in range(1, num_days):
        # Generate random numbers from normal distributions
        revenue_growth = np.random.normal(revenue_growth_mean, revenue_growth_std, num_simulations)
        operating_margin = np.random.normal(operating_margin_mean, operating_margin_std, num_simulations)
        capital_ratio = np.random.normal(capital_ratio_mean, capital_ratio_std, num_simulations)
        cost_of_capital = np.random.normal(cost_of_capital_mean, cost_of_capital_std, num_simulations)

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

# Parameters for Gaussian distributions
revenue_growth_mean, revenue_growth_std = -0.001, 0.0002
operating_margin_mean, operating_margin_std = 0.00001, 0.001
capital_ratio_mean, capital_ratio_std = -0.0001, 0.001
cost_of_capital_mean, cost_of_capital_std = -0.002, 0.0001

# Run the simulation
simulations = monte_carlo_simulation(starting_price, num_simulations, num_days,
                                     revenue_growth_mean, revenue_growth_std,
                                     operating_margin_mean, operating_margin_std,
                                     capital_ratio_mean, capital_ratio_std,
                                     cost_of_capital_mean, cost_of_capital_std)

# Plot the results
plt.figure(figsize=(10, 6))
for i in range(num_simulations):
    plt.plot(simulations[i, :])

plt.title('Monte Carlo Simulation of Daily Stock Prices with Variable Factors (Gaussian Distribution)')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.show()
