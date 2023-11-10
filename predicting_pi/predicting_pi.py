import mpmath
import matplotlib.pyplot as plt

def estimate_pi(num_samples):
    points_inside_circle = 0

    for _ in range(num_samples):
        x = mpmath.rand()
        y = mpmath.rand()

        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

    pi_estimate = mpmath.mpf(4 * points_inside_circle) / mpmath.mpf(num_samples)
    return pi_estimate

# Set the precision to 30 decimal places
mpmath.mp.dps = 30

# List to store the estimated values of pi for different sample sizes
pi_estimates = []

# List of different sample sizes
sample_sizes = [10, 100, 1000, 10000, 100000, 1000000]

# Estimating pi for each sample size
for num_samples in sample_sizes:
    pi_approximation = estimate_pi(num_samples)
    pi_estimates.append(pi_approximation)

# Plotting the results
plt.plot(sample_sizes, pi_estimates, marker='o')
plt.xscale('log')  # Use a logarithmic scale for the x-axis
plt.axhline(y=mpmath.pi, color='r', linestyle='--', label='True value of pi')
plt.xlabel('Number of Samples')
plt.ylabel('Approximation of pi')
plt.title('Monte Carlo Estimation of Pi for Varying # of Samples')
plt.legend()
plt.show()
