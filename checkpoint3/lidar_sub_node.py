#!/usr/bin/env python3
import rospy as rp
from std_msgs.msg import String 

def callback(msg):
    rp.loginfo("I heard: %s", msg.data)

def other(msg):
    rp.loginfo("I heard: %s", msg.data)

def listener():
    rp.Subscriber("/lidar_info/chatter", String, callback)
    rp.Subscriber("/lidar_info/three", String, callback=other)
    rp.init_node('listener', anonymous=True)
    
if __name__ == '__main__':
    listener()
    rp.spin()