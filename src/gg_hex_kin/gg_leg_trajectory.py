import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the coefficient 'a' for the parametric parabola
a = 1.0  # Coefficient

# Define the new origin offsets (alpha, beta, gamma)
alpha = 2.0  # Offset in the x-direction
beta = 3.0   # Offset in the y-direction
gamma = 1.0  # Offset in the z-direction

# Define the range for the parameter t
t_values = np.linspace(-5, 5, 100)

# Calculate the corresponding y, z values using the parametric equations with offsets

y_values = 2 * a * t_values + gamma  # Negative sign for downward opening parabola
z_values = -a * t_values**2 + beta

# Set x to a constant value (alpha) since the parabola is parallel to the zy plane
x_values =  y_values* np.cos(np.pi/8)

# Plot the parametric parabola in 3D space
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the parametric curve with moved origin
ax.plot(x_values, y_values, z_values, label=r'Parametric Parabola with Origin at $(\alpha, \beta, \gamma)$', color='b')

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Parametric Parabola $z^2 = -4ay$ Parallel to ZY Plane with Shifted Origin')
ax.legend()

plt.show()
