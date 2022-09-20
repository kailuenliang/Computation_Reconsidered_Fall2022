# Write your code here :-)
# https://learn.adafruit.com/adafruit-circuit-playground-express/adafruit2-circuitpython-cap-touch

# with midi send


# UNDERSTANDING DOCUMENTATION!



import board
import touchio

import neopixel

import time
import random

import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend


#  USB MIDI setup
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)



# midi example
print(usb_midi.ports)




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


#  array of MIDI notes CHANGE TO WHAT YOU WANT:
midi_notes = [60, 62, 63, 65, 67, 72, 74]

#  array of input states
input_states = [state_A1, state_A2, state_A3, state_A4, state_A5, state_A6, state_TX]


#threshold for when to turn on:
threshold = 600

while True:

    #  iterate through colors, inputs and MIDI notes
    for i in range(len(input_states)):
        #  reset the state of the input and send NoteOff msg
        #
#         print(inputs[0].raw_value, inputs[1].raw_value,inputs[2].raw_value,inputs[3].raw_value,inputs[4].raw_value,inputs[5].raw_value)
        if (inputs[i].raw_value > threshold) and (input_states[i]):

            input_states[i] = False
            #midi.send(NoteOff(midi_notes[i], 120))
            midi.send(NoteOn(midi_notes[i], 120))
            pixels.fill(colors[i])
            pixels.show()

        #  if an input is released
        if not inputs[i].value and not input_states[i]:
            #  change thhe colors of the NeoPixels

            #  send the NoteOff msg
            midi.send(NoteOff(midi_notes[i], 120))
            #  update input state
            input_states[i] = True

    time.sleep(0.01)



