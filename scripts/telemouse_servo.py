#!/usr/bin/python
# coding: utf-8 

import rospy
from std_msgs.msg import Int16MultiArray
import os, sys

import RPi.GPIO as GPIO
import time
import signal


def exit_handler(signal, frame):
    print("\nExit")
    servo.ChangeDutyCycle(7.0)
    time.sleep(0.5)
    servo.stop()
    GPIO.cleanup()
    time.sleep(1.)
    sys.exit(0)

# 終了処理用のシグナルハンドラを準備
signal.signal(signal.SIGINT, exit_handler)

GPIO.setmode(GPIO.BCM)

# GPIO 21番を使用
gp_out = 21

GPIO.setup(gp_out, GPIO.OUT)
# pwm = GPIO.PWM([チャンネル], [周波数(Hz)])
servo = GPIO.PWM(gp_out, 50) 

# 初期化
servo.start(0.0)

val = [2.5,3.6875,4.875,6.0625,7.25,8.4375,9.625,10.8125,12]
val = [4.875,6.0625,7.25,8.4375,9.625]
val = [5., 6., 7., 8., 9.,]

RIGHT = 6.
CENTER = 7.
LEFT = 8.

f_right = False
f_left = False
f_center = False

def callback(array):
    pos_id = np.argmax(array.data)
    f_right = ((pos_id == 2) or (pos_id == 5) or (pos_id == 8))
    f_center = ((pos_id == 1) or (pos_id == 4) or (pos_id == 7))
    f_left = ((pos_id == 0) or (pos_id == 3) or (pos_id == 6))


while True:
    if f_right:
        servo.ChangeDutyCycle(RIGHT)
        time.sleep(0.5)
    if f_center
        servo.ChangeDutyCycle(CENTER)
        time.sleep(0.5)        
    if f_left:
        servo.ChangeDutyCycle(LEFT)
        time.sleep(0.5)        

