#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanSubscriberNode(Node):
    
    def __init__(self):
        super().__init__("scan_subscriber")
        self.scan_subscriber_ = self.create_subscription(
            LaserScan, "/scan",self.scan_callback,10)
        self.get_logger().info("Scan subscriber node has been started")

    def scan_callback(self,msg: LaserScan):
        self.get_logger().info(str(msg.ranges)) 
    

def main(args=None):
    rclpy.init(args=args)
    node =ScanSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()