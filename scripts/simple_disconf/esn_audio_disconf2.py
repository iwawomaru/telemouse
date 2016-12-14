#!/usr/bin/env python
import rospy
from audio_common_msgs.msg import AudioData

import os, sys
import numpy as np

from esn import ESN
import random
import pickle
from scipy.fftpack import fft, fftfreq
import time
import pygame

class AudioDisconf(object):

    def __init__(self):
        self.N = 256
        self.accum = 0
        with open("esn.pickle", "rb") as f:
            self.esn = pickle.load(f)
        rospy.init_node("esn_audio_disconf")
        sub = rospy.Subscriber("audio", AudioData, self.callback)
      
        pygame.mixer.init()
        self.hit_sound = pygame.mixer.Sound("pi.wav")

    def callback(self, audio):
        data = np.array([ord(n) for n in audio.data[:self.N]], np.float32)/255.
        yf = fft(data)[:self.N/2:4]/(self.N/2)
        out = self.esn.prop(yf)[1][0].real
        self.accum = (self.accum + out) if out > 0.6 else self.accum
        if self.accum > 1.3:
            print "deconf: ", self.accum
            self.hit_sound.play()
            self.accum = 0
        else:
            print out
        self.accum *= 0.6
    
    
if __name__ == "__main__":
    obj = AudioDisconf()
    rospy.spin()

