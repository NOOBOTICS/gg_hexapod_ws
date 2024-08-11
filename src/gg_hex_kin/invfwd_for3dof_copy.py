import numpy as np


# copy dosent has point multiplied to the transformations


class Forwardkin:
    def __init__(self, ang1, ang2, ang3, a1, a2, a3):
        # Define angles and link lengths
        self.the1, self.the2, self.the3 = ang1, ang2, ang3
        self.a1, self.a2, self.a3 = a1, a2, a3
        
        # Define the initial point (identity matrix)
        point = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        
        # Calculate transformations
        rta0 = self.rtf(0, 0, self.the1)
        self.t1 = rta0 @ point

        tta0 = self.ttf(0, 0, self.a1)
        rto0 = self.rtf(0, -90, 0)
        rtox = self.rtf(-90, 0, 0)
        rta1 = self.rtf(0, 0, self.the2)
        self.t2 = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ point

        ttn0 = self.ttf(self.a2, 0, 0)
        rta2 = self.rtf(0, 0, self.the3)
        self.t3 = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ ttn0 @ rta2 @ point

        ttn1 = self.ttf(self.a3, 0, 0)
        # rto2 = self.rtf(0, 90, 0)
        self.t4 = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ ttn0 @ rta2 @ ttn1

    def rtf(self, n, o, a):
        # Convert degrees to radians
        n, o, a = np.radians(n), np.radians(o), np.radians(a)
        
        # Rotation matrices
        Rx = np.array([[1, 0, 0, 0],
                       [0, np.cos(n), -np.sin(n), 0],
                       [0, np.sin(n), np.cos(n), 0],
                       [0, 0, 0, 1]])

        Ry = np.array([[np.cos(o), 0, np.sin(o), 0],
                       [0, 1, 0, 0],
                       [-np.sin(o), 0, np.cos(o), 0],
                       [0, 0, 0, 1]])

        Rz = np.array([[np.cos(a), -np.sin(a), 0, 0],
                       [np.sin(a), np.cos(a), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

        # Combined rotation matrix
        return Rx @ Ry @ Rz

    def ttf(self, n, o, a):
        # Translation matrix
        return np.array([[1, 0, 0, n],
                         [0, 1, 0, o],
                         [0, 0, 1, a],
                         [0, 0, 0, 1]])

if __name__ == "__main__":
    # Example usage
    a = Forwardkin(30, 40, 50, 1, 1, 1)
    print("Transformation matrix t4:")
    print(a.t4)
