#!/usr/bin/env python3

# Import the necessary ROS packages and message types
import rospy
from checkpoint2.msg import custom

# Define the triangulation_node class
class triangulation_node:
    # Constructor method that initializes the node and the custom message
    def __init__(self):
        # Create an instance of the custom message
        self.msg = custom()
        # Set the cone_id field of the message to a string
        self.msg.cone_id = "My Position is: "
        # Set the x, y, and z fields of the message to floats
        self.msg.x = 2.0
        self.msg.y = 1.5
        self.msg.z = 3.0
        # Initialize the node with a name and an anonymous flag
        rospy.init_node("custom_Msg", anonymous=True)
        # Create a publisher that publishes custom messages to the "publishing_node" topic
        self.pub = rospy.Publisher("publishing_node", custom, queue_size=10)
        # Set the rate at which the node will loop
        self.rate = rospy.Rate(1)
        # Log that the publisher node has started
        rospy.loginfo("Publisher node started!!")

    # Method that loops until the node is shut down, publishing the custom message at a set rate
    def triangulation(self):
        while not rospy.is_shutdown():
            # Log the current state of the message
            log(self.msg)
            # Publish the message
            self.pub.publish(self.msg)
            # Sleep for the set amount of time
            self.rate.sleep()

# Method that logs the fields of the custom message
def log(msg):
    rospy.loginfo("%s X: %f Y: %f Z: %f time: %f", msg.cone_id, msg.x, msg.y, msg.z, msg.time)

# Main function that creates an instance of the triangulation_node class and starts the triangulation loop
if __name__ == '__main__':
    try:
        tri = triangulation_node()
        tri.triangulation()
    except rospy.ROSInterruptException:
        pass
