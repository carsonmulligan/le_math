import numpy as np
import matplotlib.pyplot as plt
from sympy import primerange

# Generate primes up to 1 million using SymPy's primerange
primes = list(primerange(1, 1000001))

# 1. Prime Gaps
def plot_prime_gaps(primes):
    """
    Plots the gaps between consecutive prime numbers.
    """
    prime_gaps = np.diff(primes)  # Calculate gaps between consecutive primes
    plt.figure(figsize=(10, 6))
    plt.plot(primes[:-1], prime_gaps, 'bo-', markersize=2)
    plt.title("Prime Gaps Between Consecutive Primes (1 to 1 Million)")
    plt.xlabel("Prime Number")
    plt.ylabel("Gap")
    plt.grid(True)
    plt.show()

# 2. Prime Density (Histogram)
def plot_prime_density(primes):
    """
    Plots a histogram showing the density of primes in different intervals between 1 and 1 million.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(primes, bins=100, color='green', alpha=0.75)
    plt.title("Prime Number Density (1 to 1 Million)")
    plt.xlabel("Number")
    plt.ylabel("Prime Count in Each Bin")
    plt.grid(True)
    plt.show()

# 3. Cumulative Prime Count
def plot_cumulative_prime_count(primes):
    """
    Plots the cumulative number of primes found up to each prime, showing the total prime count as numbers increase.
    """
    cumulative_count = np.arange(1, len(primes) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(primes, cumulative_count, 'r-', linewidth=2)
    plt.title("Cumulative Prime Count (1 to 1 Million)")
    plt.xlabel("Prime Number")
    plt.ylabel("Cumulative Count of Primes")
    plt.grid(True)
    plt.show()

# 4. Prime Distribution (Logarithmic Scale)
def plot_prime_distribution_log(primes):
    """
    Plots the prime numbers on a logarithmic scale to observe their distribution.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(primes, 'b-', markersize=1)
    plt.xscale('log')  # Logarithmic scale for better visualization of larger primes
    plt.title("Prime Distribution on a Logarithmic Scale (1 to 1 Million)")
    plt.xlabel("Index (log scale)")
    plt.ylabel("Prime Number")
    plt.grid(True, which="both")
    plt.show()

# 5. Prime Number Histogram (Logarithmic Binning)
def plot_prime_histogram_log(primes):
    """
    Plots a histogram with logarithmic bins to analyze the distribution of prime numbers at different scales.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(primes, bins=np.logspace(np.log10(1), np.log10(1000000), 100), color='purple', alpha=0.75)
    plt.xscale('log')
    plt.title("Prime Number Distribution (Logarithmic Binning)")
    plt.xlabel("Number (Log Scale)")
    plt.ylabel("Prime Count")
    plt.grid(True, which="both")
    plt.show()

# Main execution
if __name__ == "__main__":
    # Call each analysis function one by one
    plot_prime_gaps(primes)              # Analyze gaps between consecutive primes
    plot_prime_density(primes)           # Analyze the density of primes in different intervals
    plot_cumulative_prime_count(primes)  # Plot cumulative count of primes
    plot_prime_distribution_log(primes)  # Plot prime distribution on a logarithmic scale
    plot_prime_histogram_log(primes)     # Analyze prime distribution with logarithmic binning
