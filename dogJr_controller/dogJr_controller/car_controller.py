#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class CarControllerNode(Node):
    
    def __init__(self):
        super().__init__("car_controller")
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "/demo/cmd_demo",10)
        self.scan_subscriber_ = self.create_subscription(
            LaserScan, "/scan",self.scan_callback,10)
        self.get_logger().info("Car controller node has been started")

    def scan_callback(self, laser_scan: LaserScan):
        #cmd = Twist()

        if all(y > 2.5 for y in laser_scan.ranges):
            self.get_logger().info("All clear")
            cmd = Twist()
            cmd.linear.x = 1.0
            cmd.angular.z = 0.0
            self.cmd_vel_publisher_.publish(cmd)

        elif all(y > 2.5 for y in laser_scan.ranges[:14]) and any(y < 2.5 for y in laser_scan.ranges[15:]):
            self.get_logger().info("Obstacle on the left")
            cmd = Twist()
            cmd.linear.x = 0.5
            cmd.angular.z = -1.0
            self.cmd_vel_publisher_.publish(cmd)

        elif any(y < 2.5 for y in laser_scan.ranges[:14]) and all(y > 2.5 for y in laser_scan.ranges[15:]):
            self.get_logger().info("Obstacle on the right")
            cmd = Twist()
            cmd.linear.x = 0.5
            cmd.angular.z = 1.0
            self.cmd_vel_publisher_.publish(cmd)
        
        elif (laser_scan.ranges[0]==laser_scan.ranges[29]) and (laser_scan.ranges[1]==laser_scan.ranges[28]) and (laser_scan.ranges[0] < 2.5): 
            # This condition is tu turn in a corner
            self.get_logger().info("Arriving a corner")
            cmd = Twist()
            cmd.linear.x = 0.5
            cmd.angular.z = 1.0
            self.cmd_vel_publisher_.publish(cmd)

        elif (laser_scan.ranges[14] < 2.5) or (laser_scan.ranges[15] < 2.5): 
            # This condition is tu turn when an object is right in front of the car
            self.get_logger().info("Obstacle on the front")
            cmd = Twist()
            cmd.linear.x = 0.5
            cmd.angular.z = 1.0
            self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = CarControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()