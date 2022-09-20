# Write your code here :-)

import board
import busio
import usb_midi
import adafruit_midi
import displayio
import terminalio

from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend

import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=True)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


oled_reset = board.D1



#  midi setup
print(usb_midi.ports)
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0
)

msg = midi.receive()

# list of midi notes that you are checking for as input
midi_notes_r = [36, 38, 40, 41, 43, 45, 47]
colors = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

while True:
    #  receive midi messages
    msg = midi.receive()

    if msg is not None:
        #  if a NoteOn message...
        if isinstance(msg, NoteOn):
            string_msg = 'NoteOn'
            #  get note number
            #string_val = str(msg.note)
            string_val = msg.note
            print(msg.note)

            if string_val == midi_notes_r[0]:
                for i in range(len(pixels)):
                   pixels[i] = colors[0]
            if string_val == midi_notes_r[1]:
                for i in range(len(pixels)):
                   pixels[i] = colors[1]
            if string_val == midi_notes_r[2]:
                for i in range(len(pixels)):
                   pixels[i] = colors[2]
            if string_val == midi_notes_r[3]:
                for i in range(len(pixels)):
                   pixels[i] = colors[3]
            if string_val == midi_notes_r[4]:
                for i in range(len(pixels)):
                   pixels[i] = colors[4]
            if string_val == midi_notes_r[5]:
                for i in range(len(pixels)):
                   pixels[i] = colors[5]
            if string_val == midi_notes_r[6]:
                for i in range(len(pixels)):
                   pixels[i] = colors[6]



        #  if a NoteOff message...
        if isinstance(msg, NoteOff):
            string_msg = 'NoteOff'
            #  get note number
            string_val = str(msg.note)

            for i in range(len(pixels)):
                pixels[i] = OFF



