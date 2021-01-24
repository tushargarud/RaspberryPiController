import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  p.ChangeDutyCycle(5)
  time.sleep(3.4)
  print("Lock closed")
except KeyboardInterrupt:
  p.stop()
  print("stopped")
finally:
  GPIO.cleanup()