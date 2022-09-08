from sense_hat import SenseHat 
import time
import random
sense = SenseHat()

sense.clear()

#function to return random orientation
def randOrientation():
    orientations = [0,90,180,270]
    return orientations[random.randint(0,3)]

#function to generate random color
def randColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

#loop determines the color and orientation changes each time
def switchColor(times):
    for i in range(0, times):        
        #set random orientation
        sense.set_rotation(randOrientation())
        #let y be the colored pixel
        y = randColor()
        b = (0, 0, 0)
        image_pixels =	[b, b, b, b, b, b, b, b,
        b, b, b, y, b, b, b, b,
        b, b, y, y, y, b, b, b,
        b, y, b, y, b, y, b, b,
        b, b, b, y, b, b, b, b,
        b, b, b, b, y, b, b, b,
        b, b, b, y, b, b, b, b, 
        b, b, b, b, b, b, b, b]
        sense.set_pixels(image_pixels)
        time.sleep(1)

switchColor(7)

sense.clear()