#!/usr/bin/env python3
import rospy
from checkpoint2.msg import custom

class triangulation_node:
    def __init__(self):
        self.msg = custom()
        self.msg.cone_id = "My Postion is: "
        self.msg.x = 2.0
        self.msg.y = 1.5
        self.msg.z = 3.0
        rospy.init_node("custom_Msg", anonymous=True)
        self.pub = rospy.Publisher("publishing_node", custom, queue_size=10)    
        self.rate = rospy.Rate(1)
        rospy.loginfo("Publisher node started!!")
        
    def triangulation(self):
        while not rospy.is_shutdown():
            log(self.msg)
            self.pub.publish(self.msg)
            self.rate.sleep()
            
def log(msg):
        rospy.loginfo("%s X: %f Y: %f Z: %f time: %f", msg.cone_id, msg.x, msg.y, msg.z, msg.time)


if __name__ == '__main__':
    try:
        tri = triangulation_node()
        tri.triangulation()      
    except rospy.ROSInterruptException:
        pass