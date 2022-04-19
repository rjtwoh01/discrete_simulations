import random
import matplotlib.pyplot as plt
import numpy as np
from progress import printProgressBar

class Employee:
    def __init__(self):
        self.computer = Computer()
        self.messages = []


class Computer:
    def __init__(self):
        self.infectedCount = 0
        self.recovered = False

def simulation():
    employeeCount = int(input('enter the number of employees: '))
    simulationCount = int(input('enter the number of times to run the simulation: '))
    dayCount = int(input('enter the number of days each simulation should run: '))

    innerCounter = 0
    infectedComputers = []
    dayCounter = dict()
    recoveriesPerDay = dict()
    totalInfectionsAtDay = dict()
    progressTotal = simulationCount * employeeCount * dayCount
    printProgressBar(0, progressTotal, prefix = 'Progress:', suffix = 'Complete', length = 50)

    for counter in range(0,simulationCount):
        employeeList = list()
        infectedComputers = []
        for i in range(0, employeeCount):
            employeeList.append(Employee())

        #randomly select one of the employees to be case zero
        employeeIndex = random.randint(0, len(employeeList) - 1)
        employeeList[employeeIndex].computer.infectedCount = 1
        for day in range(0,dayCount):
            todaysInfected = 0
            todaysRecovered = 0
            for employee in employeeList:
                #open existingMessages
                # print(employee.messages)
                for message in employee.messages:
                    #you can only get infected once per day
                    infectedThisTime = False
                    infectionTransmission = random.randint(0, 100)
                    if message == 'virus' and not infectedThisTime and infectionTransmission < 40 and not employee.computer.recovered:
                        employee.computer.infectedCount += 1
                        todaysInfected += 1
                        if employee.computer.infectedCount > 2:
                            todaysRecovered += 1
                            employee.computer.recovered = True
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

                innerCounter += 1
                printProgressBar(innerCounter, progressTotal, prefix = 'Progress:', suffix = 'Complete', length = 50)
            if day in dayCounter:
                dayCounter[day] += todaysInfected
                recoveriesPerDay[day] += todaysRecovered
                totalInfectionsAtDay[day] += len(infectedComputers)
            else:
                dayCounter[day] = todaysInfected
                recoveriesPerDay[day] = todaysRecovered
                totalInfectionsAtDay[day] = len(infectedComputers)
    
    # print('total number of computers infected:', len(infectedComputers))
    return (dayCounter, simulationCount, recoveriesPerDay, totalInfectionsAtDay)

dayCounter, simulationCount, recoveriesPerDay, totalInfectionsAtDay = simulation()

for day in dayCounter:
    dayCounter[day] = dayCounter[day] / simulationCount

days = dayCounter.keys()
infections = dayCounter.values()

plt.plot(days, infections)
plt.title('Average infections per day')
plt.xlabel('Day')
plt.ylabel('Infections')

plt.figure(2)

for day in recoveriesPerDay:
    recoveriesPerDay[day] = recoveriesPerDay[day] / simulationCount

days = recoveriesPerDay.keys()
recoveries = recoveriesPerDay.values()
plt.plot(days, recoveries)
plt.title('Average recoveries per day')
plt.xlabel('Day')
plt.ylabel('Recoveries')

plt.figure(3)

for day in totalInfectionsAtDay:
    totalInfectionsAtDay[day] = totalInfectionsAtDay[day] / simulationCount

days = totalInfectionsAtDay.keys()
cases = totalInfectionsAtDay.values()
plt.plot(days, cases)
plt.title('Average Cases at day')
plt.xlabel('Day')
plt.ylabel('Case Count')


plt.show()