#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

import os, sys
import numpy as np

import pygame

class Avoidance(object):

    def __init__(self, node_name="avoidance_node"):

        rospy.init_node(node_name)
        sub = rospy.Subscriber("disconfort", Int16, self.callback)
      
        pygame.mixer.init()
        self.hit_sound = pygame.mixer.Sound("n_418d125.wav")

    def callback(self, disconfort):

        if disconfort.data == 1:
            
            self.hit_sound.play()
    
if __name__ == "__main__":
    obj = Avoidance()
    rospy.spin()

