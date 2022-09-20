
# ALL SENSORS in one piece of code


# https://learn.adafruit.com/adafruit-circuit-playground-express/adafruit2-circuitpython-cap-touch
# UNDERSTANDING DOCUMENTATION!


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

# print board pins
print(help(board))
# print adafruit_simplemath library to see available functions we might use
print(help(adafruit_simplemath))

# SETUP --------------------------------------------------------------------
#------------------------------------------------------------------
#set up accelerometer:
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
accelerometer.range = adafruit_lis3dh.RANGE_8_G

# --------------------------------------------------------------
# for buttons on circuit playground
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonB = digitalio.DigitalInOut(board.BUTTON_B)

# this specifies that the button is a digital input
# pull=digitalio.Pull.DOWN  specifies that it starts OFF, if it is Pull.UP then it starts ON
# since we are using it as a button to turn on an LED when pressed, we start off

buttonA.switch_to_input(pull=digitalio.Pull.DOWN)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)

buttonA_state = False
buttonB_state = False

# store 0 for false, 1 for true for buttons
butA = 0;
butB = 0;

counter = -1

#  setup for digital inputs

#  NeoPixel setup
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.02, auto_write=False)

#  setup for digital inputs

inputs = [touchio.TouchIn(board.A1), touchio.TouchIn(board.A2), touchio.TouchIn(board.A3), touchio.TouchIn(board.A4), touchio.TouchIn(board.A5), touchio.TouchIn(board.A6), touchio.TouchIn(board.TX)]


#  NeoPixel colors
col1 = (0, 255, 0)
col2 = (0, 255, 255)
col3 = (0, 0, 255)
col4 = (100, 0, 255)
col5 = (30, 130, 255)
col6 = (100, 0, 0)
col7 = (120, 0, 55)


#  debounce states for inputs
state_A1 = False
state_A2 = False
state_A3 = False
state_A4 = False
state_A5 = False
state_A6 = False
state_TX = False


#  array of NeoPixel colors
colors = [col1, col2, col3, col4, col5, col6, col7]


#  array of input states
input_states = [state_A1, state_A2, state_A3, state_A4, state_A5, state_A6, state_TX]
input_binary = [0,0,0,0,0,0,0]


#threshold for when to turn on:
threshold = 600

# variable to light sensor-----------------------------------------
light = analogio.AnalogIn(board.LIGHT)

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

while True:


# ACCELEROMETER CODE ----------------------------------------------------------------------------
    x,y,z = accelerometer.acceleration

    # map the accelerometer range from 0 -10 to 0 - 1 (normalize the values)
    x = adafruit_simplemath.map_range(x, -10, 10, 0, 1)
    y = adafruit_simplemath.map_range(y, -10, 10, 0, 1) # have mapped 127 to 0 because my board is upside down
    z = adafruit_simplemath.map_range(z, -10, 10, 0, 1)


    # https://arduinogetstarted.com/tutorials/arduino-button-debounce
    # maybe only print out values if there has been a significant change in the accelerometer
    #     print(time.time()) use this as millis() in arduino


# CAPACITIVE TOUCH CODE ---------------------------------------------------------------------------------

    for i in range(len(input_states)):
        #  reset the state of the input
        #  after the input is released

#         print(inputs[0].raw_value, inputs[1].raw_value,inputs[2].raw_value,inputs[3].raw_value,inputs[4].raw_value,inputs[5].raw_value)
        if (inputs[i].raw_value > threshold) and (input_states[i]):

            input_binary[i] = 1
            input_states[i] = False

        #  if an input is pressed...
        if not inputs[i].value and not input_states[i]:
            input_binary[i] = 0
            #  update input state
            input_states[i] = True


# -LIGHT SENSOR-----------------------------------------------------------------

    # light.value is what is storing our light sensor value ...this is not normalized from 0-1 in the code :


# SOUND SENSOR ------------------------------------------------------------------
    mic.record(samples, len(samples))
    audio_level = normalized_rms(samples)


# BUTTONS ---------------------------------------------------------------------
    if(buttonA.value):
        butA = 1;
    else:
        butA = 0;
    if(buttonB.value):
        butB = 1;
    else:
        butB = 0;

# THIS IS IMPORTANT!!!! THIS IS WHAT IS BEING SENT TO TOUCHDESIGNER, it will be sent as a string of numbers!!!

# PRINT ALL VALUES TO SEND TO TOUCHDESIGNER or wherever -----------------------------------------------------------

    #  (state_A1,state_A2,state_A3,state_A4,state_A5,state_A6,state_TX, X,Y,Z, LIGHT,AUDIO,BUTTONA,BUTTONB
    print(input_binary[0],input_binary[1],input_binary[2],input_binary[3],input_binary[4],input_binary[5],input_binary[6],
    x, y, z,light.value,audio_level, butA, butB)

#     print(input_binary[0],input_binary[1],input_binary[2],input_binary[3],input_binary[4],input_binary[5],input_binary[6],
#     x, y, z,light.value,audio_level, butA, butB)

    time.sleep(0.1)




