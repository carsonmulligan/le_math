import numpy as np
import plotly.graph_objects as go
import math
from sympy import primerange, zeta, I
from scipy.stats import describe

# Generate primes in a given range
def generate_primes(lower, upper):
    """
    Generate a list of primes between lower and upper bounds.
    
    Parameters:
    lower (int): Lower bound for prime generation.
    upper (int): Upper bound for prime generation.

    Returns:
    list: List of primes between lower and upper bounds.
    """
    return list(primerange(lower, upper))

# Function to calculate the non-trivial zeros of the Riemann zeta function
def zeta_zeros(num_zeros):
    """
    Generate a list of the first non-trivial zeros of the Riemann zeta function.
    
    Parameters:
    num_zeros (int): Number of zeta zeros to generate.

    Returns:
    list: Imaginary parts of the first non-trivial zeros of the Riemann zeta function.
    """
    zeros = []
    for n in range(1, num_zeros + 1):
        zeta_zero = zeta(0.5 + n * I)
        zeros.append(zeta_zero.imag)
    return zeros

# Function to create curved paths between consecutive primes
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
    
    for i in range(len(primes) - 1):
        x0, x1 = primes[i], primes[i + 1]
        mid_x = (x0 + x1) / 2
        gap = (x1 - x0) / 2
        curvature = math.log(gap + 1)  # Logarithmic curve to emphasize gaps
        
        curve_x.extend([x0, mid_x, x1, None])  # x-coordinates
        curve_y.extend([0, curvature, 0, None])  # y-coordinates
        curve_z.extend([0, 0, 0, None])  # z-coordinates (flat for simplicity)
    
    return curve_x, curve_y, curve_z

# Statistical analysis of prime gaps
def analyze_prime_gaps(primes):
    """
    Analyze the gaps between consecutive prime numbers.
    
    Parameters:
    primes (list): List of prime numbers.

    Returns:
    dict: Descriptive statistics of the prime gaps.
    """
    prime_gaps = np.diff(primes)
    stats = describe(prime_gaps)
    return {
        'mean_gap': stats.mean,
        'variance_gap': stats.variance,
        'min_gap': stats.minmax[0],
        'max_gap': stats.minmax[1]
    }

# Function to visualize primes, prime gaps, and zeta function zeros in 3D
def plot_prime_solar_system(primes, zeta_zeros, lower_bound, upper_bound):
    """
    Plot a 3D number line of primes with curved lines to emphasize gaps between primes, and plot the non-trivial 
    zeros of the Riemann zeta function alongside the primes.

    Parameters:
    primes (list): List of prime numbers.
    zeta_zeros (list): List of non-trivial zeros of the Riemann zeta function.
    lower_bound (int): Lower bound for the plot.
    upper_bound (int): Upper bound for the plot.
    """
    # Coordinates for prime markers (like planets)
    prime_x = primes
    prime_y = np.zeros(len(primes))
    prime_z = np.zeros(len(primes))
    
    # Coordinates for zeta zeros (like stars)
    zeta_x = np.linspace(lower_bound, upper_bound, len(zeta_zeros))
    zeta_y = zeta_zeros
    zeta_z = np.zeros(len(zeta_zeros))
    
    # Create curved lines between consecutive primes
    curve_x, curve_y, curve_z = create_curved_lines(primes)

    # Plot prime points (planets)
    prime_trace = go.Scatter3d(
        x=prime_x,
        y=prime_y,
        z=prime_z,
        mode='markers',
        marker=dict(
            size=7,
            color=prime_x,  # Color according to their position on the number line
            colorscale='Viridis',
            opacity=0.8
        ),
        name='Prime Numbers (Planets)'
    )

    # Plot curved lines (prime gaps)
    curve_trace = go.Scatter3d(
        x=curve_x,
        y=curve_y,
        z=curve_z,
        mode='lines',
        line=dict(color='blue', width=2),
        name='Prime Gaps (Orbits)'
    )

    # Plot zeta zeros (stars)
    zeta_trace = go.Scatter3d(
        x=zeta_x,
        y=zeta_y,
        z=zeta_z,
        mode='markers',
        marker=dict(
            size=5,
            color='yellow',
            opacity=0.8
        ),
        name='Zeta Zeros (Stars)'
    )

    # Create the figure
    fig = go.Figure(data=[prime_trace, curve_trace, zeta_trace],
                    layout=go.Layout(
                        title=f'Prime Number Solar System ({lower_bound} to {upper_bound})',
                        scene=dict(
                            xaxis_title='Number Line',
                            yaxis_title='Curved Prime Gaps',
                            zaxis_title='Z (Flat for simplicity)',
                            aspectmode='cube'
                        ),
                        margin=dict(r=10, l=10, b=10, t=40),
                        hovermode='closest'
                    ))

    fig.show()

# Main execution
if __name__ == "__main__":
    # Set initial parameters for prime exploration
    lower_bound = 10000  # Start from 10,000 for better visualization
    upper_bound = 100000  # Go up to 100,000 primes
    step_size = 10000  # Step size for prime exploration
    
    # Generate primes and zeta zeros
    primes = generate_primes(lower_bound, upper_bound)
    num_zeros = len(primes)  # Use same number of zeta zeros as primes for comparison
    zeta_zeros_list = zeta_zeros(num_zeros)

    # Plot the prime solar system and zeta function zeros
    plot_prime_solar_system(primes, zeta_zeros_list, lower_bound, upper_bound)

    # Analyze prime gaps
    stats = analyze_prime_gaps(primes)
    print(f"Prime Gap Analysis between {lower_bound} and {upper_bound}:")
    print(f"Mean gap: {stats['mean_gap']}")
    print(f"Variance of gaps: {stats['variance_gap']}")
    print(f"Minimum gap: {stats['min_gap']}")
    print(f"Maximum gap: {stats['max_gap']}")
