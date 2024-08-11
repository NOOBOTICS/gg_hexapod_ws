import matplotlib.pyplot as plt
import numpy as np
from invfwd_for3dof import Forwardkin

def plot_frame(ax, T, length=0.5):
    """Plot a 3D frame given a 4x4 transformation matrix."""
    origin = T[:3, 3]
    x_vec = T[:3, 0]
    y_vec = T[:3, 1]
    z_vec = T[:3, 2]

    ax.quiver(origin[0], origin[1], origin[2],
              x_vec[0], x_vec[1], x_vec[2], color='r', length=length, normalize=True)
    ax.quiver(origin[0], origin[1], origin[2],
              y_vec[0], y_vec[1], y_vec[2], color='g', length=length, normalize=True)
    ax.quiver(origin[0], origin[1], origin[2],
              z_vec[0], z_vec[1], z_vec[2], color='b', length=length, normalize=True)

def round_small_values(matrix, threshold=1e-10):
    """Round small values in a matrix to zero."""
    matrix[np.abs(matrix) < threshold] = 0
    return matrix

# Create a new figure for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#//////////////////////////////////////////////////
a1 = 1 
a2 = 1 
a3 = 1 
the1 = 0

the2 = 0
the3 = 0

#41.989999725548806, -13.330000138756613, 120.00000009485251
a = Forwardkin(the1, the2, the3, a1, a2,a3)

# Define 4x4 transformation matrices and round small values to zero 
T1 = round_small_values(a.t1)
T2 = round_small_values(a.t2)
T3 = round_small_values(a.t3)
T4 = round_small_values(a.t4)

print(T4)

transformations = [T1, T2, T3, T4]

for T in transformations:
    plot_frame(ax, T)

# Extract origins
origins = np.array([T[:3, 3] for T in transformations])

# Plot lines connecting the origins
ax.plot(origins[:, 0], origins[:, 1], origins[:, 2], color='k')

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Set the limits of the plot
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([0, 6])

# Show the plot
plt.show()
