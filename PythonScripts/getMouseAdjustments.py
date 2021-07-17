import json
import math
from flask import Flask, request, jsonify
from werkzeug.datastructures import MultiDict
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

calib_x = 0
current_x = 0
CIRC = 1516

@app.route('/')
def index():
    return jsonify({'status':'Success'})

@app.route('/mousePos', methods=['POST'])
def mousePos():
    #The value we are gonna get is from 0 - 2
    my_vals = json.loads(request.data)
    x = my_vals['x']

    

    if x < 0:
        x = (1 - math.fabs(x) + 1) / 2.0 
    else:
        x = x / 2.0

    x -= calib_x
    if(x < 0):
        x = 1 + x

    #calib_x is front position
    #current_x is current position
    global current_x
    #x is the target position
    
    #check if moving to the right or left is faster
    midpoint = current_x + .5
    if(midpoint > 1):
        midpoint -= 1

    dx = 0

    if((midpoint - x < .5 and midpoint - x > 0) or (x - current_x < .5 and x - current_x > 0)):
        #move right
        print("Right")
        diff = x - current_x
        if(diff < 0):
            diff = 1 + diff
        
        dx = CIRC * diff

        #print("x: " + str(x) + " cur x: " + str(current_x))
        while dx > 0:
           
            if(dx > 127):
                #print("Moving R 127")
                dx -= 127
                #move right 127
            else:
                #print("Moving R " + str(dx))
                dx -= dx
                #move right dx
        
    else:
        #move left
        print("Left")
        diff = current_x - x
        if(diff < 0):
            diff = 1 + diff
        
        dx = CIRC * diff

        while dx > 0:
            if(dx > 127):
                #print("Moving L 127")
                dx -= 127
                #move 129
            else:
                #print("Moving L " + str(dx))
                dx -= dx
                #move 256 - dx

    current_x = x

    #print(current_x)

    return jsonify({'status':'Mouse has moved'})

@app.route('/calibrate', methods=['POST'])
def calibrate():
    my_vals = json.loads(request.data)
    global calib_x 
    global current_x
    calib_x = my_vals['x']

    if(calib_x < 0):
        calib_x = (1 - math.fabs(calib_x) + 1) / 2.0
    else:
        calib_x /= 2.0

    current_x = calib_x

    #print(current_x)

    return jsonify({"status":"huh"})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
