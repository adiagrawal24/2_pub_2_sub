#!/usr/bin/env python3
import rclpy  # Import ROS2 Python library
from rclpy.node import Node  # Import Node module
from std_msgs.msg import String  # Import String message type

# Class definition for our ROS2 subscriber node
class MySubscriber(Node):
    def __init__(self):
        super().__init__('first_subscriber')  # Initialize the Node with the name 'my_subscriber'
        self.subscription = self.create_subscription(String,'topic1',self.listener_callback,10)  # The queue size
        self.subscription  # prevent unused variable warning
        
        self.publisher_ = self.create_publisher(String, 'topic2', 10)  # Create a publisher
        self.timer = self.create_timer(0.5, self.timer_callback)  # Create a timer to call the callback every 0.5 seconds

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)  # Log the received message

    def timer_callback(self):
        msg = String()  # Create a new String message
        msg.data = 'Now 2 Going'  # Assign data to the message
        self.publisher_.publish(msg)  # Publish the message
        self.get_logger().info('Publishing: "%s"' % msg.data)  # Log an info message

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS2 Python communication
    first_subscriber = MySubscriber()  # Create a MySubscriber object
    rclpy.spin(first_subscriber)  # Keep the node alive to continue listening

    first_subscriber.destroy_node()  # Cleanup the node
    rclpy.shutdown()  # Shutdown ROS2 Python communication

if __name__ == '__main__':
    main()