from distutils.command.build import build
from operator import indexOf
import random

class Building(object):
    def __init__(self):
        self.floors = [1, 2, 3, 4]
        self.floorPositions = [0, 60, 90, 105]
        self.peopleWaiting = list()
        self.elevator = None #defined later


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
                # if (person.destinationFloor < 4): print(person.destinationFloor)
                # print('adjusting nearestfloor')
                nearestFloor = person.destinationFloor

        # print(nearestFloor)
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

    while currentTime < 3600: #an hour
        dieRoll = random.randint(1,101)
        if (dieRoll < 10): #chance of a person arriving at the building
            newPerson = Person()
            newPerson.getDestination()
            building.peopleWaiting.append(newPerson) #add the person to the queue

        while (len(elevator.occupants) < elevator.capacity and len(building.peopleWaiting) > 0 and elevator.currentPosition == 0):
            print('elevator occupants:',len(elevator.occupants))
            print('building occupants:',len(building.peopleWaiting))
            elevator.occupants.append(building.peopleWaiting.pop(0)) #remove person that arrived first and put them on the elevator
            currentTime += 1
            # print('elevator occupants:',len(elevator.occupants))
            # print('building occupants:',len(building.peopleWaiting))

        if len(elevator.occupants) == elevator.capacity:
            for person in building.peopleWaiting:
                takingStairs = person.determineIfLeave()
                if takingStairs: building.peopleWaiting.remove(person) #if the person is taking the stairs then remove them from the queue
        
        #move the elevator up
        if len(elevator.occupants) > 0:
            nearestFloor = elevator.getNearestFloor()
            # print(nearestFloor)

            if  elevator.currentPosition not in building.floorPositions or elevator.currentPosition == 0:
                # print('elevator current position is not in the designated floor posistions')
                elevator.currentPosition += 1
                currentTime += 1
            
            # print(elevator.currentPosition)
            if elevator.currentPosition in building.floorPositions:
                elevator.currentFloor = building.floorPositions.index(elevator.currentPosition) + 1
                
                print('arriving at floor: ', elevator.currentFloor)
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
                    print('at top floor', len(elevator.occupants))
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
            print('waiting for people at position:', elevator.currentPosition)

    print('hour elapsed')
    print('elevator occupants:',len(elevator.occupants))
    print('building occupants:',len(building.peopleWaiting))



def main():
    simulationCount = int(input('Enter how many times to run the simulation: '))
    counter = 0

    while counter < simulationCount:
        simulation()
        counter +=1 


if __name__ == "__main__":
    main()