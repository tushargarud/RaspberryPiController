import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

try:
    GPIO.output(servoPIN, GPIO.LOW)
    print("Camera started")
except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()
