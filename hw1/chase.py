import math
from operator import truediv
import struct
import time
import random

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

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
        self.theta = 0
        self.alpha = 0
        self.magnitude = 0
    
    def setCoordinates(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

class Ship(object):
    def __init__(self):
        self.speed = 0
        self.coordinates = Coordinates()
        self.laserSpread = 0
        self.thrusterLikelihood = 0
        self.history = [Coordinates()]

    def printPosition(self):
        print('(', "{:.2f}".format(self.coordinates.x), ',', "{:.2f}".format(self.coordinates.y), ',', "{:.2f}".format(self.coordinates.z), ')')

    def increaseDistance(self):
        self.coordinates.setCoordinates((self.coordinates.x + (self.speed / 3)), (self.coordinates.y + (self.speed / 3)), (self.coordinates.z + (self.speed / 3)))

    def decreaseDistance(self):
        self.coordinates.setCoordinates((self.coordinates.x - (self.speed / 3)), (self.coordinates.y - (self.speed / 3)), (self.coordinates.z - (self.speed / 3)))

    def calculateTheta(self):
        self.coordinates.theta = np.arctan(self.coordinates.x / self.coordinates.y)

def calculateTheta(shipA: Ship, shipB: Ship):
    theta = math.degrees(np.arctan((shipA.coordinates.x - shipB.coordinates.x) / (shipA.coordinates.y - shipB.coordinates.y)))
    return theta

# α = arccos[(a · b) / (|a| * |b|)]
def calculateAlpha(shipA: Ship, shipB: Ship):
    dotProduct = (shipA.coordinates.x * shipB.coordinates.x) + (shipA.coordinates.y * shipB.coordinates.y) + (shipA.coordinates.y * shipB.coordinates.y)
    difference = (shipA.coordinates.x - shipB.coordinates.x) + (shipA.coordinates.y - shipB.coordinates.y) + (shipA.coordinates.z - shipB.coordinates.z)
    alpha = math.degrees(np.arctan((dotProduct) / calculateDistance(shipA, shipB)))
    # print()
    return alpha

def calculateDistance(shipA: Ship, shipB: Ship):
    #d = sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
    distance = math.sqrt(((shipA.coordinates.x - shipB.coordinates.x) ** 2) + ((shipA.coordinates.y - shipB.coordinates.y) ** 2) + ((shipA.coordinates.z - shipB.coordinates.z) ** 2))
    return distance

def tick(seconds):
    time.sleep(seconds)

def main():
    shipA = Ship()
    shipB = Ship()

    shipA.speed = int(input('Input the speed for Ship A: '))
    ax = int(input("Input Ship A's x coordinate: "))
    ay = int(input("Input Ship A's y coordinate: "))
    az = int(input("Input Ship A's z coordinate: "))
    thrustorOdds = int(input("Input Ship A's chance to find a thrustor (1-99): "))
    shipA.coordinates.setCoordinates(ax,ay,az)
    shipA.thrusterLikelihood = thrustorOdds

    shipB.speed = int(input('Input the speed for Ship B: '))
    bx = int(input("Input Ship B's x coordinate: "))
    by = int(input("Input Ship B's y coordinate: "))
    bz = int(input("Input Ship B's z coordinate: "))
    laser = int(input("Input Ship B's laser spread (degrees): "))
    shipB.coordinates.setCoordinates(bx,by,bz)
    shipB.laserSpread = laser

    chaseInProgress = True
    caught = False
    counter = 0

    #The total time that shipB will be able to chase shipA
    #Ranges from 30 seconds to 1 hour
    totalPossibleLength = random.randrange(30, 3601)

    shipAThrustorsRemaining = 0

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.autoscale(enable=True, axis='both', tight=True)
    
    while (chaseInProgress):
        print("Ship A position: ")
        shipA.printPosition()
        print("Ship B position: ")
        shipB.printPosition()

        shipA.history.append(shipA.coordinates)
        shipB.history.append(shipB.coordinates)

        shipA.increaseDistance()
        if (shipAThrustorsRemaining > 0):
            shipA.increaseDistance()
            shipAThrustorsRemaining = shipAThrustorsRemaining - 1
            print('ShipA used a thrustor with', shipAThrustorsRemaining, 'remaining')
        
        if random.randrange(0,100) > 10:
            if shipB.coordinates.x > shipA.coordinates.x or shipB.coordinates.y > shipA.coordinates.y or shipB.coordinates.z > shipA.coordinates.z:
                shipB.decreaseDistance()
            else:
                shipB.increaseDistance()
        else:
            print('ShipB encountered an astroid and is stuck for the next second')
                

        
        if random.randrange(0,100) < shipA.thrusterLikelihood and shipAThrustorsRemaining == 0:
            shipAThrustorsRemaining = random.randrange(1, 6)
            print("ShipA found a thrustor pack with", shipAThrustorsRemaining, "thrustors")
        
        
        distance = calculateDistance(shipA, shipB)
        alpha = calculateAlpha(shipA, shipB)

        print('The distance between the two is', "{:.2f}".format(distance), 'with an angle alpha of', "{:.2f}".format(alpha), 'degrees')
        print('')
        print('-----------------------------------------------------------------------------')
        print('')
        
        ax.scatter3D(shipA.coordinates.x, shipA.coordinates.y, shipA.coordinates.z, color='green')
        ax.scatter3D(shipB.coordinates.x, shipB.coordinates.y, shipB.coordinates.z, color='red')

        plt.show(block=False)
        plt.pause(1)

        if distance <= 50 and alpha <= shipB.laserSpread:
            chaseInProgress = False
            caught = True
        else:
            ax.scatter3D(shipA.coordinates.x, shipA.coordinates.y, shipA.coordinates.z, color='white')
            ax.scatter3D(shipB.coordinates.x, shipB.coordinates.y, shipB.coordinates.z, color='white')
            plt.pause(0.01)

        counter = counter + 1

        

        if (counter >= totalPossibleLength): chaseInProgress = False

    print("Ship A final position: ")
    shipA.printPosition()
    print("Ship B final position: ")
    shipB.printPosition()

    distance = calculateDistance(shipA, shipB)

    if caught:
        print("Ship B caught ship A after", counter, "seconds; with distance of", "{:.2f}".format(distance), "meters between them")
    else:
        print("Ship A got away after ", counter, "seconds")

    plt.show()

if __name__ == "__main__":
    main()