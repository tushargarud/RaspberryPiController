import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

try:
    GPIO.output(servoPIN, GPIO.LOW)
    print("Camera started")
except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()
