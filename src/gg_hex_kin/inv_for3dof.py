import numpy as np

class Inv3DOF:
    def __init__(self, a1, a2, a3, rnx, roy):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.rnxx = rnx
        self.rnyy = roy

    def solve(self, x, y, z):
        # Calculate theta1 and theta12
        the1 = 0.0
        the12 = 0.0

        if np.abs(x) < 0.00000000001:  # Check if x is close to zero
            if y > 0:
                x = 0.000000001
                y = y - x
            elif y < 0:
                x = 0.000000001
                y = y + x

            else:
                the1 = np.arctan2(self.rnyy,self.rnxx)
                the12 = -np.pi + the1 if the1 > 0 else np.pi + the1
        
        else:

            the1 = np.arctan2(y, x)
            the12 = -np.pi + the1 if the1 > 0 else np.pi + the1

        
            

        # Calculate ez and ew
        ez = z - self.a1
        ew = x / np.cos(the1)
        ew2 = x / np.cos(the12)

        # Calculate alpha
        cos_alp = (self.a2**2 + self.a3**2 - (ez**2 + ew**2)) / (2 * self.a2 * self.a3)
        if cos_alp > 1 or cos_alp < -1:
            raise ValueError("Position is out of reach for the given arm lengths.")
        
        alp = np.arccos(cos_alp)
        alp2 = 2 * np.pi - alp

        # Calculate theta3
        the3 = np.pi - alp
        the32 = np.pi - alp2

        # Calculate beta values
        beta1_1 = np.arctan2(self.a3 * np.sin(the3), self.a2 + self.a3 * np.cos(the3))
        beta2_1 = np.arctan2(self.a3 * np.sin(the32), self.a2 + self.a3 * np.cos(the32))

        # Calculate gamma
        gama11 = np.arctan2(ew, ez)
        gama21 = np.arctan2(ew2, ez)

        # Calculate theta2
        the211 = gama11 - beta1_1
        the212 = gama11 - beta2_1
        the221 = gama21 - beta2_1
        the222 = gama21 - beta1_1

        # Adjust the211
        if the211 > np.pi:
            the211 = the211 - 2 * np.pi
        elif the211 < -np.pi:
            the211 = the211 + 2 * np.pi

        # Adjust the212
        if the212 > np.pi:
            the212 = the212 - 2 * np.pi
        elif the212 < -np.pi:
            the212 = the212 + 2 * np.pi

        # Adjust the221
        if the221 > np.pi:
            the221 = the221 - 2 * np.pi
        elif the221 < -np.pi:
            the221 = the221 + 2 * np.pi

        # Adjust the222
        if the222 > np.pi:
            the222 = the222 - 2 * np.pi
        elif the222 < -np.pi:
            the222 = the222 + 2 * np.pi

        # Collect all solutions
        solutions = [
            (the1, the211, the3),
            (the1, the212, the32),
            (the12, the221, the32),
            (the12, the222, the3)
        ]

        # Convert angles to degrees for readability
        solutions_deg = [(np.degrees(t1), np.degrees(t2), np.degrees(t3)) for t1, t2, t3 in solutions]
        
        self.solutions_rad = solutions
        self.solutions_deg = solutions_deg

    def get_solutions_rad(self):
        return self.solutions_rad

    def get_solutions_deg(self):
        return self.solutions_deg
    

if __name__ == "__main__":
    # Example usage
    a1, a2, a3 = 1, 1, 1
    x, y, z = 0,2.99999, 1

    robot_arm = Inv3DOF(a1, a2, a3)
    robot_arm.solve(x, y, z)

    # Access solutions in radians
    solutions_rad = robot_arm.get_solutions_rad()
    print("Solutions in radians:")
    for i, (t1, t2, t3) in enumerate(solutions_rad):
        print(f"Solution {i+1}:")
        print(f"  the1: {t1:.2f} radians")
        print(f"  the2: {t2:.2f} radians")
        print(f"  the3: {t3:.2f} radians")
        print("\n")

    # Access solutions in degrees
    solutions_deg = robot_arm.get_solutions_deg()
    print("Solutions in degrees:")
    for i, (t1, t2, t3) in enumerate(solutions_deg):
        print(f"Solution {i+1}:")
        print(f"  the1: {t1:.2f} degrees")
        print(f"  the2: {t2:.2f} degrees")
        print(f"  the3: {t3:.2f} degrees")
        print("\n")
