#!/usr/bin/python
# coding: utf-8 

import RPi.GPIO as GPIO
import time
import signal
import sys 

def exit_handler(signal, frame):
    # Ctrl+Cが押されたときにデバイスを初期状態に戻して終了する。
    print("\nExit")
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    servo.stop()
    GPIO.cleanup()
    sys.exit(0)
    
# 終了処理用のシグナルハンドラを準備
signal.signal(signal.SIGINT, exit_handler)

GPIO.setmode(GPIO.BCM)

# GPIO 21番を使用
gp_out = 21

GPIO.setup(gp_out, GPIO.OUT)
# pwm = GPIO.PWM([チャンネル], [周波数(Hz)])
servo = GPIO.PWM(gp_out, 500) 

# 初期化
servo.start(0.0)

# val = [2.5,3.6875,4.875,6.0625,7.25,8.4375,9.625,10.8125,12]
val = [(4.0 + 0.5*i) for i in xrange(12)]

RIGHT = 4.5
CENTER = 7.0
LEFT = 9.5

while True:
    servo.ChangeDutyCycle(RIGHT)
    time.sleep(1.0)

    servo.ChangeDutyCycle(CENTER)
    time.sleep(1.0)

    servo.ChangeDutyCycle(LEFT)
    time.sleep(1.0)
    

