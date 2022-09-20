

import board
import time

import neopixel

# import the library to allow us to use the capacitive touch sensors!

# http://docs.circuitpython.org/en/latest/shared-bindings/touchio/index.html#touchio.TouchIn
import touchio

# here are the documentation if you ever want to check...https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

# just copy this, its long
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=True)

print(help(board))


# define some variables to store our info:
touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_TX = touchio.TouchIn(board.TX)

# lets change the threshold

# touch_A1.threshold = 8000
# touch_A2.threshold = 8000
# touch_A3.threshold = 8000
# touch_A4.threshold = 8000
# touch_A5.threshold = 8000
# touch_A6.threshold = 8000
# touch_TX.threshold = 8000


while True:
    if touch_A1.value:
        print("A1 touched!")
    if touch_A2.value:
        print("A2 touched!")
    if touch_A3.value:
        print("A3 touched!")
    if touch_A4.value:
        print("A4 touched!")
    if touch_A5.value:
        print("A5 touched!")
    if touch_A6.value:
        print("A6 touched!")
    if touch_TX.value:
        print("TX touched!")

    time.sleep(0.01)


