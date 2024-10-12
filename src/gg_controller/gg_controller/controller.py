import rclpy
from rclpy.node import Node                                                                                                                                                                                        
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import numpy as np
from std_msgs.msg import Int16
import time


class Hex_Controller(Node):
    def __init__(self):
        super().__init__("Hex_Controller")
        self.theta = 40  # in degrees
        self.initial_z = 3   # initial height difference in cm
        self.legspa = 6   # cm (leg span)

        # Convert theta to radians
        self.alp = np.deg2rad(self.theta)
        self.beta = np.deg2rad(90 - self.theta)
        self.gama = np.deg2rad(90)

        # Central position of trajectory
        self.x0 = 10
        self.y0 = 0
        self.z0 = 0

        # Calculate positions from x0 and leg span
        self.x1 = self.x0 - ((self.legspa / 2) * np.cos(self.alp))    
        self.y1 = self.y0 - ((self.legspa / 2) * np.cos(self.beta))  
        self.z1 = self.z0 - ((self.legspa / 2) * np.cos(self.gama))  

        print(f"x1, y1, z1: {self.x1}, {self.y1}, {self.z1}")

        self.x2 = self.x0 + ((self.legspa / 2) * np.cos(self.alp))
        self.y2 = self.y0 + ((self.legspa / 2) * np.cos(self.beta))  
        self.z2 = self.z0 + ((self.legspa / 2) * np.cos(self.gama))  

        print(f"x2, y2, z2: {self.x2}, {self.y2}, {self.z2}")

        # Leg starting coordinates
        self.x = self.x1
        self.y = self.y1
        self.z = self.z1

        # Timer for updating position
        self.time_period = 0.1
        self.timer1 = self.create_timer(self.time_period, self.timer1_callback)
        self.timer1_time = 0
        self.timer1_iter = 100
        self.boolleg = 0
        self.boolreatched = False

        self.boollegsub = self.create_subscription(
            Int16,
            'boolleg',
            self.boolleg_callback,
            10)

    def boolleg_callback(self, msg):
        self.boolleg = msg.data


    def timer1_callback(self):
        print(self.boolleg)
        print(f"current x,y,z are {self.x}, {self.y}, {self.z}")
        if self.x1 <= self.x <= self.x2 and self.y1 <= self.y <= self.y2 and self.boolleg == 0:
            self.x = self.x + (self.legspa * np.cos(self.alp)) * (self.timer1_time / self.timer1_iter)
            self.y = self.y + (self.legspa * np.cos(self.beta)) * (self.timer1_time / self.timer1_iter)
            self.timer1_time += self.time_period                    # for real time time, can be multiplied and divided accouring to our needs
            print(f"moving forward x,y,z are {self.x}, {self.y}, {self.z}")

        elif abs(self.x - self.x2) < 0.3 and abs(self.y - self.y2) < 0.3 and self.boolleg == 0 :
            if not self.boolreatched:
                self.timer1_time = 0
                print(f"reatched first endpoint x,y,z are {self.x}, {self.y}, {self.z}")
                self.boolreatched = True

            else:
                self.z -= (self.initial_z * (self.timer1_time / self.timer1_iter))
                self.timer1_time += self.time_period
                print(f"moving downward x,y,z are {self.x}, {self.y}, {self.z}")

       

        elif abs(self.x - self.x2) < 0.3 and abs(self.y - self.y2) < 0.3 and self.boolleg == 1 :
            if self.boolreatched :
                self.timer1_time = 0
                print(f"reatched second endpoint x,y,z are {self.x}, {self.y}, {self.z}")
                self.boolreatched = False

            elif self.x >= self.x1 and self.y >= self.y1 and self.boolleg == 1:
                self.x = self.x2 - (self.legspa * np.cos(self.alp)) * (self.timer1_time / self.timer1_iter)
                self.y = self.y2 - (self.legspa * np.cos(self.beta)) * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"moving backwards x,y,z are {self.x}, {self.y}, {self.z}")

        elif self.x >= self.x1 and self.y >= self.y1 and self.boolleg == 1:
            self.x = self.x2 - (self.legspa * np.cos(self.alp)) * (self.timer1_time / self.timer1_iter)
            self.y = self.y2 - (self.legspa * np.cos(self.beta)) * (self.timer1_time / self.timer1_iter)
            self.timer1_time += self.time_period
            print(f"moving backwards x,y,z are {self.x}, {self.y}, {self.z}")

        elif abs(self.x - self.x1) < 0.3 and abs(self.y - self.y1) < 0.3 and self.boolleg == 1:
            if not self.boolreatched:
                self.timer1_time = 0
                print(f"reatched third endpoint x,y,z are {self.x}, {self.y}, {self.z}")
                self.boolreatched = True
                self.boolleg = 0



        elif abs(self.x - self.x1) < 0.3 and abs(self.y - self.y1) < 0.3 and self.z < self.z1:
            self.z += self.initial_z * (self.timer1_time / self.timer1_iter)
            self.timer1_time += self.time_period
            print(f"moving upward x,y,z are {self.x}, {self.y}, {self.z}")

        elif abs(self.x - self.x1) < 0.3 and abs(self.y - self.y1) < 0.3 and abs(self.z -self.z1) < 0.3:
            if self.boolreatched:
                self.timer1_time = 0
                print(f"reatched fourth endpoint x,y,z are {self.x}, {self.y}, {self.z}")
                self.boolreatched = False

            else:
                self.x = self.x + (self.legspa * np.cos(self.alp)) * (self.timer1_time / self.timer1_iter)
                self.y = self.y + (self.legspa * np.cos(self.beta)) * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period                    # for real time time, can be multiplied and divided accouring to our needs
                print(f"moving forward x,y,z are {self.x}, {self.y}, {self.z}")

        else:
            print("The given self.x, self.y, and self.z do not lie in the locus of leg tip")







def main(arg = None):
    rclpy.init()
    hex_controller = Hex_Controller()
    rclpy.spin(hex_controller)
    hex_controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()



    



        
        
        






