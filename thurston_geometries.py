import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mayavi import mlab

# Function to visualize Euclidean space (a 3D grid)
def plot_euclidean_space():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a grid in Euclidean space
    x = np.linspace(-1, 1, 10)
    y = np.linspace(-1, 1, 10)
    z = np.linspace(-1, 1, 10)

    for i in x:
        for j in y:
            for k in z:
                ax.scatter(i, j, k, color='b')

    ax.set_title('Euclidean Space (Flat)')
    plt.show()

# Function to visualize Spherical Geometry (a sphere in 3D)
def plot_spherical_geometry():
    phi, theta = np.mgrid[0:np.pi:100j, 0:2*np.pi:100j]
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='r', alpha=0.6)

    ax.set_title('Spherical Geometry')
    plt.show()

# Function to visualize Hyperbolic Geometry (a hyperbolic paraboloid)
def plot_hyperbolic_geometry():
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(x, y)
    z = x**2 - y**2  # Equation of hyperbolic paraboloid

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='g', alpha=0.6)

    ax.set_title('Hyperbolic Geometry')
    plt.show()

# Main function to visualize Thurston geometries
def visualize_thurston_geometries():
    print("Visualizing Euclidean, Spherical, and Hyperbolic geometries...")
    plot_euclidean_space()
    plot_spherical_geometry()
    plot_hyperbolic_geometry()

# Run the visualization
visualize_thurston_geometries()
