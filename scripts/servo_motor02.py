import wiringpi
import time
import sys

servo_pin = 18

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(servo_pin, 2)

# wiringpi.pwmSetMode(0)
# wiringpi.pwmSetMode(1024)
# wiringpi.pwmSetMode(375)


for i in xrange(0, 1024, 16):
  print i
  wiringpi.pwmWrite(servo_pin, i)
  time.sleep(0.2)

