#x = 0
#y = True
#while y:
#	if x <20;
#		x+=1
#	elif x == 20:
#		y = False

import time
x = 0
y = 0
z = 0
count = 0

while True:
	count+=1
	for i int range(10):
		# x+=1 is the same as x=x+1
		x=10+ x
		y=15 +y
		z=20+ z
		if y%20 == 0:
			x = 0
			z = 15
		time.sleep(0.5)
		if x >= 255 or y >= 255 or z>= 255:
			x = 0
			y = 0
			z == 0
	if count >= 10:
		break




