import wiringpi2

PWM_PIN = 18
DUTY = 0

wiringpi2.wiringPiSetupGpio()
wiringpi2.pinMode(PWM_PIN, wiringpi2.GPIO.PWM_OUTPUT)
wiringpi2.pwmSetMode(wiringpi2.GPIO.PWM_MODE_MS)
wiringpi2.pwmSetClock(375)

try:
    while True:
        for DUTY in range(40, 120, 1):
            print DUTY
            wiringpi2.pwmWrite(PWM_PIN, DUTY)
            wiringpi2.delay(100)

except KeyboardInterrupt:
    pass

wiringpi2.pwmWrite(PWM_PIN, 0)
