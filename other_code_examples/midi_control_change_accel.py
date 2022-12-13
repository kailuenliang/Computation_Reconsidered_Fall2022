# for nicki_ basic accelerometer code to send midi control messages



import board
import touchio
import digitalio

import time
import random
import usb_midi
import adafruit_midi
import adafruit_lis3dh # import for accelerometer
import busio

import adafruit_simplemath

import math

from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend




#  USB MIDI setup
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)



# midi port print
print(usb_midi.ports)
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

counter = -1


#threshold for when to turn on:
threshold = 400

while True:

    if not buttonA.value and not buttonA_state:
        counter+=1
        buttonA_state = True
    if buttonA.value and buttonA_state:
        buttonA_state = False





    x,y,z = accelerometer.acceleration


    # map the accelerometer range from 0 - 10 to 0 -127 for midi CC
    x = adafruit_simplemath.map_range(x, -10, 10, 0, 127)
    y = adafruit_simplemath.map_range(y, -10, 10, 0, 127) # have mapped 127 to 0 because my board is upside down
    z = adafruit_simplemath.map_range(z, -10, 10, 0, 127)

    # we don't need the floating point numbers,
    x = math.floor(x)
    y = math.floor(y)
    z = math.floor(z)


    # https://arduinogetstarted.com/tutorials/arduino-button-debounce
    # maybe only print out values if there has been a significant change in the accelerometer
    #     print(time.time()) use this as millis() in arduino

    # print((x,y,z))
    midi_map_states = counter % 5

    # 4 states: switches between

    if midi_map_states == 0:

        print("CC XYZ-ALL")
        midi.send(ControlChange(3, x))
        midi.send(ControlChange(4, y))
        midi.send(ControlChange(5, z))

    elif midi_map_states == 1:
        print("CC X")
        midi.send(ControlChange(3, x))
    elif midi_map_states == 2:
        midi.send(ControlChange(4, y))
        print("CC Y")
    elif midi_map_states == 3:
        midi.send(ControlChange(5, z))
        print("CC Z")
    else:
        print("no midi cc")
        # put some kind of indicator here, a LED etc.




    time.sleep(0.1)


