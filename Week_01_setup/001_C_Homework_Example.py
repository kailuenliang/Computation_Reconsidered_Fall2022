
# Week 01 C:

# Homework Assignment Example


# import our libraries
import board
import time
import neopixel



# here are the documentation if you ever want to check...https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

# just copy this, its long
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=True)

#

# our infinite loop

while True:
    pixels[0] = (178,132,190)

    time.sleep(1)

    pixels[0] = (0,0,0)
    pixels[1] = (123,200,34)
    pixels[3] = (32,32,100)

    time.sleep(1)

    pixels[1] = (0,0,0)
    pixels[3] = (0,0,0)
    time.sleep(0.5)

    pixels[9] = (120,0,0)
    pixels[8] = (54,30,100)
    time.sleep(0.1)

    pixels[9] = (0,0,0)
    pixels[8] = (0,0,0)
    time.sleep(0.1)

    pixels[0] = (255,255,255)
    time.sleep(0.1)

    pixels[0] = (0,0,0)
    time.sleep(0.1)

    pixels[1] = (255,255,255)
    time.sleep(0.1)

    pixels[1] = (0,0,0)
    time.sleep(0.1)

    pixels[2] = (255,255,255)
    time.sleep(0.1)

    pixels[2] = (0,0,0)
    time.sleep(0.1)

    pixels[3] = (255,255,255)
    time.sleep(0.1)

    pixels[3] = (0,0,0)
    time.sleep(0.1)

    pixels[4] = (255,255,255)
    time.sleep(0.1)

    pixels[4] = (0,0,0)
    time.sleep(0.1)

    pixels[5] = (255,255,255)
    time.sleep(0.1)

    pixels[5] = (0,0,0)
    time.sleep(0.1)


