
# Week 02 Intro to Conditional Statements

# import our libraries
import board
import time
import neopixel


## 1) Lets look at the if else diagram:
# https://www.educba.com/if-else-in-python/

## here are the documentation if you ever want to check...https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

## just copy this, its long
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=True)


### Part 1:
### https://www.geeksforgeeks.org/relational-operators-in-python/

### try defining a few variables and using the relational operators and see what prints

a = 10
b = 20

# returns a boolean value (True or  False)
print(a < b)

# >

# ==

# !=

#  <=

#  >=

## Part 2: Conditional Statements

# kai = True
# this_class = "fun"
# a = 20

# if this_class == "fun":
#     print("coding can be fun!")

# if a < 100:
#     print("This is true ... do something here!")

## ------------ if elif else  ------------------------

# if a > 100:
#     print("if")
# elif a > 50:
#     print("elif")
# elif a > 15:
#     print("second elif")
# else:
#     print("none are true")



## ------------------------- Part 3 Logical operators -----------------

## and

isSunday = True
isHoliday = True

if isHoliday and isSunday:
    print('Sunday is a Funday!!')
else:
    print('Not holiday!! Boss is on your ass to start working :(')

## or

isGalleryNight = True
amTooTipsy = True

if isGalleryNight and not amTooTipsy:
    print("Keep having fun looking and supporting each other's art.")
elif isGalleryNight and amTooTipsy:
    print("Maybe you should go home and relax")
elif not isGalleryNight:
    print("its not gallery night, its only Monday")
else:
    print("Not sure what day it is.")




