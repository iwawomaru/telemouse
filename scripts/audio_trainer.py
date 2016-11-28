#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from audio_common_msgs.msg import AudioData

import os, sys
import numpy as np

def callback(array):
        rospy.loginfo("I heard "+str(array.data))

rospy.init_node("audio_trainer")
sub = rospy.Subscriber("", AudioData, callback)
rospy.spin()
