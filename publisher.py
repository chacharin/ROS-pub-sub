#!/usr/bin/env python

import rospy
from std_msgs.msg import String

counter=0

def talker():
    global counter
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        hello_str = "Chacharin %s" % str(counter)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        counter=counter+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass