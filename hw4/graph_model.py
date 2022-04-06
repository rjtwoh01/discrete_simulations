import random

# Start node: [ {Destination Nodes : Travel Time}] where travel time = constant OR tuple
graph = {
    1: {2: (3, 5), 5: 6},
    2: {3: 6, 4: (7, 9)},
    3: {4: (5, 8)},
    4: {7: 4},
    5: {3: 7, 4: 9, 6: (7, 10)},
    6: {7: (8, 12)}
}

traversalTimes = {
    '1,2': (3,5),
    '1, 5': (6)
}


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

print(find_all_paths(graph, 1, 7))
traversalTime = []
print(graph)

count = 0
simulationCount = int(input('Enter how many times to run the simulation: '))
printProgressBar(0, simulationCount, prefix = 'Progress:', suffix = 'Complete', length = 50)
while count < simulationCount: 
    pathList = find_all_paths(graph, 1, 7)
    for path in pathList:
        # print(path)
        parentNode = path[0]
        # print(parentNode)
        # nodeIndex = 0
        for node in path:
            if node != 1 & parentNode != 7:
                # graphIndex = list(graph).index(parentNode)
                graphNode = graph[parentNode]
                # print('graphNode:',graphNode)
                # print('parentNode:',parentNode)
                # print('node:',node)
                value = graphNode[node]
                # print('value:',value)
                parentNode = node
            # print('node before update:', node)
    count += 1
    printProgressBar(count, simulationCount, prefix = 'Progress:', suffix = 'Complete', length = 50)
