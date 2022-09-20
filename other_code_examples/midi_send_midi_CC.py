# https://learn.adafruit.com/adafruit-circuit-playground-express/adafruit2-circuitpython-cap-touch

# with midi send



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

#  setup for digital inputs

inputs = [touchio.TouchIn(board.A1), touchio.TouchIn(board.A2), touchio.TouchIn(board.A3), touchio.TouchIn(board.A4), touchio.TouchIn(board.A5), touchio.TouchIn(board.A6), touchio.TouchIn(board.TX)]




#  debounce states for inputs
state_A1 = False
state_A2 = False
state_A3 = False
state_A4 = False
state_A5 = False
state_A6 = False
state_TX = False


#  array of MIDI notes, change to whatever notes you want to send
midi_notes = [60, 62, 63, 65, 67, 72, 74]
#  array of input states
input_states = [state_A1, state_A2, state_A3, state_A4, state_A5, state_A6, state_TX]


#threshold for when to turn on:
threshold = 400

while True:

    if not buttonA.value and not buttonA_state:
        counter+=1
        buttonA_state = True
    if buttonA.value and buttonA_state:
        buttonA_state = False





    x,y,z = accelerometer.acceleration

    # i only want absolute value
    x = abs(x)
    y = abs(y)
    z = abs(z)

    # map the accelerometer range from 0 - 10 to 0 -127 for midi CC
    x = adafruit_simplemath.map_range(x, 0, 10, 0, 127)
    y = adafruit_simplemath.map_range(y, 0, 10, 127, 0) # have mapped 127 to 0 because my board is upside down
    z = adafruit_simplemath.map_range(z, 0, 10, 0, 127)

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



    #  iterate through inputs and MIDI notes
    for i in range(len(input_states)):
        #  reset the state of the input and send NoteOff msg
        #  after the input is released

#         print(inputs[0].raw_value, inputs[1].raw_value,inputs[2].raw_value,inputs[3].raw_value,inputs[4].raw_value,inputs[5].raw_value)
        if (inputs[i].raw_value > threshold) and (input_states[i]):

            input_states[i] = False

            midi.send(NoteOn(midi_notes[i], 120))


        #  if an input is pressed...
        if not inputs[i].value and not input_states[i]:

            #  send the NoteOn msg
            midi.send(NoteOff(midi_notes[i], 120))
            #  update input state
            input_states[i] = True

    time.sleep(0.1)



