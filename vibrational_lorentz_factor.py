# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
c = 3e8  # Speed of light in m/s
G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
mass_earth = 5.972e24  # Mass of the Earth in kg
initial_frequency = 1e14  # Initial vibrational frequency in Hz
num_objects = 1000  # Number of objects

# Generate random distances and velocities
distances_from_mass = np.random.rand(num_objects) * 1e7  # Random distances (in meters)
velocities = np.random.rand(num_objects) * c  # Random velocities (up to the speed of light)

# Create a DataFrame to hold the data
df = pd.DataFrame({
    'distance_from_mass': distances_from_mass,
    'velocity': velocities,
    'x': np.random.rand(num_objects) * 1e7,  # Random X coordinates
    'y': np.random.rand(num_objects) * 1e7,  # Random Y coordinates
    'z': np.random.rand(num_objects) * 1e7   # Random Z coordinates
})

# Step 2: Defining Vibrational Slowdown Functions
# We now define two functions to calculate the vibrational slowdown due to gravitational energy and velocity:

# Function to calculate vibrational slowdown due to gravity
def vibrational_slowdown_gravity(frequency, mass, distance):
    potential_energy = (G * mass) / distance
    return frequency / np.sqrt(1 + potential_energy / c**2)

# Function to calculate vibrational slowdown due to velocity
def vibrational_slowdown_velocity(frequency, velocity):
    return frequency / np.sqrt(1 + (velocity**2 / c**2))

# Apply these functions to the DataFrame
df['vibrational_slowdown_gravity'] = df['distance_from_mass'].apply(
    lambda d: vibrational_slowdown_gravity(initial_frequency, mass_earth, d)
)

df['vibrational_slowdown_velocity'] = df['velocity'].apply(
    lambda v: vibrational_slowdown_velocity(initial_frequency, v)
)


# Step 3: Visualization in 4D (Projected in 3D)
# We will now visualize the spatial dimensions (X, Y, Z) and use the vibrational slowdown due to gravity as the color dimension to represent the "fourth dimension."
# Create a 3D scatter plot where color represents vibrational slowdown
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract data for 3D plotting
x = df['x']
y = df['y']
z = df['z']
colors = df['vibrational_slowdown_gravity']  # Color representing vibrational slowdown

# Scatter plot in 3D with color scale
scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', marker='o')
plt.colorbar(scatter, label='Vibrational Slowdown (Hz)')

# Labels and title
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Position (m)')
plt.title("Vibrational Slowdown in 4D Space (Projected in 3D)")

plt.show()
