import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import numpy as np
from std_msgs.msg import Int16
import time


class Hex_Controller(Node):
    def __init__(self):
        super().__init__("Hex_Controller")
        self.minthe = -90
        self.maxthe = 91
        self.lstthe = list(range(self.minthe, self.maxthe))  
        
        # Lists for all possible values of x1, x2, y1, y2, z1, z2
        self.lstx1, self.lsty1, self.lstz1 = [], [], []
        self.lstx2, self.lsty2, self.lstz2 = [], [], []

        self.theta = 0  # theta in degrees, initially set to 0
        self.initial_z = 3   # Initial height difference in cm
        self.legspa = 6   # cm (leg span)

        # Convert theta to radians
        self.alp = np.deg2rad(self.theta)
        self.beta = np.deg2rad(90 - self.theta)
        self.gama = np.deg2rad(90)

        # Central position of trajectory
        self.x0, self.y0, self.z0 = 10, 0, 0

        # Calculate positions from x0 and leg span for each theta
        for j in self.lstthe:
            self.alp = np.deg2rad(j)
            self.beta = np.deg2rad(90 - j)

            x1 = self.x0 - ((self.legspa / 2) * np.cos(self.alp))
            y1 = self.y0 - ((self.legspa / 2) * np.cos(self.beta))
            z1 = self.z0 - ((self.legspa / 2) * np.cos(self.gama))

            self.lstx1.append(x1)
            self.lsty1.append(y1)
            self.lstz1.append(z1)

            x2 = self.x0 + ((self.legspa / 2) * np.cos(self.alp))
            y2 = self.y0 + ((self.legspa / 2) * np.cos(self.beta))
            z2 = self.z0 + ((self.legspa / 2) * np.cos(self.gama))

            self.lstx2.append(x2)
            self.lsty2.append(y2)
            self.lstz2.append(z2)

        # Leg starting coordinates
        self.x, self.y, self.z = self.lstx1.copy(), self.lsty1.copy(), self.lstz1.copy()

        # Timer for updating position
        self.time_period = 0.1
        self.timer1 = self.create_timer(self.time_period, self.timer1_callback)
        self.timer2 = self.create_timer(self.time_period, self.timer2_callback)

        self.timer1_time = 0
        self.timer1_iter = 100
        self.boolleg = 0
        self.boolreatched = False
        self.error = 0.3

        # Subscriptions
        self.boollegsub = self.create_subscription(
            Int16,
            'boolleg',
            self.boolleg_callback,
            10)

        self.legdir = self.create_subscription(
            Int16,
            'legdir',
            self.legdir_callback,
            10)

    def boolleg_callback(self, msg):
        self.boolleg = msg.data

    def legdir_callback(self, msg):
        self.theta = msg.data
        self.alp = np.deg2rad(self.theta)  # Update alp based on new theta
        self.beta = np.deg2rad(90 - self.theta)  # Update beta based on new theta

    def timer2_callback(self):
        pass

    def timer1_callback(self):
        for i in range(len(self.lstthe)):
            x1 = self.lstx1[i]
            y1 = self.lsty1[i]
            z1 = self.lstz1[i]
            x2 = self.lstx2[i]
            y2 = self.lsty2[i]
            z2 = self.lstz2[i]

            if x1 <= self.x[i] <= x2 and y1 <= self.y[i] <= y2 and self.boolleg == 0:
                self.x[i] += (self.legspa * np.cos(self.alp)) * (self.timer1_time / self.timer1_iter)
                self.y[i] += (self.legspa * np.cos(self.beta)) * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"Moving forward x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")

            elif abs(self.x[i] - x2) < self.error and abs(self.y[i] - y2) < self.error and self.boolleg == 0:
                if not self.boolreatched:
                    self.timer1_time = 0
                    print(f"Reached first endpoint x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")
                    self.boolreatched = True
                else:
                    self.z[i] -= (self.initial_z * (self.timer1_time / self.timer1_iter))
                    self.timer1_time += self.time_period
                    print(f"Moving downward x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")

            elif abs(self.x[i] - x2) < self.error and abs(self.y[i] - y2) < self.error and self.boolleg == 1:
                if self.boolreatched:
                    self.timer1_time = 0
                    print(f"Reached second endpoint x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")
                    self.boolreatched = False

            elif self.x[i] >= x1 and self.y[i] >= y1 and self.boolleg == 1:
                self.x[i] = x2 - (self.legspa * np.cos(self.alp)) * (self.timer1_time / self.timer1_iter)
                self.y[i] = y2 - (self.legspa * np.cos(self.beta)) * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"Moving backwards x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")

            elif abs(self.x[i] - x1) < self.error and abs(self.y[i] - y1) < self.error and self.boolleg == 1:
                if not self.boolreatched:
                    self.timer1_time = 0
                    print(f"Reached third endpoint x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")
                    self.boolreatched = True
                    self.boolleg = 0

            elif abs(self.x[i] - x1) < self.error and abs(self.y[i] - y1) < self.error and self.z[i] < z1:
                self.z[i] += self.initial_z * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"Moving upward x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")

            elif abs(self.x[i] - x1) < self.error and abs(self.y[i] - y1) < self.error and abs(self.z[i] - z1) < self.error:
                if self.boolreatched:
                    self.timer1_time = 0
                    print(f"Reached fourth endpoint x,y,z are {self.x[i]}, {self.y[i]}, {self.z[i]}")
                    self.boolreatched = False

def main():
    rclpy.init()
    node = Hex_Controller()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
