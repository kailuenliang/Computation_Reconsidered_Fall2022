# Write your code here :-)



# ----------------------IMPORT LIBRARIES --------------------------------

import board
import touchio
import digitalio
import analogio
import array
import audiobusio


import time
import random

import adafruit_lis3dh # import for accelerometer
import busio

import adafruit_simplemath
import math
import neopixel
import adafruit_thermistor



# print board pins
print(help(board))
# print adafruit_simplemath library to see available functions we might use
print(help(adafruit_simplemath))

# SETUP --------------------------------------------------------------------
#------------------------------------------------------------------

#  NeoPixel setup
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.9, auto_write=True)

# variable to light sensor-----------------------------------------
light = analogio.AnalogIn(board.LIGHT)

# thermistor
thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

# ------------------------- RELAY CODE -------------------------

rel = digitalio.DigitalInOut(board.A1)
rel.direction = digitalio.Direction.OUTPUT



#  NeoPixel colors
col1 = (0, 255, 0)
col2 = (0, 255, 255)
col3 = (0, 0, 255)
col4 = (100, 0, 255)
col5 = (30, 130, 255)
col6 = (100, 0, 0)
col7 = (120, 0, 55)


#  array of NeoPixel colors
colors = [col1, col2, col3, col4, col5, col6, col7]


# setup for sound sensor-------------------------------------------:
# functions for sound stuff-----------------------------------------------------------------------:

# Restrict value to be between floor and ceiling.
def constrain(value, floor, ceiling):
    return max(floor, min(value, ceiling))

# Scale input_value between output_min and output_max, exponentially.
def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / \
                             (input_max - input_min)
    return output_min + \
        math.pow(normalized_input_value, SCALE_EXPONENT) \
        * (output_max - output_min)

# Remove DC bias before computing RMS.
def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(samples_sum / len(values))

def mean(values):
    return sum(values) / len(values)

# Exponential scaling factor.
# Should probably be in range -10 .. 10 to be reasonable.
CURVE = 2
SCALE_EXPONENT = math.pow(10, CURVE * -0.1)

# Number of samples to read at once.
NUM_SAMPLES = 160

# https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/playground-sound-meter
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,sample_rate=16000, bit_depth=16)
# RECORDS A QUICK BIT OF SOUND_ WHAT IT SHOULD SOUND LIKE AT LOWEST VOLUME
samples = array.array('H', [0] * NUM_SAMPLES)
mic.record(samples, len(samples))
# Set lowest level to expect, plus a little.
input_floor = normalized_rms(samples) + 10
# OR: used a fixed floor
# input_floor = 50



## -------------VARIABLES ---------------------------------------




audio_threshold = 500
counter = 0
num_pixels = 10

red = (155, 0 , 0)
green = (0, 100, 0 )
blue = (0, 0, 200 )
off = (0, 0, 0)


## ----------------------PROGRAM ------------------------------------------------------
## -------------------------------------------------------------

while True:


# # SOUND SENSOR ------------------------------------------------------------------
    mic.record(samples, len(samples))
    audio_level = normalized_rms(samples)
    # print(audio_level)

#     rel.value = True
#     time.sleep(1.0)
#     rel.value = False
#     time.sleep(0.5)
    print(audio_level)
    if audio_level > 1000:
        rel.value = True
        time.sleep(2)
    else:
        rel.value = False







# -LIGHT SENSOR-----------------------------------------------------------------

    ## light.value is what is storing our light sensor value ...this is not normalized from 0-1 in the code :
    # print(light.value)

# -----------------TEMPERATURE ---------

    # temp_c = thermistor.temperature
#     temp_f = thermistor.temperature * 9 / 5 + 32
#     print(temp_f)





    time.sleep(0.01)



# Write your code here :-)
