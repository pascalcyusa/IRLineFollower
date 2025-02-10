import RPi.GPIO as GPIO
import time


SENSOR_PIN1 = 10 
SENSOR_PIN2 = 12 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR_PIN1, GPIO.IN)
GPIO.setup(SENSOR_PIN2, GPIO.IN)

try:
    while True:
        # move forward if black line is detected
        if GPIO.input(SENSOR_PIN1) and  GPIO.input(SENSOR_PIN2)  == GPIO.HIGH:
            print("Black line detected")
        else:
            print("On white surface")
            # turn robot left or right so that it stays on course
            if GPIO.input(SENSOR_PIN1) == GPIO.LOW:
                print("Turn right")
            if GPIO.input(SENSOR_PIN2) == GPIO.LOW:
                print("Turn left")

        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
