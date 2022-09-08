from sense_hat import SenseHat 
import time
import random
sense = SenseHat()

sense.clear()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

colors = [red, green, blue, yellow]

sense.clear()

sense.set_pixel(0,0,red)
sense.set_pixel(0,7,blue)
sense.set_pixel(7,7,green)
sense.set_pixel(7,0,yellow)

time.sleep(3)
sense.clear()

def randPixel():
    return random.randint(0,7)

for color in colors:
    sense.set_pixel(randPixel(), randPixel(), color)
    time.sleep(1)

sense.clear()
