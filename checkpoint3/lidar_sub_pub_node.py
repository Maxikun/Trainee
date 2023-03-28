#!/usr/bin/env python3

import rospy as rp
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import random
from datetime import datetime

# Define a class for the lidar subscriber node
class lidar_sub_node:

    def __init__(self):
        self.my_data = ''
        rp.init_node('listener', anonymous=True)
        # Subscribe to the PointCloud2 topic "/fsds/lidar/Lidar1"
        rp.Subscriber("/fsds/lidar/Lidar1", PointCloud2, self.callback_func)
        self.rate = rp.Rate(1)
        # Define two publishers for the String topics "/lidar_info/chatter" and "/lidar_info/three"
        self.pub = rp.Publisher("/lidar_info/chatter", String, queue_size= 10)
        self.pub2 = rp.Publisher("/lidar_info/three", String, queue_size=10)
        self.xyz = []
        
        self.time = str(datetime.now())
        
    # Define a callback function to read the XYZ coordinates of the lidar points
    def callback_func(self, msg):
        points = np.around(list(pc2.read_points(msg, skip_nans=True)), decimals=2)
        self.xyz = points[:,:]
        self.my_data = "XYZ coordinates: \n{}".format(self.xyz)
    
    # Define a talker function to publish random yaw, velocity and time information to the two topics
    def talker(self):
        while not rp.is_shutdown():
            self.yaw = random.randrange(1000)
            self.vel = random.randrange(100)
            self.pub.publish(self.my_data)
            self.pub2.publish("\nYaw: " + str(self.yaw)+ "\nvelocity: " + str(self.vel) + "\ntime: " + self.time)
            rp.loginfo("\nYaw: " + str(self.yaw) + "\nvelocity: " + str(self.vel) + "\ntime: " + self.time)
            rp.loginfo(rp.get_caller_id() + "\nXYZ coordinates: {}".format(self.xyz))
            self.rate.sleep() 
    
if __name__ == '__main__':
    try:
        lidar = lidar_sub_node()
        lidar.talker()
    except rp.ROSInterruptException:
        pass
