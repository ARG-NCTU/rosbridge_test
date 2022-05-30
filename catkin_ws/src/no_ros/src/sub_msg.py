#! /usr/bin/env python

import rospy
import math
from std_msgs.msg import String

class subandprint(object):
 
    def __init__(self):
        self.sub = rospy.Subscriber("/no_ros_publish", String, self.callback_sub)

    def callback_sub(self, data):
        print("I heard %s",data.data)

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    SUB = subandprint()
    rospy.spin() #run forever