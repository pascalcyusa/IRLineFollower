import RPi.GPIO as GPIO
import time

# IR Sensor pins
SENSOR_PIN1 = 8 
SENSOR_PIN2 = 10

# Motor 1 pins (Left)
ENA = 12  # Hardware PWM channel 0
IN1 = 24
IN2 = 26

# Motor 2 pins (Right)
ENB = 33
IN3 = 11
IN4 = 13

# Motor settings
PWM_FREQ = 8000 
BASE_SPEED = 50 
TURN_SPEED = 30 


# Setup GPIO
GPIO.setmode(GPIO.BOARD)

# Setup sensor pins
GPIO.setup(SENSOR_PIN1, GPIO.IN)
GPIO.setup(SENSOR_PIN2, GPIO.IN)

# Setup motor 1 pins (Left)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Setup motor 2 pins (Right)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)


# Initialize all motor control pins to LOW
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)

# Setup motor pins and PWM
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
pwm_left = GPIO.PWM(ENA, PWM_FREQ)
pwm_right = GPIO.PWM(ENB, PWM_FREQ)
pwm_left.start(0)
pwm_right.start(0)

def move_forward():
    # Left motor forward
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    # Right motor forward
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    # Set speeds using PWM
    pwm_left.ChangeDutyCycle(BASE_SPEED)
    pwm_right.ChangeDutyCycle(BASE_SPEED)

def turn_left():
    # Left motor slower
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    # Right motor faster
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    # Set speeds using PWM
    pwm_left.ChangeDutyCycle(TURN_SPEED)
    pwm_right.ChangeDutyCycle(BASE_SPEED)

def turn_right():
    # Left motor faster
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    # Right motor slower
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    # Set speeds using PWM
    pwm_left.ChangeDutyCycle(BASE_SPEED)
    pwm_right.ChangeDutyCycle(TURN_SPEED)

def stop():
    # Stop both motors
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)

try:
    while True:
        left_sensor = GPIO.input(SENSOR_PIN1)
        right_sensor = GPIO.input(SENSOR_PIN2)
        
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
    # Clean up
    stop()
    pwm_left.stop()
    pwm_right.stop()
    GPIO.cleanup()
