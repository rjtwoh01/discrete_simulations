import time
from rng import random_uniform_sample, lcg

interval = int(input('Input the interval to find pi: '))

circlePoints = 0
squarePoints = 0
valuesOfPi = []
seed = time.time()

for i in range(interval**2):
    rus = random_uniform_sample(2, [-1, 1], seed)
    randX = rus[0]
    randY = rus[1]
    seed += 2


    originDistance = randX**2 + randY**2

    if (originDistance <= 1):
        circlePoints += 1
    
    squarePoints += 1

    pi = 4 * circlePoints / squarePoints
    valuesOfPi.append(pi)
    print(pi)

print('Interval range:', interval, ", with total iterations:", interval**2)
print('Final estimation of Pi=', pi)