
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


## assign color by pixel[0-9] = (r,g,b)


var = 100

if var == 200:
   print("1 - Got a true expression value")
   print(var)
elif var == 150:
   print("2 - Got a true expression value")
   print(var)
else:
   print("3 - Got a false expression value")
   print(var)


# ------------------------------------------------------------

## 2.1: Comparison operators  == , <= , >=, != , <, >
## https://www.tutorialspoint.com/python/comparison_operators_example.htm

if var <= 100:
    print("var is less than or equals: ")

if var != 100:
    print("var does not equal value: ")


# ------------------------------------------------------------
## 2.2 _ Python Logical Operators# Write your code here :-)

## and,  or



# ------------------------------------------------------------

## 2.3 # True False

class_is_fun = True

if(class_is_fun):
    print("YAY. Class is fun")
else:
    print("This shit is tiring my brain. I need a coffee.")
