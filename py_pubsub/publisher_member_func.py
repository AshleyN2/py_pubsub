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
    