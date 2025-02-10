import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led = 10    
s2 = 12     

GPIO.setup(led, GPIO.OUT)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def readIRSensor():
    if GPIO.input(s2) == GPIO.LOW:
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)
    time.sleep(0.01)  
try:
    while True:
        readIRSensor()
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program terminated")
