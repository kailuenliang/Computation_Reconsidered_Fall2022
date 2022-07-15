
# Week 01 D:

# Homework Assignment Example With Variables


# import our libraries
import board
import time
import neopixel



# here are the documentation if you ever want to check...https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

# just copy this, its long
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=True)



# whats a variable? We can store values into variable names to make it easier to change later

# store the color values into variables: remember (R,G,B)

violet = (178,132,190)
turq = (77,255,225)

# turn off all the pixels
off = (0,0,0)

# lets store a variable for time so we can change this easily
delay_time = 0.2


# our infinite loop

while True:
    # now lets use our variables
    pixels[0] = violet

    time.sleep(delay_time*10)

    pixels[0] = off
    pixels[1] = turq
    pixels[3] = violet

    time.sleep(delay_time*10)

    pixels[1] = off
    pixels[3] = off
    time.sleep(delay_time)

    pixels[9] = turq
    pixels[8] = violet
    time.sleep(delay_time)

    pixels[9] = off
    pixels[8] = off
    time.sleep(delay_time)

    pixels[0] = violet
    time.sleep(delay_time)

    pixels[0] = (0,0,0)
    time.sleep(delay_time)

    pixels[1] = violet
    time.sleep(delay_time)

    pixels[1] = off
    time.sleep(delay_time)

    pixels[2] = violet
    time.sleep(delay_time)

    pixels[2] = off
    time.sleep(delay_time)

    pixels[3] = violet
    time.sleep(delay_time)

    pixels[3] = off
    time.sleep(delay_time)

    pixels[4] = violet
    time.sleep(delay_time)

    pixels[4] = off
    time.sleep(delay_time)

    pixels[5] = violet
    time.sleep(delay_time)

    pixels[5] = off
    time.sleep(delay_time)


