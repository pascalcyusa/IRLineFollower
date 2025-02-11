import RPi.GPIO as GPIO
import time

# Cleanup and setup
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# Motor pins definition
# Left motor
ENA = 12
IN1 = 24
IN2 = 26

# Right motor
ENB = 33
IN3 = 11
IN4 = 13

# Setup pins
def setup_pins():
    # Left motor
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    
    # Right motor
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def test_motor(name, ena_pin, in1_pin, in2_pin, duration=3):
    print(f"\nTesting {name} motor...")
    print(f"Using pins - ENA: {ena_pin}, IN1: {in1_pin}, IN2: {in2_pin}")
    
    pwm = GPIO.PWM(ena_pin, 8000)
    pwm.start(0)
    
    # Forward
    print("Testing forward direction...")
    GPIO.output(in1_pin, GPIO.HIGH)
    GPIO.output(in2_pin, GPIO.LOW)
    pwm.ChangeDutyCycle(50)
    time.sleep(duration)
    
    # Stop
    print("Stopping...")
    GPIO.output(in1_pin, GPIO.LOW)
    GPIO.output(in2_pin, GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    time.sleep(1)
    
    # Backward
    print("Testing backward direction...")
    GPIO.output(in1_pin, GPIO.LOW)
    GPIO.output(in2_pin, GPIO.HIGH)
    pwm.ChangeDutyCycle(50)
    time.sleep(duration)
    
    # Stop
    print("Stopping...")
    GPIO.output(in1_pin, GPIO.LOW)
    GPIO.output(in2_pin, GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    
    pwm.stop()
    print(f"{name} motor test complete\n")

try:
    setup_pins()
    
    # Test left motor
    test_motor("Left", ENA, IN1, IN2)
    
    # Test right motor
    test_motor("Right", ENB, IN3, IN4)
    
except KeyboardInterrupt:
    print("\nTest interrupted by user")
    
finally:
    GPIO.cleanup()
    print("GPIO cleanup completed")