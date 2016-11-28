#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from audio_common_msgs.msg import AudioData

import os, sys
import numpy as np

def callback(audio):

    int_array = [ord(n) for n in audio.data]
    print int_array

    # print np.array(audio.data, dtype=np.uint8)
    """
    for d in np.array(audio.data, dtype=np.uint8):
        print d
    """
rospy.init_node("audio_trainer")
sub = rospy.Subscriber("audio", AudioData, callback)
rospy.spin()
