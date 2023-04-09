#!/usr/bin/env python3
import rospy

from chekcPoint2.msgs import custom

def log(msg):
    rospy.loginfo("%s X: %f Y: %f Z: %f", msg.message, msg.x, msg.y, msg.z)

def triangulation():
    pub = rospy.Publisher("Publishin node", custom, queue_size=10)
    rospy.init_node("Custom_Msg", anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher node started!!")
    while not rospy.is_shutdown():
        msg = custom()
        msg.message = "My Postion is: "
        msg.x = 2.0
        msg.y = 1.5
        msg.z = 3.0
        log(msg)
        pub.publish(msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        triangulation()      
    except rospy.ROSInterruptException:
        pass