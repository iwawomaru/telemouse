#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from audio_common_msgs.msg import AudioData

import os, sys
import numpy as np

class MakeAudioDataset(object):
    def __init__(self):
        self.disconf = -1
        self.dataset = []

        rospy.init_node("audio_trainer")
        audio_sub = rospy.Subscriber("audio", AudioData, self.audio_callback)
        disconf_sub = rospy.Subscriber("disconfort", Int16, self.disconf_callback)

    def __del__(self):
        dataset = np.array(self.dataset)
        np.save("test.npy", dataset)

    def disconf_callback(self, disconf):
        self.disconf = disconf.data

    def audio_callback(self, audio):
        if self.disconf == -1:
            return
        int_array = [ord(n) for n in audio.data]
        # print int_array[0:10]
        self.dataset.append((int_array, self.disconf))

obj = MakeAudioDataset()
rospy.spin()
