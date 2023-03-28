#!/usr/bin/env python3
import rospy as rp
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import random
from datetime import datetime


class lidar_sub_node:

    def __init__(self):
        self.my_data = ''
        rp.init_node('listener', anonymous=True)
        rp.Subscriber("/fsds/lidar/Lidar1", PointCloud2, self.callback_func)
        self.rate = rp.Rate(1)
        self.pub = rp.Publisher("/lidar_info/chatter", String, queue_size= 10)
        self.pub2 = rp.Publisher("/lidar_info/three", String, queue_size=10)
        self.xyz = []
        
        self.time = str(datetime.now())
        
        
    def callback_func(self, msg):
        points = np.around(list(pc2.read_points(msg, skip_nans=True)), decimals=2)
        self.xyz = points[:,:]
        self.my_data = "XYZ coordinates: \n{}".format(self.xyz)
        
    
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