import time
from rng import random_uniform_sample, lcg
import matplotlib
matplotlib.use("TkAgg") # set the backend (to move the windows to desired location on screen)
import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
from matplotlib.pyplot import *
import numpy as np
import distutils


def plot(i, isFirst1, isFirst2, circleX, circleY, squareX, squareY, circlePoints, totalPoints, piValueI, totalDropsArray):
    #taken and modified from: https://www.bragitoff.com/2021/05/value-of-pi-using-monte-carlo-python-program/
    if i%100==0:
        # Draw on first window
        plt.figure(1)
        # The label is only needed once so 
        if isFirst1:
                
            # Plot once with label
            plt.scatter(circleX,circleY,c='blue',s=50,label='Drop inside')
            isFirst1 = False
            plt.legend(loc=(0.75, 0.9))
        else:
            #Remaining plot without label
            plt.scatter(circleX,circleY,c='blue',s=50)
        # Draw on first window
        plt.figure(1)
        # The label is only needed once so 
        if isFirst2:
            # Plot once with label
            plt.scatter(squareX,squareY,c='orange',s=50,label='Drop outside')
            isFirst2 = False
            plt.legend(loc=(0.75, 0.9))
        else:
            #Remaining plot without label
            plt.scatter(squareX,squareY,c='orange',s=50)
            
            
        area = 4*circlePoints/totalPoints
        plt.figure(1)
        plt.title('No. of pin drops = '+str(totalPoints)+';         No. inside circle = '+str(circlePoints)+r';         π  ≈ $4\frac{N_\mathrm{inside}}{N_\mathrm{total}}=$ '+str(np.round(area,6)))
        piValueI.append(area)
        totalDropsArray.append(totalPoints)
        # For plotting on the second window
        plt.figure(2)
        plt.axhline(y=np.pi, c='darkseagreen',linewidth=2,alpha=0.5)
        plt.plot(totalDropsArray,piValueI,c='mediumorchid')
        plt.title('π estimate vs no. of pin drops')
        plt.annotate('π',[0,np.pi],fontsize=20)
        # The following command is needed to make the second window plot work.
        plt.draw()
        # # Pause for animation
        plt.pause(0.00000001)

    return (piValueI, totalDropsArray, isFirst1, isFirst2)


def main():
    interval = int(input('Input the interval to find pi: '))
    drawPlot = distutils.util.strtobool(input('Draw a plot?: '))
    radius = 1

    if drawPlot:
        fig = figure(figsize=(8, 8), dpi=120)

    circlePoints = 0
    squarePoints = 0
    totalPoints = 0
    valuesOfPi = []
    seed = time.time()
    count = 0

    # First matplotlib window
    if drawPlot:
        fig1 = plt.figure(1)
        plt.get_current_fig_manager().window.wm_geometry("+00+00") # move the window
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.legend()

        # Second matplotlib window
        plt.figure(2)
        plt.get_current_fig_manager().window.wm_geometry("+960+00") # move the window
        # plt.ylim(2.8,4.3)

        isFirst1 = True
        isFirst2 = True

    circleX = []
    circleY = []
    squareX = []
    squareY = []

    piValueI = []
    totalDropsArray = []

    for i in range(interval**2):
        rus = random_uniform_sample(2, [-1, 1], seed)
        randX = rus[0]
        randY = rus[1]
        seed += 2

        originDistance = randX**2 + randY**2

        if (originDistance <= 1):
            circlePoints += 1
            circleX.append(randX)
            circleY.append(randY)
        else:
            squarePoints += 1
            squareX.append(randX)
            squareY.append(randY)

        totalPoints += 1

        if (drawPlot): 
            piValueI, totalDropsArray, isFirst1, isFirst2 = plot(i, isFirst1, isFirst2, circleX, circleY, squareX, squareY, circlePoints, totalPoints, piValueI, totalDropsArray)

        pi = 4 * circlePoints / totalPoints
        print(pi)

    print('Interval range:', interval, ", with total iterations:", interval**2)
    print('Final estimation of Pi=', pi)

    if drawPlot:
        plt.draw()
        plt.show()

if __name__ == "__main__":
    main()