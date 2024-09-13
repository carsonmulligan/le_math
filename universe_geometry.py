"""
This Python visualization simulates the evolution of the universe's geometry following the Big Bang, allowing 
users to manipulate key cosmological parameters such as energy, dark matter, and curvature. The expansion of 
the universe can be understood through the Friedmann equations, which govern how different densities of matter, 
radiation, and dark energy influence the curvature of spacetime and the rate at which the universe expands.

The three major components involved are:
    1. **Energy Density (Ω_m)**: The density of ordinary matter and radiation that drives the gravitational collapse 
       of the universe, contributing to its deceleration.
    2. **Dark Matter (Ω_dm)**: An invisible form of matter that interacts through gravity but not with electromagnetic 
       forces, contributing to the gravitational pull without being detected directly.
    3. **Curvature (Ω_k)**: The geometric structure of the universe, which can be open, closed, or flat. This is influenced 
       by the total energy density of the universe compared to the critical density.

The evolution of these parameters over time determines whether the universe will continue expanding indefinitely, 
re-collapse, or reach a steady state. By using sliders to manipulate these variables, users can visualize how different 
cosmological models (open, closed, or flat universes) evolve.

    1. **Friedmann Equations**: Governs the dynamics of the universe's expansion rate in terms of energy densities.
    2. **Curvature**: Determines whether the universe is positively curved (closed), flat, or negatively curved (open).
    3. **Cosmological Constant**: Represents dark energy and its effect on the acceleration of the universe's expansion.

The visualization provides a 4D slider system to explore how these parameters affect the universe's geometry and expansion.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Function to simulate universe expansion based on energy density, dark matter, and curvature
def universe_expansion(time, omega_m, omega_dm, omega_k):
    """
    Simulates the scale factor of the universe (a(t)) over time using a simplified model
    based on energy density (Ω_m), dark matter (Ω_dm), and curvature (Ω_k).
    """
    H0 = 70  # Hubble constant at present time (in km/s/Mpc)
    omega_lambda = 1 - omega_m - omega_dm - omega_k  # Cosmological constant (dark energy)
    
    # Friedmann equation to compute the scale factor a(t) as a function of time and the energy parameters
    scale_factor = np.sqrt(omega_m * (1 + time)**3 + omega_dm * (1 + time)**2 + omega_lambda + omega_k * (1 + time)**-2)
    return scale_factor

# Time range: from Big Bang to present (normalized, 0 is Big Bang, 1 is now)
time = np.linspace(0, 1, 500)

# Initial parameters for omega_m, omega_dm, and omega_k
initial_omega_m = 0.3
initial_omega_dm = 0.25
initial_omega_k = 0.05

# Simulate the initial expansion
scale_factor = universe_expansion(time, initial_omega_m, initial_omega_dm, initial_omega_k)

# Create a 3D plot to visualize the expansion of the universe's geometry over time
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot, = ax.plot(time, scale_factor, time * 0, label="Universe Expansion")

# Labels and titles
ax.set_title("Universe Geometry Evolution - Post Big Bang")
ax.set_xlabel('Time (normalized)')
ax.set_ylabel('Scale Factor (a(t))')
ax.set_zlabel('Expansion Geometry')

# Create sliders to manipulate the parameters (Ω_m, Ω_dm, Ω_k)
axcolor = 'lightgoldenrodyellow'
ax_omega_m = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_omega_dm = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_omega_k = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

# Slider initialization
omega_m_slider = Slider(ax_omega_m, 'Omega_m (Energy)', 0.0, 1.0, valinit=initial_omega_m)
omega_dm_slider = Slider(ax_omega_dm, 'Omega_dm (Dark Matter)', 0.0, 1.0, valinit=initial_omega_dm)
omega_k_slider = Slider(ax_omega_k, 'Omega_k (Curvature)', -1.0, 1.0, valinit=initial_omega_k)

# Update function for the sliders
def update(val):
    omega_m_val = omega_m_slider.val
    omega_dm_val = omega_dm_slider.val
    omega_k_val = omega_k_slider.val
    
    # Recompute the scale factor based on the updated parameters
    new_scale_factor = universe_expansion(time, omega_m_val, omega_dm_val, omega_k_val)
    
    # Update the plot with the new scale factor
    plot.set_ydata(new_scale_factor)
    plot.set_3d_properties(time * 0)  # Z-axis stays 0 to represent flat expansion plane
    fig.canvas.draw_idle()

# Connect the sliders to the update function
omega_m_slider.on_changed(update)
omega_dm_slider.on_changed(update)
omega_k_slider.on_changed(update)

# Display the plot
plt.show()
