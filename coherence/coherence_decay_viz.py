import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import ttest_ind

# Quantum coherence decay function
def coherence_decay(t, gamma):
    """ 
    Computes quantum coherence decay at time t given decoherence rate gamma.
    
    Arguments:
    t -- time (array-like or float)
    gamma -- decoherence rate (float)
    
    Returns:
    Quantum coherence P(t) = exp(-gamma * t)
    """
    return np.exp(-gamma * t)

# Generate coherence data across different biological environments
def generate_coherence_data(time_points, gamma_values):
    """
    Generates coherence data for different decoherence rates (biological environments).
    
    Arguments:
    time_points -- duration of the experiment (int)
    gamma_values -- list of decoherence rates (array-like)
    
    Returns:
    time, coherence data for each gamma value
    """
    time = np.linspace(0, time_points, 100)
    coherence_data = []
    
    for gamma in gamma_values:
        coherence = coherence_decay(time, gamma)
        coherence_data.append(coherence)
    
    return time, coherence_data

# 3D plot of quantum coherence across multiple environments
def plot_3d_coherence(time, gamma_values, coherence_data):
    """
    Plots the 3D visualization of quantum coherence decay in multiple biological environments.
    
    Arguments:
    time -- time array (array-like)
    gamma_values -- list of decoherence rates (array-like)
    coherence_data -- coherence data for each gamma value
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for i, gamma in enumerate(gamma_values):
        ax.plot(time, coherence_data[i], gamma * np.ones_like(time), label=f'gamma={gamma:.2f}')
    
    ax.set_xlabel('Time (t)')
    ax.set_ylabel('Coherence P(t)')
    ax.set_zlabel('Decoherence Rate (gamma)')
    ax.set_title('Quantum Coherence Decay in Biological Systems')
    ax.legend()
    plt.show()

# Perform t-test to compare quantum and classical systems
def perform_t_test(quantum_data, classical_data):
    """
    Performs a t-test to compare quantum and classical system coherence data.
    
    Arguments:
    quantum_data -- array of quantum system data
    classical_data -- array of classical system data
    
    Returns:
    t-statistic and p-value of the test
    """
    t_stat, p_value = ttest_ind(quantum_data, classical_data)
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")

# Simulating coherence decay in biological systems
time_points = 10  # Duration of the experiment
gamma_values = np.linspace(0.01, 0.2, 5)  # Range of gamma values for different environments

# Generate coherence data
time, coherence_data = generate_coherence_data(time_points, gamma_values)

# 3D Visualization of coherence decay
plot_3d_coherence(time, gamma_values, coherence_data)

# Example: Perform t-test between a quantum system (gamma=0.05) and classical system (gamma=0.15)
quantum_data = coherence_data[1]  # gamma=0.05
classical_data = coherence_data[4]  # gamma=0.15
perform_t_test(quantum_data, classical_data)
