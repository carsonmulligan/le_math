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
