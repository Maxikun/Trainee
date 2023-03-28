#!/usr/bin/env python3

# Import necessary ROS packages and message types
import rospy as rp
from std_msgs.msg import String 

# Define callback function to be executed when a message is received on the "/lidar_info/chatter" topic
def callback(msg):
    rp.loginfo("I heard: %s", msg.data)

# Define another callback function to be executed when a message is received on the "/lidar_info/three" topic
def other(msg):
    rp.loginfo("I heard: %s", msg.data)

# Define listener function that creates subscribers to the two topics and initializes the node
def listener():
    # Create a subscriber to the "/lidar_info/chatter" topic with the callback function "callback"
    rp.Subscriber("/lidar_info/chatter", String, callback)
    # Create another subscriber to the "/lidar_info/three" topic with the callback function "other"
    rp.Subscriber("/lidar_info/three", String, callback=other)
    # Initialize the node with the name "listener" and anonymous flag set to True
    rp.init_node('listener', anonymous=True)

# Main function that calls the listener function and enters a loop to keep the node alive
if __name__ == '__main__':
    # Call the listener function to create subscribers and initialize the node
    listener()
    # Enter a loop to keep the node alive
    rp.spin()
