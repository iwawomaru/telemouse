#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from audio_common_msgs.msg import AudioData

import os, sys
import numpy as np

class MakeAudioDataset(object):
    def __init__(self, disconf=0, dres_name="test.npy"):
        self.disconf = disconf
        self.dres_name = dres_name
        self.dataset = []

        rospy.init_node("audio_trainer")
        audio_sub = rospy.Subscriber("audio", AudioData, self.audio_callback)

    def __del__(self):
        dataset = np.array(self.dataset)
        np.save(self.dres_name, dataset)

    def audio_callback(self, audio):
        int_array = [ord(n) for n in audio.data]
        self.dataset.append((int_array, self.disconf))

obj = MakeAudioDataset(disconf=1, dres_name="npy/bayashi_breathe_left.npy")
rospy.spin()
