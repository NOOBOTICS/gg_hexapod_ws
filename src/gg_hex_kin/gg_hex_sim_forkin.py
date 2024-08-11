import matplotlib.pyplot as plt
import numpy as np
from GS_arm_forwardKin import forwardkin

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

# Create a new figure for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
a = forwardkin()

# Define 4x4 transformation matrices
T1 = a.t1
T2 = a.t2
T3 = a.t3
T4 = a.t4
T5 = a.t5

# Set precision for printing
np.set_printoptions(precision=10, suppress=True)

# Print matrices
# print("T4:")
# print(T4)
# print("T5:")
# Print matrix T5 with integer elements
for row in T5:
    print(" ".join(f"{element}" for element in row))


# List of transformation matrices
transformations = [T1, T2, T3, T4, T5]

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
