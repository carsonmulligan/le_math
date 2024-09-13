import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define vertices of a tesseract in 4D space
def tesseract_vertices():
    vertices = []
    for i in range(16):
        vertex = [(i >> j) & 1 for j in range(4)]
        vertices.append(np.array(vertex) * 2 - 1)  # Scale and center the vertices
    return np.array(vertices)

# Function to plot the edges of the tesseract projected into 3D
def plot_tesseract():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Tesseract vertices
    vertices = tesseract_vertices()

    # 4D to 3D projection by dropping one dimension (W)
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    # Edges of the tesseract (connect vertices that differ by one bit)
    for i in range(16):
        for j in range(i+1, 16):
            if bin(i ^ j).count('1') == 1:  # Hamming distance of 1
                ax.plot([vertices[i, 0], vertices[j, 0]],
                        [vertices[i, 1], vertices[j, 1]],
                        [vertices[i, 2], vertices[j, 2]], color='b')

    ax.set_title('3D Projection of a Tesseract (4D Hypercube)')
    plt.show()

# Visualize the 4D tesseract projected into 3D
plot_tesseract()
