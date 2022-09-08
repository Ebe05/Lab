from sense_hat import SenseHat 
import time
import random
sense = SenseHat()

sense.clear()

green = (0,255,0)
red = (255,0,0)

#generate random orientation
def randOrientation():
    orientations = [0,90,180,270]
    return orientations[random.randint(0,3)]

#function that switches to randome orientation
def switchOrient(color):   
    orientation = randOrientation()    
    sense.set_rotation(orientation)
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
    return orientation 


timer = 3
count = 0
while True:
    orientation = switchOrient(green)
    time.sleep(timer)
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'])
    y = round(acceleration['y'])
    if x == -1 and orientation == 0:
        timer = timer*0.95
        count = count + 1
    elif y == -1 and orientation == 90:
        timer = timer*0.95
        count = count + 1
    elif x == 1 and orientation == 180:
        timer = timer*0.95
        count = count + 1
    elif y == 1 and orientation == 270:
        timer = timer*0.95
        count = count + 1
    else:
        switchOrient(red)
        time.sleep(2)
        sense.clear()
        sense.show_message("Successful trials: ")
        sense.show_message(str(count))
        break

sense.clear()


