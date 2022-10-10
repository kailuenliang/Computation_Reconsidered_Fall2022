# Write your code here :-)
# import our libraries
import board
import time
import digitalio
import neopixel


# defining the buttons
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonB = digitalio.DigitalInOut(board.BUTTON_B)

buttonA.switch_to_input(pull=digitalio.Pull.DOWN)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)



## just copy this, its long
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=True)

while True:

    if buttonA.value and buttonB.value:
        for i in range(10):
            pixels[i] = (100, 20, 200)
            time.sleep(0.1)
            pixels[i] = (0, 0, 0)
            time.sleep(0.1)

    elif buttonA.value:  # button is pushed
        pixels[0] = (255, 0, 0)

    elif buttonB.value:
        pixels[9] = (0, 255, 0)

    else:
        pixels[0] = (0, 0, 0)
        pixels[9] = (0, 0, 0)


    time.sleep(0.01)


