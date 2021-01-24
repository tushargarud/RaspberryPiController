import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

try:
    GPIO.output(servoPIN, GPIO.HIGH)
    print("Camera stopped")
except KeyboardInterrupt:
    print("Program stopped")
