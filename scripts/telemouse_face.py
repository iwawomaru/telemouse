#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16MultiArray
import os, sys
import pygame
from pygame.locals import *

import numpy as np

SCREEN_SIZE = (800, 480)
pos_list = np.array([(300, 120), (400, 120), (500, 120), 
                     (300, 240), (400, 240), (500, 240), 
                     (300, 360), (400, 360), (500, 360)])
lbias = np.array([-150, 0])
rbias = np.array([150, 0])

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("telemouse_face")

dname = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../img/")

eye_l = pygame.image.load(os.path.join(dname, "robomi_eye_l.png")).convert_alpha()
eye_l_rect = eye_l.get_rect()
eye_l_rect.center = pos_list[4] + lbias

eye_r = pygame.image.load(os.path.join(dname, "robomi_eye_r.png")).convert_alpha()
eye_r_rect = eye_r.get_rect()
eye_r_rect.center = pos_list[4] + rbias

def callback(array):
        rospy.loginfo("I heard "+str(array.data))

        pos_id = np.argmax(array.data)
        eye_l_rect.center = pos_list[pos_id] + lbias
        eye_r_rect.center = pos_list[pos_id] + rbias        

        screen.fill((255, 255, 255))
        screen.blit(eye_l, eye_l_rect)
        screen.blit(eye_r, eye_r_rect)
        pygame.display.update()
        

rospy.init_node("telemouse_face")
sub = rospy.Subscriber("direction", Int16MultiArray, callback)
screen.fill((255, 255, 255))
screen.blit(eye_l, eye_l_rect)
screen.blit(eye_r, eye_r_rect)
pygame.display.update()
rospy.spin()
