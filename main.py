import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# IR Sensor pins
SENSOR_PIN1 = 8 
SENSOR_PIN2 = 10

# Set pin values
ena1 = 12
in1 = 24
in2 = 26

ena2 = 32
in3 = 11
in4 = 13

# Setup sensor pins
GPIO.setup(SENSOR_PIN1, GPIO.IN)
GPIO.setup(SENSOR_PIN2, GPIO.IN)

# Board and pin setup
GPIO.setup(ena1, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# Set all pins low to start to prevent rotation on run
GPIO.output(ena1, GPIO.LOW)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(ena2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

# Create PWM instance on enable pin A at 50 Hz
motor1 = GPIO.PWM(ena1, 50)
motor2 = GPIO.PWM(ena2, 50)

def move_forward():
    motor1.start(25)
    motor2.start(25)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def turn_right():
    motor1.start(25)
    motor2.start(25)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

     
def turn_left():
    motor1.start(25)
    motor2.start(25)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
     

try:
    while True:
        left_sensor = GPIO.input(SENSOR_PIN2)
        right_sensor = GPIO.input(SENSOR_PIN1)
        
        # Both sensors detect black line - move forward
        if left_sensor == GPIO.HIGH and right_sensor == GPIO.HIGH:
            print("Black line detected - Moving forward")
            move_forward()
        
        # Both sensors off line - stop
        elif left_sensor == GPIO.LOW and right_sensor == GPIO.LOW:
            print("No line detected - Stopping")
            stop()
            
        # Left sensor off line - turn right
        elif left_sensor == GPIO.LOW:
            print("Turn right")
            turn_right()
            
        # Right sensor off line - turn left
        elif right_sensor == GPIO.LOW:
            print("Turn left")
            turn_left()

        time.sleep(0.1)
       

except KeyboardInterrupt:
    # Stop motor
    motor1.stop()
    motor2.stop()
    
    # Cleanup pins
    GPIO.cleanup()