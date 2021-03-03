import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

try:
    GPIO.output(servoPIN, GPIO.HIGH)
    print("Camera stopped")
except KeyboardInterrupt:
    print("Program stopped")
