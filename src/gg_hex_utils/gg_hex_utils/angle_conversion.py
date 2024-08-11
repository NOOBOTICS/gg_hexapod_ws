#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from arm_interface_pkg.srv import EulerToQuaternion, QuaternionToEuler
from tf_transformations import quaternion_from_euler, euler_from_quaternion


class AngleConversion(Node):

    def __init__(self):
        super().__init__('angle_conversion')
        self.srv_euler_to_quat = self.create_service(EulerToQuaternion, 'eulertoquaternion', self.euler_to_quaternion_callback)
        self.srv_quat_to_euler = self.create_service(QuaternionToEuler, 'quaterniontoeuler', self.quaternion_to_euler_callback)
        self.get_logger().info("Angle conversion services are ready")

    def euler_to_quaternion_callback(self, request, response):
        self.get_logger().info("Request to convert Euler angles roll: %f, pitch: %f, yaw: %f to Quaternion" % (request.roll, request.pitch, request.yaw))
        (response.x, response.y, response.z, response.w) = quaternion_from_euler(request.roll, request.pitch, request.yaw)
        self.get_logger().info("Quaternion values: x: %f, y: %f, z: %f, w: %f" % (response.x, response.y, response.z, response.w))
        return response
    
    def quaternion_to_euler_callback(self, request, response):
        self.get_logger().info("Request to convert Quaternion values x: %f, y: %f, z: %f, w: %f to Euler angles" % (request.x, request.y, request.z, request.w))
        (response.roll, response.pitch, response.yaw) = euler_from_quaternion([request.x, request.y, request.z, request.w])
        self.get_logger().info("Euler angles: roll: %f, pitch: %f, yaw: %f" % (response.roll, response.pitch, response.yaw))
        return response

def main(args=None):
    rclpy.init(args=args)

    angle_conversion_service = AngleConversion()

    rclpy.spin(angle_conversion_service)
    angle_conversion_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
