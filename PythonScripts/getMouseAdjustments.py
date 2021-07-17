#!/usr/bin/python3

import os
import sys
# import dbus
# import dbus.service
# import dbus.mainloop.glib
            
import json
import math
from flask import Flask, request, jsonify
from werkzeug.datastructures import MultiDict
import logging
import pyautogui


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

calib_x = 0
calib_y = 0
current_x = 0
last_y = 0
last_x = 0
CIRC = 3000

current_pos = 0

# class MouseClient():
# 	def __init__(self):
# 		super().__init__()
# 		self.state = [0, 0, 0, 0]
# 		self.bus = dbus.SystemBus()
# 		self.btkservice = self.bus.get_object(
# 			'org.thanhle.btkbservice', '/org/thanhle/btkbservice')
# 		self.iface = dbus.Interface(self.btkservice, 'org.thanhle.btkbservice')
# 	def send_current(self):
# 		try:
# 			self.iface.send_mouse(0, bytes(self.state))
# 		except OSError as err:
# 			error(err)

# client = MouseClient()


@app.route('/')
def index():
    return jsonify({'status':'Success'})

@app.route('/mousePos', methods=['POST'])
def mousePos():
    global last_x
    global current_pos
    global calib_x
    #The value we are gonna get is from 0 - 2
    my_vals = json.loads(request.data)
    x = my_vals['x'] - calib_x
    y = my_vals['y']
    
    if(x > 1):
        x = 1
    if(x < -1):
        x = -1
    if(x < 0):
        x = 2 + x

    x = x / 2.0

    if(last_x > x):
        m = last_x - x
        if(m <= .5):
            #print("Moving Right")
            current_pos += m
            #print("1M: " + str(m))
            pyautogui.moveRel(int(-127 * m), 0)
        else:
            #print("Moving Left")
            current_pos -=  (1 - m)
            #print("2M: " + str(m))
            pyautogui.moveRel(int(127 * (1 - m)), 0)
    else:
        m = x - last_x
        if(m <= .5):
            current_pos -= m
            #print("3M: " + str(m))
            pyautogui.moveRel(int(127 * m), 0)
            #print("Moving Left")
            
        else:
            current_pos += 1 - m
            #print("4M: " + str(m))
            pyautogui.moveRel(int(-127 * (1 - m)), 0)
            #print("Moving Right")
    #print("Current: " + str(current_pos) + " x: " + str(x))
    last_x = x

    global last_y
    if(last_y > y):
        m = last_y - y
        pyautogui.moveRel(0, int(-127 * m))
    else:
        m = y - last_y
        pyautogui.moveRel(0, int(127 * m))
    last_y = y

    return jsonify({'status':'Mouse has moved'})

@app.route('/calibrate', methods=['POST'])
def calibrate():
    my_vals = json.loads(request.data)
    global calib_x 
    global calib_y
    global current_x
    calib_x = my_vals['x']

    if(calib_x < 0):
        calib_x = (1 - math.fabs(calib_x) + 1) / 2.0
    else:
        calib_x /= 2.0

    current_x = calib_x

    return jsonify({"status":"huh"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
