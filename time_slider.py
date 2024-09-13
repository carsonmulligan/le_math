import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
initial_frequency = 1e14  # Initial vibrational frequency in Hz
expansion_rate = 0.02  # Rate of expansion (arbitrary units for simulation)

# Create data for the "universe" (random points in space)
num_points = 1000
x = np.random.rand(num_points) * 100  # Initial positions in X
y = np.random.rand(num_points) * 100  # Initial positions in Y
z = np.random.rand(num_points) * 100  # Initial positions in Z
frequencies = initial_frequency * np.ones(num_points)  # Uniform initial frequency

# Function to update positions based on expansion factor
def update_positions(expansion_factor):
    return x * expansion_factor, y * expansion_factor, z * expansion_factor

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=frequencies, cmap='plasma', marker='o')
plt.colorbar(scatter, label='Vibrational Frequency (Hz)')

# Slider for Time (Expanding Universe)
ax_time = plt.axes([0.25, 0.02, 0.65, 0.03])
time_slider = Slider(ax_time, 'Time', 0.1, 10, valinit=1, valstep=0.1)

# Update function for the slider
def update(val):
    expansion_factor = time_slider.val
    x_new, y_new, z_new = update_positions(expansion_factor)
    scatter._offsets3d = (x_new, y_new, z_new)
    fig.canvas.draw_idle()

# Link slider to update function
time_slider.on_changed(update)

plt.show()
