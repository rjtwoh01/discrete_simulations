import random
import matplotlib.pyplot as plt
import numpy as np

class Employee:
    def __init__(self):
        self.computer = Computer()
        self.messages = []


class Computer:
    def __init__(self):
        self.infectedCount = 0

def simulation():
    employeeCount = int(input('enter the number of employees: '))
    simulationCount = int(input('enter the number of times to run the simulation: '))
    dayCount = int(input('enter the number of days each simulation should run: '))
    counter = 0
    infectedComputers = []

    for counter in range(0,simulationCount):
        employeeList = list()
        for i in range(0, employeeCount):
            employeeList.append(Employee())

        #randomly select one of the employees to be case zero
        employeeIndex = random.randint(0, len(employeeList) - 1)
        employeeList[employeeIndex].computer.infectedCount = 1
        for day in range(0,dayCount):
            for employee in employeeList:
                #open existingMessages
                print(employee.messages)
                for message in employee.messages:
                    #you can only get infected once per day
                    infectedThisTime = False
                    infectionTransmission = random.randint(0, 100)
                    if message == 'virus' and not infectedThisTime and infectionTransmission < 40:
                        employee.computer.infectedCount += 1
                        infectedThisTime = True
                        if employee.computer not in infectedComputers:
                            infectedComputers.append(employee.computer)
                    employee.messages.remove(message)

                #send out new messages
                messagesSent = []
                #once a computer has been infected twice it will no longer forward the virus
                messageContents = "virus" if 1 <= employee.computer.infectedCount <= 2 else "normal"
                while len(messagesSent) < 3:
                    employeeIndex = random.randint(0, len(employeeList) - 1)
                    if (employeeIndex not in messagesSent) & (employeeIndex != employeeList.index(employee)):
                        messagesSent.append(employeeIndex)
                        employeeList[employeeIndex].messages.append(messageContents)
    
    print('total number of computers infected:', len(infectedComputers))

simulation()