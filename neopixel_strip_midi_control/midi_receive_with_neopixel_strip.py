# Write your code here :-)

import board
import neopixel
import time
import touchio


print(help(board))




import busio
import usb_midi
import adafruit_midi
import displayio
import terminalio

from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn



# if want to use onboard led lights
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=True)

# for led strip
strip_pixel = neopixel.NeoPixel(board.A1, 30)

# define colors

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


oled_reset = board.D1



# ---------  midi setup --------------#
print(usb_midi.ports)
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0
)

msg = midi.receive()

# list of midi notes that you are checking for as input
midi_notes_r = [36, 38, 40, 41, 43, 45, 47]
colors = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

# ---------  TIME duration --------------#

bpm_val = 118.0


# make a function to calculate 8th note based on bpm!!!!
def bpm():
    """ function returns time of 32nd note"""

    note = (60/bpm_val)/32
    print(f"a 32nd note of {bpm_val} bpm is {note} seconds")
    return note



def solid(t, col):
    """
    args: t (float) : time of delay in seconds
          col(string) : color of pixel
    """
    for i in range(30):
        strip_pixel[i] = col
        time.sleep(t)


def other(t, col, mod):
    """
    args: t (float) : time of delay in seconds
          col(string) : color of pixel
          mod (int): modulo...every other n pixel
    """
    for i in range(30):
        if( i % mod == 0):
            strip_pixel[i] = col
        else:
            strip_pixel[i] = OFF
        time.sleep(t)



def follow(t, col):
    strip_pixel[0] = col
    for i in range(29):
        if(i < 28):
            strip_pixel[i] = OFF
            strip_pixel[i+1] = col
        else:
            strip_pixel[i] = OFF
        time.sleep(t)
    for i in range(29, 0, -1):
        if(i < 29):
            strip_pixel[i] = OFF
            strip_pixel[i-1] = col
        else:
            strip_pixel[i] = OFF
        time.sleep(t)


def offState():
    for i in range(30):
        strip_pixel[i] = OFF



on_time = bpm() # in seconds

while True:
    #  receive midi messages
    msg = midi.receive()

    if msg is not None:
        #  if a NoteOn message...
        if isinstance(msg, NoteOn):
            string_msg = 'NoteOn'
            string_val = msg.note
            print(msg.note)

            if string_val == midi_notes_r[0]:
                solid(0.0, GREEN)

            if string_val == midi_notes_r[1]:
                solid(0.0, BLUE)
#                 for i in range(len(pixels)):
#                    pixels[i] = colors[1]
            if string_val == midi_notes_r[2]:
                other(0.0, WHITE, 4)
                # for i in range(len(pixels)):
#                    pixels[i] = colors[2]
            if string_val == midi_notes_r[3]:
                other(0.0, YELLOW, 2)
#                 for i in range(len(pixels)):
#                    pixels[i] = colors[3]
            if string_val == midi_notes_r[4]:
                other(on_time, WHITE, 4)
                # for i in range(len(pixels)):
#                    pixels[i] = colors[4]
            if string_val == midi_notes_r[5]:
                other(on_time, CYAN, 1)
#                 for i in range(len(pixels)):
#                    pixels[i] = colors[5]
            if string_val == midi_notes_r[6]:
                follow(on_time, PURPLE)
#                 for i in range(len(pixels)):
#                    pixels[i] = colors[6]



        #  if a NoteOff message...
        if isinstance(msg, NoteOff):
            string_msg = 'NoteOff'
            #  get note number
            string_val = str(msg.note)

            offState()



