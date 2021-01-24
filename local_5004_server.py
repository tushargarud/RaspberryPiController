#!/home/pi/virtual_envs/controller_venv/bin/python3

import RPi.GPIO as GPIO
import time
import os
import _thread
from flask import Flask, render_template, request
app = Flask(__name__)
HEAD_UP = 38
HEAD_DOWN = 40
LEG_UP = 32
LEG_DOWN = 36
pins_used = [HEAD_UP, HEAD_DOWN, LEG_UP, LEG_DOWN]
GPIO.setmode(GPIO.BOARD)
DEFAULT_POSITION = HEAD_DOWN
DEFAULT_DURATION = 5
for x in pins_used:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.LOW)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bedController")
def action():
    bed_part = request.args.get('bed_part')
    bed_position = request.args.get('bed_position')
    duration = int(request.args.get('duration'))
    # resp = f"bed_part={bed_part} bed_position={bed_position} duration={duration}"
    # print(resp)
    relay = DEFAULT_POSITION
    if duration is None or duration < 0 or duration > 20:
        duration = DEFAULT_DURATION
    if bed_part is not None and bed_position is not None:
        if bed_part.lower() == "head":
            if bed_position.lower() == "up":
                relay = HEAD_UP
            else:
                relay = HEAD_DOWN
        elif bed_part.lower() == "leg":
            if bed_position.lower() == "up":
                relay = LEG_UP
            else:
                relay = LEG_DOWN
        GPIO.output(relay, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(relay, GPIO.LOW)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)
    

