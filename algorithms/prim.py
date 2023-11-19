from heapq import heappush
from heapq import heappop

# connected undirected graph
# element -> [  (weight, neighbor), (weight, neighbor) ]
adjList = {
    5: [(5, 7), (3, 3), (4, 6)],
    3: [(3, 5), (7, 8), (2,2), (1,1)],
    7: [(5, 5)],
    6: [(4, 5), (2, 2)],
    8: [(7, 3), (3, 9)],
    2: [(2, 3), (5, 1), (2, 6)],
    1: [(5, 2), (1, 3), (1, 9)],
    9: [(1, 1), (3, 8)]
}

startingNode = 3
result = 0
visited = set([startingNode])
priorityQueue = []

for neighbor in adjList[startingNode]:
    heappush(priorityQueue, neighbor)

while priorityQueue:
    if priorityQueue[0][1] in visited:
        heappop(priorityQueue)
        continue
    
    minWeight, node = heappop(priorityQueue)
    result += minWeight
    visited.add(node)

    for neighbor in adjList[node]:
        # would work without this check because
        # we are checking for visited, at the start anyways
        # but we might save some space and time by 
        # checking here as well
        if neighbor not in visited:
            heappush(priorityQueue, neighbor)


print(result)





