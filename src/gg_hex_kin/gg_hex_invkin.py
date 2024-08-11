import numpy as np
from inv_for3dof import Inv3DOF
from invfwd_for3dof_copy import Forwardkin
import GS_arm_forwardKin_copy

def round_small_values(matrix, threshold=1e-10):
    """Round small values in a matrix to zero."""
    matrix[np.abs(matrix) < threshold] = 0
    return matrix

# Length from wrist to end effector
a1 = 1
a2 = 1
a3 = 1
a4 = 1  

point = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

# Taking a 4x4 matrix as input
matrix = []
print("Enter the end effector transformation frame (4x4 matrix row-wise):")

for i in range(4):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert the list of lists into a numpy array
end_frame = np.array(matrix)

# Apply the rounding function
end_frame = round_small_values(end_frame)

# Extracting the position vector O5 and rotation matrix R5
O5 = end_frame[:3, 3].reshape((3, 1))
R5 = end_frame[:3, :3]

# Defining the unit vector along the z-axis
zorin = np.array([[0], [0], [1]])

# Calculating the wrist position
xyz_wrist = O5 - (a4 * (R5 @ zorin))  # Changed from a4 to a5

# Printing the results with better formatting
np.set_printoptions(suppress=True, precision=10)

print("end_frame is ")
print(end_frame)
print("O5 (Position Vector):")
print(O5)
print("R5 (Rotation Matrix):")
print(R5)
print("Wrist Position (xyz_wrist):")
print(xyz_wrist)

wrist = Inv3DOF(a1, a2, a3, R5[0][0], R5[1][0]) 
wrist.solve(xyz_wrist[0][0], xyz_wrist[1][0], xyz_wrist[2][0])
wrist_frame_angles = wrist.solutions_deg

# print(wrist_frame_angles)
(ang11, ang21, ang31) = wrist_frame_angles[0]
(ang12, ang22, ang32) = wrist_frame_angles[1]
(ang13, ang23, ang33) = wrist_frame_angles[2]
(ang14, ang24, ang34) = wrist_frame_angles[3]

wrist_frame1 = Forwardkin(ang11, ang21, ang31, a1, a2, a3)
wrist_frame2 = Forwardkin(ang12, ang22, ang32, a1, a2, a3)
wrist_frame3 = Forwardkin(ang13, ang23, ang33, a1, a2, a3)
wrist_frame4 = Forwardkin(ang14, ang24, ang34, a1, a2, a3)

print(f"wrist frame1: \n{wrist_frame1.t4@ point}")
print(f"wrist frame2: \n{wrist_frame2.t4@ point}")
print(f"wrist frame3: \n{wrist_frame3.t4@ point}")
print(f"wrist frame4: \n{wrist_frame4.t4@ point}")



end_frame_orie = end_frame[:3, :3]


transformation1 = (wrist_frame1.t4.T[:3, :3]) @ end_frame_orie
transformation2 = (wrist_frame2.t4.T[:3, :3]) @ end_frame_orie

transformation3 = (wrist_frame3.t4.T[:3, :3]) @ end_frame_orie
transformation4 = (wrist_frame4.t4.T[:3, :3]) @ end_frame_orie

# print("Transformation 1:")
# print(transformation1)


# the41 = np.arctan2(transformation1[1][1],transformation1[0][1])
# the42 = np.arctan2(transformation2[1][1],transformation2[0][1])

# the43 = np.arctan2(transformation3[1][1],transformation3[0][1])
# the44 = np.arctan2(transformation4[1][1],transformation4[0][1])

# if the41 > 0:
#     the41 = -np.pi + the41
# else:
#     the41 = np.pi +the41

# if the42 > 0:
#     the42 = -np.pi + the42
# else:
#     the42 = np.pi +the42

# #///////////////////////////////////////////////////////

# if the43 > 0:
#     the43 = -np.pi + the43
# else:
#     the43 = np.pi +the43

# if the44 > 0:
#     the44 = -np.pi + the44
# else:
#     the44 = np.pi +the44

the41 = np.arctan2(transformation1[1][2],transformation1[1][0])
the42 = np.arctan2(transformation1[1][2],transformation1[1][0])

the43 = np.arctan2(transformation1[1][2],transformation1[1][0])
the44 = np.arctan2(transformation1[1][2],transformation1[1][0])

print("\n")

print("First Solution is: ")
print(wrist_frame_angles[0][0])
print(wrist_frame_angles[0][1])
print(wrist_frame_angles[0][2])
print(np.degrees(the41))
# print(np.degrees(the51))
print("\n")
c = GS_arm_forwardKin_copy.forwardkin(wrist_frame_angles[0][0],wrist_frame_angles[0][1],wrist_frame_angles[0][2],np.degrees(the41))
for row in c.t5:
    print(" ".join(f"{element}" for element in row))
print("\n")



# Only the first solution is possible the rest are not !









# print("Second Solution is: ")
# print(wrist_frame_angles[1][0])
# print(wrist_frame_angles[1][1])
# print(wrist_frame_angles[1][2])
# print(np.degrees(the42))
# # print(np.degrees(the52))
# print("\n")
# c = GS_arm_forwardKin_copy.forwardkin(wrist_frame_angles[1][0],wrist_frame_angles[1][1],wrist_frame_angles[1][2],np.degrees(the42))
# for row in c.t5:
#     print(" ".join(f"{element}" for element in row))
# print("\n")

# print("Third Solution is: ")
# print(wrist_frame_angles[2][0])
# print(wrist_frame_angles[2][1])
# print(wrist_frame_angles[2][2])
# print(np.degrees(the43))
# # print(np.degrees(the53))
# print("\n")
# c = GS_arm_forwardKin_copy.forwardkin(wrist_frame_angles[2][0],wrist_frame_angles[2][1],wrist_frame_angles[2][2],np.degrees(the43))
# for row in c.t5:
#     print(" ".join(f"{element}" for element in row))
# print("\n")

# print("Fourth Solution is: ")
# print(wrist_frame_angles[3][0])
# print(wrist_frame_angles[3][1])
# print(wrist_frame_angles[3][2])
# print(np.degrees(the44))
# # print(np.degrees(the54))
# print("\n")
# c = GS_arm_forwardKin_copy.forwardkin(wrist_frame_angles[3][0],wrist_frame_angles[3][1],wrist_frame_angles[3][2],np.degrees(the44))
# for row in c.t5:
#     print(" ".join(f"{element}" for element in row))
# print("\n")

