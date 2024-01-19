def dfs(adjList, node, visited = None):
    if visited == None: visited = set([])

    if node in visited:
        return
    
    print(node)
    visited.add(node)

    for neighbor in adjList[node]:
        dfs(adjList, neighbor, visited)



# undirected graph
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

dfs(adjList, edges[0][0])
