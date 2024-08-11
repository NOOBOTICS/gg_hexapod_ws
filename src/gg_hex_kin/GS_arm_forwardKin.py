import numpy as np


class forwardkin():
    def __init__(self):
        the1, the2, the3, the4= self.get_input_angles()
        point = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
        
        #lenght of each limb of arm
        a1 = 1
        a2 = 1
        a3 = 1
        a4 = 1
        

        
        rta0 = self.rtf(0, 0, the1)  # rotation along z-axis by the1 degrees
        self.t1 = rta0@point

        tta0 = self.ttf(0, 0, a1)     # translation along z-axis by 1
        rto0 = self.rtf(0, -90, 0)   # rotation along y-axis by -90 degrees
        rtox = self.rtf(-90, 0, 0)   # rotation along x-axis by -90 degrees
        rta1 = self.rtf(0, 0, the2)  # rotation along z-axis by the2 degrees
        self.t2 = rta0 @ tta0 @rto0 @ rtox @ rta1 @point

        ttn0 = self.ttf(a2, 0, 0)     # translation along x-axis by 1
        rta2 = self.rtf(0, 0, the3)  # rotation along z-axis by the3 degrees
        self.t3 = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ ttn0 @ rta2 @ point


        ttn1 = self.ttf(a3, 0, 0)     # translation along x-axis by 1
        rta3 = self.rtf(0, 0, the4)  # rotation along z-axis by the4 degrees
        self.t4 = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ ttn0 @ rta2 @ ttn1  @ rta3 @ point


        ttn2 = self.ttf(a4,0, 0 )     # translation along z-axis by 1
        rto2 = self.rtf(0, 90, 0)   # rotation along y-axis by -90 degrees
        rta4 = self.rtf(0, 0, 90)   # rotation along y-axis by -90 degrees
        self.t5 = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ ttn0 @ rta2 @ ttn1  @ rta3 @ ttn2 @ rto2 @ rta4 @ point




        # ttn3 = self.ttf(a5, 0, 0)     # translation along x-axis by 1
        # rto3 = self.rtf(0, 90, 0)    # rotation along y-axis by 90 degrees
        # rta5 = self.rtf(0, 0, 90)    # rotation along z-axis by 90 degrees
        # self.t6 = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ ttn0 @ rta2 @ ttn1 @ rto1 @ rta3 @ ttn2 @ rto2 @ rta4 @ ttn3 @ rto3 @ rta5 @ point

        # # Final transformation
        # final_transformation = rta0 @ tta0 @ rto0 @ rtox @ rta1 @ ttn0 @ rta2 @ ttn1 @ rto1 @ rta3 @ ttn2 @ rto2 @ rta4 @ ttn3 @ rto3 @ rta5 @ point

        # # Round small values to zero
        # final_transformation[np.abs(final_transformation) < 1e-10] = 0

        # self.trans = final_transformation
            

    def rtf(self,n, o, a):
        # Convert degrees to radians
        n = np.radians(n)
        o = np.radians(o)
        a = np.radians(a)
        
        # Rotation matrix around x-axis
        Rx = np.array([[1, 0, 0, 0],
                    [0, np.cos(n), -np.sin(n), 0],
                    [0, np.sin(n), np.cos(n), 0],
                    [0, 0, 0, 1]])

        # Rotation matrix around y-axis
        Ry = np.array([[np.cos(o), 0, np.sin(o), 0],
                    [0, 1, 0, 0],
                    [-np.sin(o), 0, np.cos(o), 0],
                    [0, 0, 0, 1]])

        # Rotation matrix around z-axis
        Rz = np.array([[np.cos(a), -np.sin(a), 0, 0],
                    [np.sin(a), np.cos(a), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

        # Combine transformations
        B = Rx @ Ry @ Rz
        return B

    def ttf(self,n, o, a):
        # Translation matrix
        Tx = np.array([[1, 0, 0, n],
                    [0, 1, 0, o],
                    [0, 0, 1, a],
                    [0, 0, 0, 1]])
        return Tx

    # Function to get input angles from the user
    def get_input_angles(self):
        the1 = float(input("Enter angle the1 in degrees: "))
        the2 = float(input("Enter angle the2 in degrees: "))
        the3 = float(input("Enter angle the3 in degrees: "))
        the4 = float(input("Enter angle the4 in degrees: "))
        return the1, the2, the3, the4

    # # Get the angles from the user
    # the1, the2, the3, the4, the5 = get_input_angles()

    # Define the point\

if __name__ == "__main__":
    a = forwardkin()
    print(a.t5)
    
