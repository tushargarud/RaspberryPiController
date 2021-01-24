#!/home/pi/virtual_envs/controller_venv/bin/python3

import RPi.GPIO as GPIO
import time
import os
import _thread
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/lockControl", methods = ["POST"])
def control_lock():
    task = request.form['task']
    if task == 'lock':
        os.system(f"/home/pi/virtual_envs/controller_venv/bin/python3 /home/pi/PiController/RaspberryPiController/close_lock.py")
    elif task == 'unlock':
        os.system(f"/home/pi/virtual_envs/controller_venv/bin/python3 /home/pi/PiController/RaspberryPiController/open_lock.py")
    return render_template('index.html')

@app.route("/cameraControl")
def control_camera():
    status = request.args.get('status')
    if status == 'off':
        os.system(f"/home/pi/virtual_envs/controller_venv/bin/python3 /home/pi/PiController/RaspberryPiController/wyzecam_off.py")
    elif status == 'on':
        os.system(f"/home/pi/virtual_envs/controller_venv/bin/python3 /home/pi/PiController/RaspberryPiController/wyzecam_on.py")
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
    

