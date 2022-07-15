
# Week 01 A:

# OUR FIRST PROGRAM


# this is a print statement, it will print whatever is inside the parenthesis into the serial monitor
# click Serial in Mu editor to see it print, hit save to run the program or command S.

print("------------")
print("Hello World!")
print("Hello World")
print("Hi everyone, My name is Kai. You've take the first step towards a lot of pain and debugging!")

# this is a comment, the code will not execute. Useful for organizing and making notes for yourself and others reading your code

# now let's start working with the Circuit Playground Bluefruit which we will call CPB for short in this class.

#first we need to import some libraries, which are external code with functions we can use

import board
import time
import neopixel

# the help() function will show all the names of the sensors on the board
print(help(board))


# here are the documentation if you ever want to check...https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.02, auto_write=True)

#

while True:
    # assign a RGB value to it
    pixels[1] = (220,20,100)

    # delays for 1 second
    time.sleep(0.1)

    # assign a RGB value to it , in this case (0,0,0) which is black or in the case of an LED is OFF.
    pixels[1] = (0,0,0)

    #delay for another second
    time.sleep(0.1)

