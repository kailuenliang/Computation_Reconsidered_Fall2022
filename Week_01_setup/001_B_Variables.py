
# Week 01 B:

# Introduction to variables


#import the libraries we need

import board
import time
import neopixel

# the help() function will show all the names of the sensors on the board
print(help(board))


# here are the documentation if you ever want to check...https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

# So whats a variable ?
# A variable is a way of referring to a storage area in a computer program.
# This memory location holds values—numbers, text or more complicated types of data

#lets use a variable to store the brightness :
bright_val = 0.1

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=bright_val, auto_write=True)

# lets store some more variables:

color_01 = (255,0,0)
color_02 = (0,255,0)
color_03 = (0,0,255)
color_off = (0,0,0)

# a value for the speed of the blink
b_speed = 0.5


# !!!!! In python, the indentation is very very important!

while True:
    pixels[0] = color_01
    pixels[1] = color_02
    pixels[2] = color_03
    time.sleep(b_speed)

    pixels[0] = color_03
    pixels[1] = color_01
    pixels[2] = color_02
    time.sleep(b_speed)

    pixels[0] = color_02
    pixels[1] = color_03
    pixels[2] = color_01
    time.sleep(b_speed)




