# Turorial on https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html
import rclpy 
from rclpy.node import Node

#from std_msgs.msg import String
from geometry_msgs.msg import Twist 

class MinimalPublisher(Node): # Node is our parent class
    def __init__(self):
        super.__init__('minimal_publisher') #gives our init method a name
        self.publisher_ = self.create_publisher (Twist, 'turtlesim1/cmd_vel', 10)
        """ Method creates a publisher 
        Twist is the message, turtlesim1/cmd_vel is the topic & 10 is the queue length. """
        #method timer to publish at a specific rate
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.5
        self.publisher_.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args) #initialize ROS2 Python client library

    minimal_publisher = MinimalPublisher() #create an instance of our class

    rclpy.spin(minimal_publisher) #keep the node running until it is shut down
    """
    Destroy the node explicitly
    (optional - otherwise it will be done automatically when the garbage collector destroys the node object)"""
    minimal_publisher.destroy_node() #destroy the node explicitly (optional)
    rclpy.shutdown() #shutdown the ROS2 client library

if __name__ == '__main__':    
    main()