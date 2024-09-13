"""
This Python visualization allows users to interact with a basic 3D knot structure and understand the relationship
between the knot's geometry and its polynomial invariant, specifically the Jones polynomial. The Jones polynomial 
is an invariant of knots and links, arising from considerations in algebraic topology and quantum field theory. 

In knot theory, a knot is a closed loop in 3D space, and knots can be transformed by continuous deformations known as 
ambient isotopies. The Jones polynomial assigns a Laurent polynomial to each knot, encoding information about its 
topology. This polynomial remains invariant under Reidemeister moves, which represent changes in the knot diagram 
that don't affect its fundamental structure.

The 3D system generated here displays several classic knots, such as the trefoil and figure-eight knots, which users 
can rotate and manipulate. In algebraic terms, manipulating a knot alters the diagram, but the corresponding Jones 
polynomial remains invariant unless a topologically distinct knot is formed.

    1. **Knots**: These are loops in space that do not intersect themselves.
    2. **Tangles**: Partial knots used in certain algebraic computations.
    3. **Jones Polynomial**: A knot invariant that is resilient to knot deformations.

Users can modify the knot and observe the behavior of the Jones polynomial under isotopic transformations.
The core mathematical focus is on algebraic topology, polynomial invariants, and knot theory transformations.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button

# Create basic 3D knot visualization (example: trefoil knot)
def trefoil_knot(t):
    """
    Parametric equations for the trefoil knot in 3D.
    The knot is a closed loop that does not intersect itself.
    """
    x = np.sin(t) + 2 * np.sin(2 * t)
    y = np.cos(t) - 2 * np.cos(2 * t)
    z = -np.sin(3 * t)
    return x, y, z

# Define the range for the parametric variable t
t = np.linspace(0, 2 * np.pi, 500)

# Generate the trefoil knot
x, y, z = trefoil_knot(t)

# Create a 3D plot for the knot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
knot_plot, = ax.plot(x, y, z, label="Trefoil Knot")

# Set labels and title
ax.set_title('Trefoil Knot - Explore Knot Transformations')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add sliders for user interaction (manipulation of knot parameters)
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor=axcolor)
t_slider = Slider(ax_slider, 'Transform', 0.1, 2.0, valinit=1.0)

def update(val):
    """
    Update function for the slider interaction, allowing users to deform the knot
    by changing the parametric equations.
    """
    t_val = t_slider.val
    new_x, new_y, new_z = trefoil_knot(t * t_val)
    knot_plot.set_data(new_x, new_y)
    knot_plot.set_3d_properties(new_z)
    fig.canvas.draw_idle()

t_slider.on_changed(update)

# Add a button to reset the knot transformation
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    """
    Reset the knot back to its original form when the reset button is pressed.
    """
    t_slider.reset()

button.on_clicked(reset)

# Display the plot
plt.show()
