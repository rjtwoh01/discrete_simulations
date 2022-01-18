import math
from operator import truediv
import struct
import time
import random

# import numpy as np
# import matplotlib.pyplot as plt

#This program should accept initial parameters such as:
#Ship A (target ship):
#       -Speed
#       -Initial Position
#Ship B (chasing ship):
#       -Speed
#       -Initial Position

#To calculate the distance between the two ships in three dimensional space will be done with the formula
# d = sqrt(x^2 + y^2 + z^2)
# Where x, y, z are the coordinates in a cartesian 3-D plane

#Initial variables are to be supplied by the user
class Coordinates(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def setCoordinates(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Ship(object):
    def __init__(self):
        self.speed = 0
        self.coordinates = Coordinates()

    def printPosition(self):
        print('(', self.coordinates.x, ',', self.coordinates.y, ',', self.coordinates.z, ')')

    def updatePosition(self):
        self.coordinates.setCoordinates((self.coordinates.x + (self.speed / 3)), (self.coordinates.y + (self.speed / 3)), (self.coordinates.z + (self.speed / 3)))

# shipA = {
#     speed = 0,
#     initialPosition = {
#         x: 0,
#         y: 0,
#         z: 0
#     }
# }

def tick(seconds):
    time.sleep(seconds)

def main():
    shipA = Ship()
    shipB = Ship()

    shipA.speed = int(input('Input the speed for Ship A: '))
    ax = int(input("Input Ship A's x coordinate: "))
    ay = int(input("Input Ship A's y coordinate: "))
    az = int(input("Input Ship A's z coordinate: "))
    shipA.coordinates.setCoordinates(ax,ay,az)

    shipB.speed = int(input('Input the speed for Ship B: '))
    bx = int(input("Input Ship B's x coordinate: "))
    by = int(input("Input Ship B's y coordinate: "))
    bz = int(input("Input Ship B's z coordinate: "))
    shipB.coordinates.setCoordinates(bx,by,bz)

    chaseInProgress = True
    caught = False
    counter = 0

    totalPossibleLength = random.randrange(25, 10000001)

    while (chaseInProgress):
        print("Ship A position: ")
        shipA.printPosition()
        print("Ship B position: ")
        shipB.printPosition()

        shipA.updatePosition()
        shipB.updatePosition()

        #d = sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
        distance = math.sqrt(((shipA.coordinates.x - shipB.coordinates.x) ** 2) + ((shipA.coordinates.y - shipB.coordinates.y) ** 2) + ((shipA.coordinates.z - shipB.coordinates.z) ** 2))

        if distance <= 150:
            chaseInProgress = False
            caught = True

        tick(1)
        counter = counter + 1

        if (counter >= totalPossibleLength): chaseInProgress = False

    print("Ship A final position: ")
    shipA.printPosition()
    print("Ship B final position: ")
    shipB.printPosition()

    if caught:
        print("Ship B caught ship A after", counter, "seconds")
    else:
        print("Ship A got away after ", counter, "seconds")

if __name__ == "__main__":
    main()