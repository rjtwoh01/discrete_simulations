import math
import time

class RNG(object):
    def __init__(self):
        #The default seed, assuming the user doesn't provide one, will be the current system time in seconds
        self.seed = time.time()
        self.a = 69069
        self.c = 1
        self.prevValue = 0

    def rand(self):
        #m_(i+1) = a * m_(i) + c mod(M) 
        newRandomNumber = self.a * self.prevValue + self.c * math.modf()
        return newRandomNumber