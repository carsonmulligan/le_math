import numpy as np
import plotly.graph_objects as go
import math
from sympy import primerange, zeta, I
import scipy.stats as stats

# Generate primes in a given range
def generate_primes(lower, upper):
    """
    Generate a list of primes between lower and upper bounds using the Sieve of Eratosthenes.
    
    Parameters:
    lower (int): Lower bound for prime generation.
    upper (int): Upper bound for prime generation.

    Returns:
    list: List of primes between lower and upper bounds.
    """
    return list(primerange(lower, upper))

# Calculate non-trivial zeros of the zeta function
def zeta_zeros(n_zeros):
    """
    Calculate the first 'n_zeros' non-trivial zeros of the Riemann zeta function.

    Parameters:
    n_zeros (int): Number of zeros to calculate.

    Returns:
    list: List of non-trivial zeros of the zeta function.
    """
    zeros = []
    for n in range(1, n_zeros + 1):
        # Riemann zeta zeros occur at approximately 1/2 + it (imaginary part)
        zeros.append((1/2, (n * np.pi)))
    return zeros

# Function to create a curved line between consecutive primes
def create_curved_lines(primes):
    """
    Create a set of curved lines connecting consecutive primes to represent the gaps.

    Parameters:
    primes (list): List of prime numbers.

    Returns:
    tuple: Arrays of x, y, z coordinates for plotting.
    """
    curve_x = []
    curve_y = []
    curve_z = []
    
    # Create curved lines between consecutive primes
    for i in range(len(primes) - 1):
        x0, x1 = primes[i], primes[i + 1]
        mid_x = (x0 + x1) / 2
        gap = (x1 - x0) / 2
        curvature = math.log(gap + 1)  # Use a logarithmic function to emphasize gaps
        
        curve_x.extend([x0, mid_x, x1, None])  # x-coordinates
        curve_y.extend([0, curvature, 0, None])  # y-coordinates
        curve_z.extend([0, 0, 0, None])  # z-coordinates (keep flat)
    
    return curve_x, curve_y, curve_z

# Statistical analysis of prime gaps
def prime_gap_stats(primes):
    """
    Perform statistical analysis on the gaps between consecutive prime numbers.

    Parameters:
    primes (list): List of prime numbers.

    Returns:
    dict: A dictionary containing mean, median, mode, and standard deviation of the prime gaps.
    """
    gaps = np.diff(primes)
    stats_data = {
        'mean': np.mean(gaps),
        'median': np.median(gaps),
        'mode': stats.mode(gaps)[0][0],
        'std_dev': np.std(gaps)
    }
    return stats_data

# Function to visualize prime numbers, zeta zeros, and prime gap statistics
def plot_prime_and_zeta_distribution(primes, zeta_zeros, lower_bound, upper_bound, gap_stats):
    """
    Plot a 3D number line of primes with curved lines to emphasize gaps between primes,
    along with zeta function zeros for comparison.

    Parameters:
    primes (list): List of prime numbers.
    zeta_zeros (list): List of zeros of the Riemann zeta function.
    lower_bound (int): Lower bound for the plot.
    upper_bound (int): Upper bound for the plot.
    gap_stats (dict): Statistical data on the prime gaps.
    """
    # Coordinates for prime markers (flat on the z-axis)
    prime_x = primes
    prime_y = np.zeros(len(primes))
    prime_z = np.zeros(len(primes))
    
    # Create curved lines between consecutive primes
    curve_x, curve_y, curve_z = create_curved_lines(primes)

    # Plot prime points
    prime_trace = go.Scatter3d(
        x=prime_x,
        y=prime_y,
        z=prime_z,
        mode='markers',
        marker=dict(
            size=5,
            color=prime_x,  # Color according to the position on the number line
            colorscale='Viridis',
            opacity=0.8
        ),
        name='Prime Numbers'
    )

    # Plot curved lines between primes
    curve_trace = go.Scatter3d(
        x=curve_x,
        y=curve_y,
        z=curve_z,
        mode='lines',
        line=dict(color='blue', width=2),
        name='Prime Gaps'
    )

    # Plot zeta zeros
    zeta_x = [x[1] for x in zeta_zeros]  # The imaginary part of the zeros
    zeta_y = np.ones(len(zeta_x)) * 2  # Keep y constant for visualization
    zeta_z = np.zeros(len(zeta_x))  # Keep z constant

    zeta_trace = go.Scatter3d(
        x=zeta_x,
        y=zeta_y,
        z=zeta_z,
        mode='markers',
        marker=dict(
            size=4,
            color='red',
            opacity=0.6
        ),
        name='Zeta Zeros'
    )

    # Create the figure
    fig = go.Figure(data=[prime_trace, curve_trace, zeta_trace],
                    layout=go.Layout(
                        title=f'Prime Distribution and Zeta Function Zeros ({lower_bound} to {upper_bound})',
                        scene=dict(
                            xaxis_title='Number Line',
                            yaxis_title='Curved Prime Gaps',
                            zaxis_title='Z (Flat for simplicity)',
                            aspectmode='cube'
                        ),
                        margin=dict(r=10, l=10, b=10, t=40),
                        hovermode='closest',
                        annotations=[{
                            'text': f"Prime Gap Stats: Mean={gap_stats['mean']:.2f}, Median={gap_stats['median']:.2f}, Mode={gap_stats['mode']}, Std Dev={gap_stats['std_dev']:.2f}",
                            'showarrow': False,
                            'xref': 'paper',
                            'yref': 'paper',
                            'x': 0,
                            'y': 1.1,
                            'font': dict(size=12)
                        }]
                    ))

    fig.show()

# Function to allow interactive exploration with a slider
def explore_prime_and_zeta_distribution(lower_bound, upper_bound, step_size, n_zeros):
    """
    Explore prime distribution interactively with zeta zeros and prime gap statistics.

    Parameters:
    lower_bound (int): Starting point of the exploration.
    upper_bound (int): Upper bound of the exploration.
    step_size (int): Interval size to explore the primes in chunks.
    n_zeros (int): Number of Riemann zeta function zeros to plot.
    """
    # Initial bounds
    start = lower_bound
    end = start + step_size
    
    while start < upper_bound:
        # Generate primes for the current range
        primes = generate_primes(start, end)
        
        if primes:
            # Perform statistical analysis on the prime gaps
            gap_stats = prime_gap_stats(primes)
            
            # Calculate the first few non-trivial zeta function zeros
            zeta_zero_vals = zeta_zeros(n_zeros)
            
            # Plot the primes, zeta zeros, and prime gaps for the current range
            plot_prime_and_zeta_distribution(primes, zeta_zero_vals, start, end, gap_stats)
        else:
            print(f"No primes found in the range {start} to {end}")
        
        # Ask the user if they want to continue to the next range
        user_input = input(f"Continue to the next range {end} to {end + step_size}? (y/n): ")
        if user_input.lower() == 'y':
            start = end
            end = start + step_size
        else:
            print("Exploration ended.")
            break

# Main execution
if __name__ == "__main__":
    # Set initial parameters
    lower_bound = 10000  # Start at a higher section of the number line
    upper_bound = 1000000  # Explore up to 1 million
    step_size = 10000  # Chunk size for prime exploration
    n_zeros = 10  # Number of zeta function zeros to visualize
    
    # Start interactive exploration
