from distutils.command.build import build
from operator import indexOf
import random
import datetime
import matplotlib.pyplot as plt
import numpy as np

class Building(object):
    def __init__(self):
        self.floors = [1, 2, 3, 4]
        self.floorPositions = [0, 60, 90, 105]
        self.peopleWaiting = list()
        self.waitTimeList = []
        self.walksToFloors = [0, 0, 0] #how many people go to the first, second, and third floors
        self.workersAtTimeBlocks = [0, 0, 0] #8:30, 8:45, 9:00
        self.lastBoardTime = 0
        self.averageWaitTime = 0
        self.elevator = None #defined later

    def addToWaitTime(self, timeValue):
        for person in self.peopleWaiting:
            person.waitTime += timeValue


class Elevator(object):
    def __init__(self):
        self.currentFloor = 1 #(G, 2, 3, 4) where G = 1
        self.currentPosition = 0
        self.travelTimeToNextFloor = [0, 1, .5, .25]
        self.occupants = list()
        self.capacity = 12

    def getNearestFloor(self):
        nearestFloor = 4
        for person in self.occupants:
            if person.destinationFloor < nearestFloor: 
                nearestFloor = person.destinationFloor
        return nearestFloor

    def exitElevator(self):
        for person in self.occupants:
            if person.destinationFloor == self.currentFloor: self.occupants.remove(person)

class Person(object):
    def __init__(self):
        self.currentFloor = 1
        self.destinationFloor = 0
        self.waitTime = 0

    def getDestination(self):
        self.destinationFloor = random.randint(2, 5)

    #Returns true if the person leaves and walks
    #Returns false if they decide to ride the elavator
    def determineIfLeave(self):
        chanceOfLeave = 0
        if self.destinationFloor == 2: chanceOfLeave = 50
        elif self.destinationFloor == 3: chanceOfLeave = 33
        elif self.destinationFloor == 4: chanceOfLeave = 10

        dieRoll = random.randint(0, 101)

        if dieRoll < chanceOfLeave: return True
        else: return False

def simulation():
    building =  Building()
    elevator = Elevator()
    currentTime = 0 #Measured in seconds
    building.elevator = elevator
    lastTimeCheck = 0

    while currentTime < 3600: #an hour
        building.addToWaitTime(currentTime - lastTimeCheck)
        lastTimeCheck = currentTime
        dieRoll = random.randint(1,101)
        if (dieRoll < 10): #chance of a person arriving at the building
            newPerson = Person()
            newPerson.getDestination()
            building.peopleWaiting.append(newPerson) #add the person to the queue

        while (len(elevator.occupants) < elevator.capacity and len(building.peopleWaiting) > 0 and elevator.currentPosition == 0):
            building.waitTimeList.append(building.peopleWaiting[0].waitTime)
            elevator.occupants.append(building.peopleWaiting.pop(0)) #remove person that arrived first and put them on the elevator
            currentTime += 1

        if len(elevator.occupants) == elevator.capacity:
            for person in building.peopleWaiting:
                takingStairs = person.determineIfLeave()
                building.waitTimeList.append(person.waitTime)
                if takingStairs:
                    floorIndex = building.floors.index(person.destinationFloor - 1) #get the index of the floor the person is going to, shifted for array
                    building.walksToFloors[floorIndex] += 1
                    building.peopleWaiting.remove(person) #if the person is taking the stairs then remove them from the queue
        
        #move the elevator up
        if len(elevator.occupants) > 0:
            nearestFloor = elevator.getNearestFloor()

            if  elevator.currentPosition not in building.floorPositions or elevator.currentPosition == 0:
                elevator.currentPosition += 1
                currentTime += 1
            
            if elevator.currentPosition in building.floorPositions:
                elevator.currentFloor = building.floorPositions.index(elevator.currentPosition) + 1
                
                if elevator.currentFloor == nearestFloor and elevator.currentFloor != 4:
                    elevator.exitElevator()
                    currentTime += 30
                    elevator.currentPosition += 1
                    if len(elevator.occupants) == 0:
                        currentTime += elevator.currentPosition
                        elevator.currentPosition = 0
                elif elevator.currentFloor == 4:
                    elevator.exitElevator() 
                    #Adjust for travel back down to the bottom
                    elevator.currentFloor = 1
                    elevator.currentPosition = 0
                    currentTime += 145 #doors stay open for 30 seconds and then travel back down time
                else:
                    elevator.currentPosition += 1
                    currentTime += 1
        elif elevator.currentPosition != 0 and elevator.currentPosition != 105:
            currentTime += elevator.currentPosition 
            elevator.currentPosition = 0
        else: 
            currentTime += 1 #we're waiting for people to show up and need the elevator

    return building

# Print iterations progress
#Src: https://stackoverflow.com/a/34325723
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def main():
    simulationCount = int(input('Enter how many times to run the simulation: '))
    counter = 0
    buildingList = list()
    averageWaitTimesList = []

    printProgressBar(0, simulationCount, prefix = 'Progress:', suffix = 'Complete', length = 50)
    while counter < simulationCount:
        building = simulation()
        buildingList.append(building)
        counter +=1
        printProgressBar(counter, simulationCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

    print('ran: {0} times', counter)
    averageWaitTime = 0
    numberOfPeople = 0
    averageWalksToSecond = []
    averageWalksToThird = []
    averageWalksToFourth = []
    for building in buildingList:
        averageWaitTime += sum(building.waitTimeList)
        building.averageWaitTime = sum(building.waitTimeList) / len(building.waitTimeList)
        averageWaitTimesList.append(building.averageWaitTime)
        numberOfPeople += len(building.waitTimeList)
        averageWalksToSecond.append(building.walksToFloors[0])
        averageWalksToThird.append(building.walksToFloors[1])
        averageWalksToFourth.append(building.walksToFloors[2])

    averageWaitTime = averageWaitTime / numberOfPeople

    averageWalksToSecondSum = sum(averageWalksToSecond) / simulationCount
    averageWalksToThirdSum = sum(averageWalksToThird) / simulationCount
    averageWalksToFourthSum = sum(averageWalksToFourth) / simulationCount

    walkingList = [averageWalksToSecondSum, averageWalksToThirdSum, averageWalksToFourthSum]

    print('average wait time:', str(datetime.timedelta(seconds=int(averageWaitTime))))

    plt.figure(1)
    plt.plot(list(range(1, simulationCount + 1)), averageWaitTimesList)
    plt.title('Average Wait Times for Buildings (seconds)')
    plt.xlabel('Building')
    plt.ylabel('Avg Wait Time')

    plt.figure(2)
    plt.plot([2, 3, 4], walkingList)
    plt.title('Average People Walking, n = ' + str(simulationCount))
    plt.xlabel('Floors')
    plt.ylabel('People Walking')
    plt.show()


if __name__ == "__main__":
    main()