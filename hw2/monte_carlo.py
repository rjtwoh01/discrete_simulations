import math
import random
import rng

#shipA.speed = int(input('Input the speed for Ship A: '))
interval = int(input('Input the interval to find pi: '))

circlePoints = 0
squarePoints = 0
valuesOfPi = []

for i in range(interval**2):
    randX = random.uniform(-1,1)
    randY = random.uniform(-1,1)


    originDistance = randX**2 + randY**2

    if (originDistance <= 1):
        circlePoints += 1
    
    squarePoints += 1

    pi = 4 * circlePoints / squarePoints
    # valuesOfPi.append(pi)
    print(pi)

print('Final estimation of Pi=', pi)
# print('total iterations:', len(valuesOfPi))
