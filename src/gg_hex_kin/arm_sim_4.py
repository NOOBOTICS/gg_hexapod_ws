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

# Create a new figure with 4 subplots
fig = plt.figure(figsize=(15, 12))

# Add four 3D subplots (2 rows, 2 columns)
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')

# Get the forward kinematics for four different sets
print("Enter values for plot 1 \n")
a = forwardkin()
print("\n")
print("Enter values for plot 2 \n")
b = forwardkin()
print("\n")
print("Enter values for plot 3 \n")
c = forwardkin()
print("\n")
print("Enter values for plot 4 \n")
d = forwardkin()
print("\n")

# Define 4x4 transformation matrices for each set
T1 = a.t1
T2 = a.t2
T3 = a.t3
T4 = a.t4
T5 = a.t5
T6 = a.t6

K1 = b.t1
K2 = b.t2
K3 = b.t3
K4 = b.t4
K5 = b.t5
K6 = b.t6

L1 = c.t1
L2 = c.t2
L3 = c.t3
L4 = c.t4
L5 = c.t5
L6 = c.t6

M1 = d.t1
M2 = d.t2
M3 = d.t3
M4 = d.t4
M5 = d.t5
M6 = d.t6

# Set precision for printing
np.set_printoptions(precision=10, suppress=True)

# Print matrices
print("T6 from first set:")
print(T6)
print("T6 from second set:")
print(K6)
print("T6 from third set:")
print(L6)
print("T6 from fourth set:")
print(M6)

# List of transformation matrices for each subplot
transformations1 = [T1, T2, T3, T4, T5, T6]
transformations2 = [K1, K2, K3, K4, K5, K6]
transformations3 = [L1, L2, L3, L4, L5, L6]
transformations4 = [M1, M2, M3, M4, M5, M6]

# Plot the transformations on each subplot
for T in transformations1:  # First subplot
    plot_frame(ax1, T)
for T in transformations2:  # Second subplot
    plot_frame(ax2, T)
for T in transformations3:  # Third subplot
    plot_frame(ax3, T)
for T in transformations4:  # Fourth subplot
    plot_frame(ax4, T)

# Extract origins for each subplot
origins1 = np.array([T[:3, 3] for T in transformations1])
origins2 = np.array([T[:3, 3] for T in transformations2])
origins3 = np.array([T[:3, 3] for T in transformations3])
origins4 = np.array([T[:3, 3] for T in transformations4])

# Plot lines connecting the origins for each subplot
ax1.plot(origins1[:, 0], origins1[:, 1], origins1[:, 2], color='k')
ax2.plot(origins2[:, 0], origins2[:, 1], origins2[:, 2], color='k')
ax3.plot(origins3[:, 0], origins3[:, 1], origins3[:, 2], color='k')
ax4.plot(origins4[:, 0], origins4[:, 1], origins4[:, 2], color='k')

# Set labels for each subplot
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
ax2.set_zlabel('Z axis')
ax3.set_xlabel('X axis')
ax3.set_ylabel('Y axis')
ax3.set_zlabel('Z axis')
ax4.set_xlabel('X axis')
ax4.set_ylabel('Y axis')
ax4.set_zlabel('Z axis')

# Set the limits of the plots
ax1.set_xlim([-3, 3])
ax1.set_ylim([-3, 3])
ax1.set_zlim([0, 6])
ax2.set_xlim([-3, 3])
ax2.set_ylim([-3, 3])
ax2.set_zlim([0, 6])
ax3.set_xlim([-3, 3])
ax3.set_ylim([-3, 3])
ax3.set_zlim([0, 6])
ax4.set_xlim([-3, 3])
ax4.set_ylim([-3, 3])
ax4.set_zlim([0, 6])

# Add titles to the subplots
ax1.set_title('Transformation Matrices Set 1')
ax2.set_title('Transformation Matrices Set 2')
ax3.set_title('Transformation Matrices Set 3')
ax4.set_title('Transformation Matrices Set 4')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
