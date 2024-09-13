import mpmath
import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the zeta function
def zeta_function(s):
    return mpmath.zeta(s)

# Define a function to evaluate if zeros are on the critical line
def is_on_critical_line(zero):
    return np.isclose(zero.real, 0.5)

# Evaluate the zeta function on the critical line
critical_line_values = []
for t in np.linspace(0, 50, 1000):  # Imaginary part varies
    s = 0.5 + 1j * t  # s = 0.5 + it
    zeta_val = zeta_function(s)
    critical_line_values.append(zeta_val)

# Visualize the magnitude of the zeta function on the critical line
plt.plot(np.linspace(0, 50, 1000), [abs(val) for val in critical_line_values])
plt.title("Magnitude of the Riemann Zeta Function on the Critical Line")
plt.xlabel("Imaginary part t")
plt.ylabel("|ζ(0.5 + it)|")
plt.show()
