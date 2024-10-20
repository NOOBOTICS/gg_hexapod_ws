import rclpy
from rclpy.node import Node                                                                                                                                                                                        
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import numpy as np
from std_msgs.msg import Int16
import time


class Hex_Controller(Node):
    def __init__(self):
        super().__init__("Hex_Controller")

        self.select = 90

        self.theta = 90  # in degrees
        self.initial_z = 3   # initial height difference in cm
        self.legspa = 2   # cm (leg span)

        self.theta_00 = 45  # in degrees
        self.initial_z_00 = 3   # initial height difference in cm
        self.legspa_00 = 10   # cm (leg span)

        # Convert theta to radians
        self.alp = np.deg2rad(self.theta)
        self.beta = np.deg2rad(90 - self.theta)
        self.gama = np.deg2rad(90)

        self.alp_00 = np.deg2rad(self.theta_00)
        self.beta_00 = np.deg2rad(90 - self.theta_00)
        self.gama_00 = np.deg2rad(90)

        # Central position of trajectory
        self.x0 = 10
        self.y0 = 0
        self.z0 = 0

        self.x0_00 = 20
        self.y0_00 = 0
        self.z0_00 = 0

        # Calculate positions from x0 and leg span (for original set)
        self.x1 = self.x0 - ((self.legspa / 2) * np.cos(self.alp))    
        self.y1 = self.y0 - ((self.legspa / 2) * np.cos(self.beta))  
        self.z1 = self.z0 - ((self.legspa / 2) * np.cos(self.gama))  

        print(f"Original x1, y1, z1: {self.x1}, {self.y1}, {self.z1}")

        self.x2 = self.x0 + ((self.legspa / 2) * np.cos(self.alp))
        self.y2 = self.y0 + ((self.legspa / 2) * np.cos(self.beta))  
        self.z2 = self.z0 + ((self.legspa / 2) * np.cos(self.gama))  

        print(f"Original x2, y2, z2: {self.x2}, {self.y2}, {self.z2}")

        # Calculate positions from x0_00 and legspa_00 (for _00 set)
        self.x1_00 = self.x0_00 - ((self.legspa_00 / 2) * np.cos(self.alp_00))    
        self.y1_00 = self.y0_00 - ((self.legspa_00 / 2) * np.cos(self.beta_00))  
        self.z1_00 = self.z0_00 - ((self.legspa_00 / 2) * np.cos(self.gama_00))  

        print(f"_00 x1, y1, z1: {self.x1_00}, {self.y1_00}, {self.z1_00}")

        self.x2_00 = self.x0_00 + ((self.legspa_00 / 2) * np.cos(self.alp_00))
        self.y2_00 = self.y0_00 + ((self.legspa_00 / 2) * np.cos(self.beta_00))  
        self.z2_00 = self.z0_00 + ((self.legspa_00 / 2) * np.cos(self.gama_00))  

        print(f"_00 x2, y2, z2: {self.x2_00}, {self.y2_00}, {self.z2_00}")

        # Leg starting coordinates (for original set)
        self.x = self.x1
        self.y = self.y1
        self.z = self.z1

        # Leg starting coordinates (for _00 set)
        self.x_00 = self.x1_00
        self.y_00 = self.y1_00
        self.z_00 = self.z1_00

        # Timer for updating position
        self.time_period = 0.1
        self.timer1 = self.create_timer(self.time_period, self.timer1_callback)
        self.timer1_time = 0
        self.timer1_iter = 100
        self.boolleg = 0
        self.boolreatched = False
        self.error = 0.3

        self.boollegsub = self.create_subscription(
            Int16,
            'boolleg',
            self.boolleg_callback,
            10)

    def boolleg_callback(self, msg):
        self.boolleg = msg.data

    def timer1_callback(self):
        if self.select == 90:

            
            if self.x1 <= self.x <= self.x2 and self.y1 <= self.y <= self.y2 and self.boolleg == 0:
                self.x = self.x + (self.legspa * np.cos(self.alp)) * (self.timer1_time / self.timer1_iter)
                self.y = self.y + (self.legspa * np.cos(self.beta)) * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period                    # for real time time, can be multiplied and divided accouring to our needs
                print(f"moving forward x,y,z are {self.x}, {self.y}, {self.z}")

            elif abs(self.x - self.x2) < self.error and abs(self.y - self.y2) < self.error and self.boolleg == 0 :
                if not self.boolreatched:
                    self.timer1_time = 0
                    print(f"reached first endpoint x,y,z are {self.x}, {self.y}, {self.z}")
                    self.boolreatched = True

                else:
                    self.z -= (self.initial_z * (self.timer1_time / self.timer1_iter))
                    self.timer1_time += self.time_period
                    print(f"moving downward x,y,z are {self.x}, {self.y}, {self.z}")

        

            elif abs(self.x - self.x2) < self.error and abs(self.y - self.y2) < self.error and self.boolleg == 1 :
                if self.boolreatched :
                    self.timer1_time = 0
                    print(f"reached second endpoint x,y,z are {self.x}, {self.y}, {self.z}")
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

            elif abs(self.x - self.x1) < self.error and abs(self.y - self.y1) < self.error and self.boolleg == 1:
                if not self.boolreatched:
                    self.timer1_time = 0
                    print(f"reached third endpoint x,y,z are {self.x}, {self.y}, {self.z}")
                    self.boolreatched = True
                    self.boolleg = 0



            elif abs(self.x - self.x1) < self.error and abs(self.y - self.y1) < self.error and self.z < self.z1:
                self.z += self.initial_z * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"moving upward x,y,z are {self.x}, {self.y}, {self.z}")

            elif abs(self.x - self.x1) < self.error and abs(self.y - self.y1) < self.error and abs(self.z -self.z1) < self.error:
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








        elif self.select == 45:
            # Movement logic for the _00 set
            if self.x1_00 <= self.x_00 <= self.x2_00 and self.y1_00 <= self.y_00 <= self.y2_00 and self.boolleg == 0:
                self.x_00 = self.x_00 + (self.legspa_00 * np.cos(self.alp_00)) * (self.timer1_time / self.timer1_iter)
                self.y_00 = self.y_00 + (self.legspa_00 * np.cos(self.beta_00)) * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"Moving forward: _00 set -> x_00: {self.x_00}, y_00: {self.y_00}, z_00: {self.z_00}")
            
            elif abs(self.x_00 - self.x2_00) < self.error and abs(self.y_00 - self.y2_00) < self.error and self.boolleg == 0:
                if not self.boolreatched:
                    self.timer1_time = 0
                    print(f"Reached endpoint: _00 set -> x_00: {self.x_00}, y_00: {self.y_00}, z_00: {self.z_00}")
                    self.boolreatched = True
                else:
                    self.z_00 -= (self.initial_z_00 * (self.timer1_time / self.timer1_iter))
                    self.timer1_time += self.time_period
                    print(f"Moving downward: _00 set -> x_00: {self.x_00}, y_00: {self.y_00}, z_00: {self.z_00}")
            
            elif abs(self.x_00 - self.x2_00) < self.error and abs(self.y_00 - self.y2_00) < self.error and self.boolleg == 1 :
                if self.boolreatched :
                    self.timer1_time = 0
                    print(f"reached second endpoint x,y,z are {self.x_00}, {self.y_00}, {self.z_00}")
                    self.boolreatched = False

                elif self.x_00 >= self.x1_00 and self.y_00 >= self.y1_00 and self.boolleg == 1:
                    self.x_00 = self.x2_00 - (self.legspa_00 * np.cos(self.alp_00)) * (self.timer1_time / self.timer1_iter)
                    self.y_00 = self.y2_00 - (self.legspa_00 * np.cos(self.beta_00)) * (self.timer1_time / self.timer1_iter)
                    self.timer1_time += self.time_period
                    print(f"moving backwards x,y,z are {self.x_00}, {self.y_00}, {self.z_00}")


            elif self.x_00 >= self.x1_00 and self.y_00 >= self.y1_00 and self.boolleg == 1:
                self.x_00 = self.x2_00 - (self.legspa_00 * np.cos(self.alp_00)) * (self.timer1_time / self.timer1_iter)
                self.y_00 = self.y2_00 - (self.legspa_00 * np.cos(self.beta_00)) * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"moving backwards x,y,z are {self.x_00}, {self.y_00}, {self.z_00}")

            elif abs(self.x_00 - self.x1_00) < self.error and abs(self.y_00 - self.y1_00) < self.error and self.boolleg == 1:
                if not self.boolreatched:
                    self.timer1_time = 0
                    print(f"reached third endpoint x,y,z are {self.x_00}, {self.y_00}, {self.z_00}")
                    self.boolreatched = True
                    self.boolleg = 0



            elif abs(self.x_00 - self.x1_00) < self.error and abs(self.y_00 - self.y1_00) < self.error and self.z_00 < self.z1_00:
                self.z_00 += self.initial_z_00 * (self.timer1_time / self.timer1_iter)
                self.timer1_time += self.time_period
                print(f"moving upward x,y,z are {self.x_00}, {self.y_00}, {self.z_00}")

            elif abs(self.x_00 - self.x1_00) < self.error and abs(self.y_00 - self.y1_00) < self.error and abs(self.z_00 -self.z1_00) < self.error:
                if self.boolreatched:
                    self.timer1_time = 0
                    print(f"reatched fourth endpoint x,y,z are {self.x_00}, {self.y_00}, {self.z_00}")
                    self.boolreatched = False

                else:
                    self.x_00 = self.x_00 + (self.legspa_00 * np.cos(self.alp_00)) * (self.timer1_time / self.timer1_iter)
                    self.y_00 = self.y_00 + (self.legspa_00 * np.cos(self.beta_00)) * (self.timer1_time / self.timer1_iter)
                    self.timer1_time += self.time_period                    # for real time time, can be multiplied and divided accouring to our needs
                    print(f"moving forward x,y,z are {self.x_00}, {self.y_00}, {self.z_00}")

            else:
                print("The given self.x, self.y, and self.z do not lie in the locus of leg tip")


def main(arg=None):
    rclpy.init()
    hex_controller = Hex_Controller()
    rclpy.spin(hex_controller)
    hex_controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
