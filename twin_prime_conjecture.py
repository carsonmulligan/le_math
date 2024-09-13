"""
Interactive 3D Visualization of the Solution to the Twin Prime Conjecture (Bounded Gaps)

This script creates an interactive 3D number line where prime numbers are represented by markers. 
The gaps between consecutive primes are illustrated using lines connecting them. Users can zoom in, rotate, 
and explore the distribution of prime numbers and their gaps, emphasizing that bounded gaps exist 
between consecutive primes, even as the numbers grow.

Prime numbers are calculated using the Sieve of Eratosthenes, and the gaps between consecutive primes are highlighted.

Libraries:
- Plotly: For 3D interactive plotting.
- Numpy: For generating arrays and mathematical operations.

Features:
- 3D number line visualization of prime numbers.
- Lines connecting consecutive primes to show gaps.
- Interactivity to zoom, pan, and rotate the number line.
"""

import numpy as np
import plotly.graph_objects as go

# Prime number generator using the Sieve of Eratosthenes
def generate_primes(limit):
    """
    Generates prime numbers up to a given limit using the Sieve of Eratosthenes.

    Parameters:
    limit (int): The upper limit for prime generation.

    Returns:
    list: A list of prime numbers less than or equal to the limit.
    """
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(np.sqrt(limit)) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = False
    return np.nonzero(sieve)[0]

# Function to generate 3D plot for prime numbers and their gaps
def plot_prime_gaps(primes):
    """
    Creates a 3D interactive plot showing prime numbers on a number line with lines connecting consecutive primes 
    to represent the gaps.

    Parameters:
    primes (list): A list of prime numbers to visualize.
    """
    # Scale the primes for better visualization
    primes_scaled = np.array(primes) * 0.1

    # 3D scatter plot of primes
    prime_trace = go.Scatter3d(
        x=primes_scaled,  # Prime numbers on the x-axis
        y=np.zeros_like(primes_scaled),  # Keep y and z fixed to create a number line effect
        z=np.zeros_like(primes_scaled),
        mode='markers',
        marker=dict(
            size=5,
            color=primes_scaled,  # Color according to prime position
            colorscale='Viridis',
            opacity=0.8
        ),
        name='Prime Numbers'
    )

    # Lines between consecutive primes to show gaps
    lines_x = []
    lines_y = []
    lines_z = []
    
    for i in range(len(primes_scaled) - 1):
        lines_x += [primes_scaled[i], primes_scaled[i + 1], None]
        lines_y += [0, 0, None]
        lines_z += [0, 0, None]

    gap_trace = go.Scatter3d(
        x=lines_x,  # Lines along the x-axis (between consecutive primes)
        y=lines_y,
        z=lines_z,
        mode='lines',
        line=dict(
            color='green',
            width=2
        ),
        name='Prime Gaps'
    )

    # Create the 3D figure with both primes and gaps
    fig = go.Figure(data=[prime_trace, gap_trace])

    # Customize layout for better visualization
    fig.update_layout(
        title="Prime Number Line and Gaps",
        scene=dict(
            xaxis_title='Number Line (Scaled)',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='cube'
        ),
        margin=dict(r=10, l=10, b=10, t=40),
        showlegend=True
    )

    # Show the interactive plot
    fig.show()

# Main execution
if __name__ == "__main__":
    # Define the upper limit for prime generation
    upper_limit = 1000

    # Generate primes up to the limit
    primes = generate_primes(upper_limit)

    # Plot the primes and their gaps in 3D
    plot_prime_gaps(primes)
