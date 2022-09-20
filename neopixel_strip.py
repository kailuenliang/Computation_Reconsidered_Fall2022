import board
import neopixel
import time

import touchio

print(help(board))



pixel = neopixel.NeoPixel(board.A1, 30)


touchA2 = touchio.TouchIn(board.A2)
touchA4 = touchio.TouchIn(board.A4)
touchA5 = touchio.TouchIn(board.A5)
touchA6 = touchio.TouchIn(board.A6)


# define colors

white = (255,255,255)
off = (0, 0, 0)
blue = (0, 0, 255)
color3 = (30, 0, 20)
color4 = (0, 255, 0)
color5 = (0,255,255)

on_time = 0.05 # in seconds

def state01():
    for i in range(30):
        pixel[i] = white

        time.sleep(on_time)

def state02():
    for i in range(30):
        pixel[i] = blue
        time.sleep(on_time)
    for i in range(30):
        pixel[i] = off
        time.sleep(on_time)

def state03():

    for i in range(30):
        if( i % 3 == 0):
            pixel[i] = color3
        else:
            pixel[i] = color4
        time.sleep(on_time/2)

    for i in range(30):
        if( i % 2 == 0):
            pixel[i] = off
        else:
            pixel[i] = color3
        time.sleep(on_time*3)

    for i in range(30):
        pixel[i] = off
        time.sleep(on_time)

def state04():
    for i in range(30):
        if( i % 2 == 0):
            pixel[i] = color5
        else:
            pixel[i] = color4
        time.sleep(on_time * 4)
    for i in range(30):
        if( i % 3 == 0):
            pixel[i] = color3
        else:
            pixel[i] = off
        time.sleep(on_time * 4)

def follow():
    pixel[0] = white
    for i in range(29):
        if(i < 28):
            pixel[i] = off
            pixel[i+1] = white
        else:
            pixel[i] = off
        time.sleep(on_time)
    for i in range(29, 0, -1):
        if(i < 29):
            pixel[i] = off
            pixel[i-1] = white
        else:
            pixel[i] = off
        time.sleep(on_time)




def offState():
    for i in range(30):
        pixel[i] = off


while True:
    #print(touchA2.value)
    if touchA2.value:
        print("a2 touched")
        state01()
    elif touchA4.value:
        print("touched")
        state02()
    elif touchA5.value:
        state03()
    elif touchA6.value:
        follow()
    else:
        offState()







# Write your code here :-)
