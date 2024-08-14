#!/usr/bin/env python3
import rclpy  # Import ROS2 Python library
from rclpy.node import Node  # Import Node module
from std_msgs.msg import String  # Import String message type

# Class definition for our ROS2 subscriber node
class MySubscriber(Node):
    def __init__(self):
        super().__init__('second_subscriber')  # Initialize the Node with the name 'my_subscriber'
        self.subscription = self.create_subscription(String,'topic2',self.listener_callback,10)  # The queue size
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Hearing: "%s"' % msg.data)  # Log the received message

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS2 Python communication
    second_subscriber = MySubscriber()  # Create a MySubscriber object
    rclpy.spin(second_subscriber)  # Keep the node alive to continue listening

    second_subscriber.destroy_node()  # Cleanup the node
    rclpy.shutdown()  # Shutdown ROS2 Python communication

if __name__ == '__main__':
    main()