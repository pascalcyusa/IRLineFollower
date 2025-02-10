import RPi.GPIO as GPIO
import time

sensor_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        sensor_value = GPIO.input(sensor_pin)
        print("Sensor reading:", sensor_value)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
