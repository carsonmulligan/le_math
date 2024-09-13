import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


# Define vertices of a tesseract in 4D space
def tesseract_vertices():
    vertices = []
    for i in range(16):
        vertex = [(i >> j) & 1 for j in range(4)]
        vertices.append(np.array(vertex) * 2 - 1)  # Scale and center the vertices
    return np.array(vertices)

def plot_rotating_tesseract():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    vertices = tesseract_vertices()

    # Rotating the tesseract
    def update(frame):
        ax.cla()
        # Rotate around the W-X plane (4D rotation)
        angle = frame * np.pi / 50
        rotation_matrix = np.array([[np.cos(angle), 0, 0, np.sin(angle)],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 0],
                                    [-np.sin(angle), 0, 0, np.cos(angle)]])
        rotated_vertices = np.dot(vertices, rotation_matrix)
        ax.scatter(rotated_vertices[:, 0], rotated_vertices[:, 1], rotated_vertices[:, 2])

        # Plot edges
        for i in range(16):
            for j in range(i+1, 16):
                if bin(i ^ j).count('1') == 1:
                    ax.plot([rotated_vertices[i, 0], rotated_vertices[j, 0]],
                            [rotated_vertices[i, 1], rotated_vertices[j, 1]],
                            [rotated_vertices[i, 2], rotated_vertices[j, 2]], color='b')
        
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])
    
    ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
    plt.show()

plot_rotating_tesseract()
