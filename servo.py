
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servoPIN = 18

#### OLD code #######
# GPIO.setup(servoPIN, GPIO.OUT)

# p = GPIO.PWM(servoPIN, 100)

# p.start(1)

# try:
#     while True:
# #        time.sleep(1)
# #       p.ChangeDutyCycle(13)  # turn towards 90 degree
# #        time.sleep(1)
# #       p.ChangeDutyCycle(7.5)
#         inp = input()
#         p.ChangeDutyCycle(inp)
# #       p.ChangeDutyCycle(0)
# except KeyboardInterrupt:
#     p.stop()
#     GPIO.cleanup()
########################


# Set up the GPIO pin for the servo
GPIO.setup(servoPIN, GPIO.OUT)

# Create a PWM object to control the servo
pwm = GPIO.PWM(servoPIN, 50)  # 50 Hz frequency

# Start PWM with 0% duty cycle (servo at minimum position)
pwm.start(2.5)  # Adjust this value for your servo

# Function to move the servo to a specific angle
def move_servo(angle):
    duty_cycle = 2.5 + (angle / 18.0)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Give the servo time to move

try:
    while True:
        # Move the servo to different angles
        move_servo(0)    # 0 degrees
        move_servo(90)   # 90 degrees
        move_servo(180)  # 180 degrees

except KeyboardInterrupt:
    pass

# Clean up GPIO settings when done
pwm.stop()
GPIO.cleanup()
