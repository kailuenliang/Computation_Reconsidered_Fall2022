# potentiometer example
# based off this
# https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/potentiometer


import time

import analogio
import board

potentiometer = analogio.AnalogIn(board.A1)


#     Then we have the get_voltage() helper function. By default, analog readings will range from 0 (minimum) to 65535 (maximum).
#     This helper will convert the 0-65535 reading from pin.value and convert it a 0-3.3V voltage reading.

def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:

    # this is just to demo how many volts
#
    # print((get_voltage(potentiometer),))

    # here is the potentiometer normalized to 0-1 floating point value , 65536 is the maximum number of a 16 bit signal


    pot_norm = potentiometer.value / 65536
    if(pot_norm < 0.01):
        pot_norm = 0.0

    print(pot_norm)


    time.sleep(0.1)
