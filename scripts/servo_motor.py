import wiringpi
import time
import sys

servo_pin = 18
param = sys.argv
set_degree = int(param[1])
print(set_degree)

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(servo_pin, 2)

wiringpi.pwmSetMode(0)
wiringpi.pwmSetMode(1024)
wiringpi.pwmSetMode(375)

if (set_degree >= -90):
  move_deg = int(81 + 41 / 90 * set_degree)
  wiringpi.pwmWrite(servo_pin, move_deg)

