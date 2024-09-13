"""
This Python visualization enables the exploration of different geometric structures on 3-manifolds, 
inspired by Perelman's solution to the Geometrization Conjecture. The conjecture, proven by Grigori Perelman, 
classifies all 3-manifolds into one of three main geometric types: hyperbolic, Euclidean, or spherical. 

The Ricci flow, introduced by Richard Hamilton and used by Perelman, plays a crucial role in the solution. 
The Ricci flow deforms the metric of a manifold over time, "smoothing out" irregularities in the manifold's 
geometry. Eventually, all 3-manifolds decompose into pieces that exhibit one of these three geometric structures.

    1. **Hyperbolic Geometry**: Negatively curved surfaces, often visualized as saddle-like spaces.
    2. **Euclidean Geometry**: Flat, uncurved spaces that follow the rules of traditional geometry.
    3. **Spherical Geometry**: Positively curved surfaces, such as the surface of a sphere.

Users can navigate between these geometries to gain insight into how they form the building blocks of 3-manifold 
topology and understand the role of Ricci flow in the Geometrization Conjecture.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import RadioButtons

# Functions to generate different geometric structures
def spherical_geometry():
    """
    Generate points on the surface of a sphere (spherical geometry).
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

def euclidean_geometry():
    """
    Generate a flat grid (euclidean geometry).
    """
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(x, y)
    z = np.zeros_like(x)  # Flat space has no curvature
    return x, y, z

def hyperbolic_geometry():
    """
    Generate points representing a saddle shape (hyperbolic geometry).
    """
    u = np.linspace(-2, 2, 100)
    v = np.linspace(-2, 2, 100)
    u, v = np.meshgrid(u, v)
    x = np.sinh(u)
    y = np.sinh(v)
    z = np.cosh(u) - np.cosh(v)
    return x, y, z

# Initialize 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])

# Default geometry: Euclidean
x, y, z = euclidean_geometry()
geometry_plot = ax.plot_surface(x, y, z, color='b', alpha=0.8)

# Set titles and labels
ax.set_title('Explore Geometries of 3-Manifolds')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Function to update the geometry based on user selection
def update_geometry(label):
    ax.cla()  # Clear current plot
    if label == 'Spherical':
        x, y, z = spherical_geometry()
        ax.plot_surface(x, y, z, color='r', alpha=0.8)
        ax.set_title('Spherical Geometry')
    elif label == 'Euclidean':
        x, y, z = euclidean_geometry()
        ax.plot_surface(x, y, z, color='b', alpha=0.8)
        ax.set_title('Euclidean Geometry')
    elif label == 'Hyperbolic':
        x, y, z = hyperbolic_geometry()
        ax.plot_surface(x, y, z, color='g', alpha=0.8)
        ax.set_title('Hyperbolic Geometry')
    
    # Reset labels and aspect ratio
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1,1,1])
    fig.canvas.draw_idle()

# Create radio buttons for user interaction
ax_radio = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor='lightgoldenrodyellow')
radio_buttons = RadioButtons(ax_radio, ('Spherical', 'Euclidean', 'Hyperbolic'))

# Link radio buttons to the update function
radio_buttons.on_clicked(update_geometry)

# Show plot with interactive elements
plt.show()
