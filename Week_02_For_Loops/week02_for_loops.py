# WEEK 2   09/27/22 For Loops Introduction!!!

# Week 01 A:

# OUR FIRST PROGRAM


# this is a print statement, it will print whatever is inside the parenthesis into the serial monitor
# click Serial in Mu editor to see it print, hit save to run the program or command S.


# this is a comment, the code will not execute. Useful for organizing and making notes for yourself and others reading your code

# now let's start working with the Circuit Playground Bluefruit which we will call CPB for short in this class.

#first we need to import some libraries, which are external code with functions we can use

import board
import time
import neopixel

# the help() function will show all the names of the sensors on the board
print(help(board))


# here are the documentation if you ever want to check...https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

numPixels = 10
r = 0



pixels = neopixel.NeoPixel(board.NEOPIXEL, numPixels, brightness=0.9, auto_write=True)

# RGB 0 - 255





red = (255, 0, 0)
magenta = (210,140,235)
off = (0, 0, 0)
blue = (0, 0, 255)

timeOn = 0.02
timeOff = 0.02


#

while True:
    print("TEST")
    time.sleep(1)

    #comments

    # use a hash  symbol to make a comment
    #  or highlight what you want to comment out and hit cmd K

    # variables and naming conventions for python, use underscores.
    ## my_variable = "something"


    # what is a for loop :
    # To loop through a set of code a specified number of times, we can use the range() function,
    # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
    # and ends at a specified number.

    # -----------------------------------------------------

    ## example 1: counting incrementally
    ## turning all leds on at once:

#     for i in range(numPixels):
#         print(i)
#         time.sleep(0.5)

#     print("exited for loop")



    # ----------------------------------
    ## example 1 with lights

#     for i in range(numPixels):
#         pixels[i] = magenta
#         time.sleep(0.5)

    # -----------------------------------

    ## EXCERCISE: write a for loop to turn off the lights
    ## write your code below:





    # -----------------------------------------------
    ## example 2 Useful to loop through something quickly without having to repeat writing the code over and over

#     for i in range(numPixels):
#         pixels[i] = red

#     time.sleep(timeOn * 0.1)

#     for i in range(numPixels):
#         pixels[i] = magenta

#     time.sleep(timeOff * 0.1)


    #------------------------------------------------


    ## EXCERCISE #2 A: Write a for loop that turns all the pixels on and then off , cycle through 3 different colors and then OFF
    ################ B: THEN => starting from off , cycle through each pixel one by one turning them on one at a time until all LEDS are on,
    ##################then  C: turn off one at a time until all lights are off

   #  write code below:





   ##----------------------------------------------------

   ## Example #3 For Loops Continued
#    for x in range(0,numPixels, 2):
#        print(x)
#        time.sleep(1)


    ## ----------------------------------------------------
    ## EXCERCISE : Turn on even pixels all at once for n amount of time, then when turning off even pixels, turn on odd pixels, then turn off odd pixels



    ## -----------------------------------------------------------
    ## Incremental Operators
     ###                       +=   -=    *=

#     for i in range(0,numPixels):
#         pixels[i] = (r, 0, 100)

#     time.sleep(0.001)
#     r+=1







