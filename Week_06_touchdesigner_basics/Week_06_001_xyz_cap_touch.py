# Write your code here :-)
# Write your code here :-)
# https://learn.adafruit.com/adafruit-circuit-playground-express/adafruit2-circuitpython-cap-touch

# with midi send


# UNDERSTANDING DOCUMENTATION!



import board
import touchio
import digitalio

import time
import random

import adafruit_lis3dh # import for accelerometer
import busio

import adafruit_simplemath

import math
import neopixel

# print board pins
print(help(board))
# print adafruit_simplemath library to see available functions we might use
print(help(adafruit_simplemath))

#set up accelerometer:
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
accelerometer.range = adafruit_lis3dh.RANGE_8_G


# for buttons on circuit playground
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonB = digitalio.DigitalInOut(board.BUTTON_B)

# this specifies that the button is a digital input
# pull=digitalio.Pull.DOWN  specifies that it starts OFF, if it is Pull.UP then it starts ON
# since we are using it as a button to turn on an LED when pressed, we start off

buttonA.switch_to_input(pull=digitalio.Pull.DOWN)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)

buttonA_state = False
buttonB_state = False

# store 0 for false, 1 for true for buttons
butA = 0;
butB = 0;

counter = -1

#  setup for digital inputs

#  NeoPixel setup
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.02, auto_write=False)

#  setup for digital inputs

inputs = [touchio.TouchIn(board.A1), touchio.TouchIn(board.A2), touchio.TouchIn(board.A3), touchio.TouchIn(board.A4), touchio.TouchIn(board.A5), touchio.TouchIn(board.A6), touchio.TouchIn(board.TX)]


#  NeoPixel colors
col1 = (0, 255, 0)
col2 = (0, 255, 255)
col3 = (0, 0, 255)
col4 = (100, 0, 255)
col5 = (30, 130, 255)
col6 = (100, 0, 0)
col7 = (120, 0, 55)


#  debounce states for inputs
state_A1 = False
state_A2 = False
state_A3 = False
state_A4 = False
state_A5 = False
state_A6 = False
state_TX = False


#  array of NeoPixel colors
colors = [col1, col2, col3, col4, col5, col6, col7]


#  array of input states
input_states = [state_A1, state_A2, state_A3, state_A4, state_A5, state_A6, state_TX]
input_binary = [0,0,0,0,0,0,0]


#threshold for when to turn on:
threshold = 600


while True:


    x,y,z = accelerometer.acceleration

    # map the accelerometer range from 0 -10 to 0 - 1 (normalize the values)
    x = adafruit_simplemath.map_range(x, -10, 10, 0, 1)
    y = adafruit_simplemath.map_range(y, -10, 10, 0, 1) # have mapped 127 to 0 because my board is upside down
    z = adafruit_simplemath.map_range(z, -10, 10, 0, 1)


    # https://arduinogetstarted.com/tutorials/arduino-button-debounce
    # maybe only print out values if there has been a significant change in the accelerometer
    #     print(time.time()) use this as millis() in arduino


        #  iterate through inputs and MIDI notes
    for i in range(len(input_states)):
        #  reset the state of the input
        #  after the input is released

#         print(inputs[0].raw_value, inputs[1].raw_value,inputs[2].raw_value,inputs[3].raw_value,inputs[4].raw_value,inputs[5].raw_value)
        if (inputs[i].raw_value > threshold) and (input_states[i]):

            input_binary[i] = 1
            input_states[i] = False

        #  if an input is pressed...
        if not inputs[i].value and not input_states[i]:
            input_binary[i] = 0
            #  update input state
            input_states[i] = True


    print(input_binary[0],input_binary[1],input_binary[2],input_binary[3],input_binary[4],input_binary[5],input_binary[6], x, y, z)

    time.sleep(0.1)



# Write your code here :-)
