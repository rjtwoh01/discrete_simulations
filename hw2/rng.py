import math
import time

def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x

def random_uniform_sample(n, interval, seed = time.time()):
    a, c, m = 1103515245, 12345, 2 ** 31
    #seed = 1644260284.448245
    bsdrand = lcg(seed, a, c, m)

    lower, upper = interval[0], interval[1]
    sample = []

    for i in range(n):
        observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower
        # sample.append(round(observation))
        sample.append(observation)

    return sample

def main():
    rus = random_uniform_sample(30, [-1, 1])
    print(rus)

if __name__ == "__main__":
    main()