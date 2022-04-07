import random
import matplotlib.pyplot as plt

# Start node: [ {Destination Nodes : Travel Time}] where travel time = constant OR tuple
def getGraph():
    graph = {
        1: {2: (3, 5), 5: 6},
        2: {3: 6, 4: (7, 9)},
        3: {4: (5, 8)},
        4: {7: 4},
        5: {3: 7, 4: 9, 6: (7, 10)},
        6: {7: (8, 12)}
    }
    return graph;

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


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

# print(find_all_paths(graph, 1, 7))
traversalTime = []
print(getGraph())
count = 0
simulationCount = int(input('Enter how many times to run the simulation: '))
printProgressBar(0, simulationCount, prefix = 'Progress:', suffix = 'Complete', length = 50)
runs = []
pathList = find_all_paths(getGraph(), 1, 7)

innerPathDistances = {
    1: {2: 0, 5: 0},
    2: {3: 0, 4: 0},
    3: {4: 0},
    4: {7: 0},
    5: {3: 0, 4: 0, 6: 0},
    6: {7: 0}
}

while count < simulationCount: 
    runGraph = dict()
    runGraph.update(getGraph()) #shallow copy, values only
    #get distance for all indeterministic paths
    for i in runGraph:
        for j in runGraph[i]:
            if type(runGraph[i][j]) == tuple:
                values = (runGraph[i][j])
                runGraph[i][j] = random.randrange(values[0], values[1])

    # print(runGraph)
    run = []
    #traverse getting total distances for the whole path
    for path in pathList:
        parentNode = path[0]
        pathDistances = []
        for node in path:
            if node != 1 & parentNode != 7:
                graphNode = runGraph[parentNode]
                value = graphNode[node]
                count = 1
                newDistanceValue = value
                if type(innerPathDistances[parentNode][node]) == tuple:
                     count = innerPathDistances[parentNode][node][1] + 1
                     newDistanceValue = innerPathDistances[parentNode][node][0] + value
                innerPathDistances[parentNode][node] = (newDistanceValue, count)
                pathDistances.append(value)
                parentNode = node
        run.append(pathDistances)
    runs.append(run)
    count += 1
    printProgressBar(count, simulationCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

# print(runs)

pathResults = []
pathDistances = [0, 0, 0, 0, 0]
for run in runs:
    innerSums = []
    counter = 0
    for path in run:
        innerSums.append(sum(path))
        pathDistances[counter] += sum(path)
        counter += 1
    pathResults.append(innerSums)

# print(pathResults)
print(pathDistances)
# for results in pathResults:
#     counter = 0
#     for distance in results:

for i in range(len(pathDistances)):
    pathDistances[i] = round(pathDistances[i] / simulationCount, 2)

print(pathDistances)
print(innerPathDistances)

for i in innerPathDistances:
    for j in innerPathDistances[i]:
        innerPathDistances[i][j] = round(innerPathDistances[i][j][0] / (innerPathDistances[i][j][1]), 2)

print(innerPathDistances)

x = []
for path in pathList:
    pathString = "("
    for element in path:
        pathString += str(element) 
        if element != path[-1]: 
            pathString += ", "
    pathString += ")"
    x.append(pathString)
print(x)
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, pathDistances)
plt.title('Average distance for paths')
plt.xlabel('Path')
plt.ylabel('Distance')
plt.xticks(x_pos, x)

plt.show()