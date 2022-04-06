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


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
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
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)

find_path(graph, '1', '7')