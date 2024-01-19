from collections import deque

def bfs(adjList, startNode):
    queue = deque([startNode])
    visited = set([startNode])

    while queue:
        popped = queue.popleft()
        print(popped)

        for neighbor in adjList[popped]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


# undirected connected graph
edges = [
    [1,2],
    [0,2],
    [0,1],
    [2,4],
    [3,5],
    [5,2],
    [7,6],
    [6,5],
    [3,7],
]


adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = set([])

    adjList[src].add(dst)

    if dst not in adjList:
        adjList[dst] = set([])

    adjList[dst].add(src)

bfs(adjList, edges[0][0])