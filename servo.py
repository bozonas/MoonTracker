
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servoPIN = 18
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 100)

p.start(1)

try:
    while True:
#        time.sleep(1)
#       p.ChangeDutyCycle(13)  # turn towards 90 degree
#        time.sleep(1)
#       p.ChangeDutyCycle(7.5)
        inp = input()
        p.ChangeDutyCycle(inp)
#       p.ChangeDutyCycle(0)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
