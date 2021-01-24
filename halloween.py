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

@app.route("/lockControl", methods = ["POST"])
def control_lock():
    task = request.form['task']
    if task == 'lock':
        os.system(f"/home/pi/virtual_envs/controller_venv/bin/python3 /home/pi/PiController/RaspberryPiController/close_lock.py")
    elif task == 'unlock':
        os.system(f"/home/pi/virtual_envs/controller_venv/bin/python3 /home/pi/PiController/RaspberryPiController/open_lock.py")
    return render_template('index.html')

@app.route("/vectorController")
def vector_act():
    vector_command = request.args.get('vector_command')
    if vector_command is not None:
        os.system(f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/{vector_command}.py")
    return render_template('index.html')

@app.route("/vectorCurse")
def vector_curse():
    person_name = request.args.get('person_name')
    if person_name is not None:
        _thread.start_new_thread(os.system, (f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/Curse.py {person_name}",))
        # os.system(f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/Curse.py {person_name}")
    return render_template('index.html')

@app.route("/vectorGoToCharger")
def vector_goto_charger():
    _thread.start_new_thread(os.system, (f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/GoToCharger.py",))
    return render_template('index.html')

@app.route("/vectorMove")
def vector_move():
    direction = request.args.get('direction')
    if direction is not None:
        # os.system(f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/Move.py {direction}")        
        _thread.start_new_thread(os.system, (f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/Move.py {direction}",))
    return render_template('index.html')

@app.route("/actLike")
def vector_actlike():
    thing = request.args.get('thing').lower()
    if thing is not None:
        _thread.start_new_thread(os.system, (f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/{thing}.py",))
    return render_template('index.html')

@app.route("/batteryStatus")
def vector_battery():
    _thread.start_new_thread(os.system, ("/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/battery.py",))
    return render_template('index.html')

@app.route("/setVolume")
def vector_volume():
    volume_value = request.args.get('volume_value').lower()
    if volume_value is not None:
        _thread.start_new_thread(os.system, (f"/home/pi/virtual_envs/vector_venv/bin/python3 /home/pi/vector_programs/VectorPlay/volume.py {volume_value}",))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
    
