import RPi.GPIO as GPIO
import time

# IR Sensor pins
SENSOR_PIN1 = 10 
SENSOR_PIN2 = 12 

# Motor pins
MOTOR_LEFT = 32
MOTOR_RIGHT = 33
PWM_FREQ = 100  # PWM frequency in Hz
BASE_SPEED = 50  # Base speed (0-100)
TURN_SPEED = 30  # Speed for turning

# Setup GPIO
GPIO.setmode(GPIO.BOARD)

# Setup sensor pins
GPIO.setup(SENSOR_PIN1, GPIO.IN)
GPIO.setup(SENSOR_PIN2, GPIO.IN)

# Setup motor pins
GPIO.setup(MOTOR_LEFT, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT, GPIO.OUT)

# Setup PWM
pwm_left = GPIO.PWM(MOTOR_LEFT, PWM_FREQ)
pwm_right = GPIO.PWM(MOTOR_RIGHT, PWM_FREQ)

# Start PWM with 0% duty cycle
pwm_left.start(0)
pwm_right.start(0)

def move_forward():
    pwm_left.ChangeDutyCycle(BASE_SPEED)
    pwm_right.ChangeDutyCycle(BASE_SPEED)

def turn_left():
    pwm_left.ChangeDutyCycle(TURN_SPEED)
    pwm_right.ChangeDutyCycle(BASE_SPEED)

def turn_right():
    pwm_left.ChangeDutyCycle(BASE_SPEED)
    pwm_right.ChangeDutyCycle(TURN_SPEED)

def stop():
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)

try:
    while True:
        # Both sensors detect black line - move forward
        if GPIO.input(SENSOR_PIN1) == GPIO.HIGH and GPIO.input(SENSOR_PIN2) == GPIO.HIGH:
            print("Black line detected - Moving forward")
            move_forward()
            
        # Left sensor off line - turn right
        elif GPIO.input(SENSOR_PIN1) == GPIO.LOW:
            print("Turn right")
            turn_right()
            
        # Right sensor off line - turn left
        elif GPIO.input(SENSOR_PIN2) == GPIO.LOW:
            print("Turn left")
            turn_left()
            
        # Both sensors off line - stop
        else:
            print("No line detected - Stopping")
            stop()

        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up
    stop()
    pwm_left.stop()
    pwm_right.stop()
    GPIO.cleanup()
    
