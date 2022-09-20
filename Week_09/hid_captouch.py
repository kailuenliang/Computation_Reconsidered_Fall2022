# Write your code here :-)
# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Circuit Playground HID Keyboard

import time



# code to control a game engine using capacitive touch using w,a,s,d

import touchio

import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull


touchA1 = touchio.TouchIn(board.A1)
touchA2 = touchio.TouchIn(board.A2)
touchA3 = touchio.TouchIn(board.A3)
touchA4 = touchio.TouchIn(board.A4)


# MAKE SURE BUTTONS AND KEYS ARE IN THE SAME POSITION OF THE LIST
buttons = [touchA1, touchA2, touchA3, touchA4]
# The keycode sent for each button, will be paired with a control key
buttonkeys = [Keycode.W, Keycode.S,Keycode.A,Keycode.D]

# the keyboard object!
# sleep for a bit to avoid a race condition on some systems
time.sleep(1)
kbd = Keyboard(usb_hid.devices)
# we're americans :)
layout = KeyboardLayoutUS(kbd)



print("Waiting for button presses")

while True:
    # check each button
    # when pressed, the LED will light up,
    # when released, the keycode or string will be sent
    # this prevents rapid-fire repeats!
    for button in buttons:
        if button.value:  # pressed?
            i = buttons.index(button)
            while button.value:
                pass  # wait for it to be released!
            # type the keycode or string
            keytyped = buttonkeys[i]  # get the corresponding keycode or string
            if isinstance(keytyped, str):
                layout.write(keytyped)
            else:
                kbd.press(keytyped)  # press...
                kbd.release_all()  # release!


    time.sleep(0.01)
