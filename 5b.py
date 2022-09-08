from sense_hat import SenseHat 
import time
import random
sense = SenseHat()

sense.clear()

green = (0,255,0)
yellow = (255,255,0)

colors = [green, yellow]
#function to return random orientation
def randOrientation():
    orientations = [0,90,180,270]
    return orientations[random.randint(0,3)]



#outer loop determines no. of times set of color switch occurs
#inner loop determines the color and orientation changes each time
def switchColor(colors, times):
    for i in range(0, times):
        for color in colors:
            #set random orientation
            sense.set_rotation(randOrientation())
            #let y be the colored pixel
            y = color
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


switchColor(colors, 3)

sense.clear()



