def dfs(adjList, node, visited, ordering):
    if node in visited:
        return
    
    visited.add(node)
    
    for preReq in adjList[node]:
        dfs(adjList, preReq, visited, ordering)
    
    ordering.append(node)



def topologicalSort(edges):
    adjList = {}
    
    for node, preReq in edges:
        if node not in adjList:
            adjList[node] = []
        
        if preReq != None:
            adjList[node].append(preReq)
    


    topologicalOrdering = []
    visited = set([])

    for node in adjList:
        dfs(adjList, node, visited, topologicalOrdering)
    
    return topologicalOrdering
    


# directed acyclic graph
# node, prerequisite node
edges = [
    [2, 6],
    [2, 0],
    [2, 3],
    [6, 9],
    [6, 0],
    [3, 0],
    [3, 7],
    [4, 7],
    [7, 5],
    [0, 5],
    [9, None],
    [5, None],
]


ordering = topologicalSort(edges)
print(ordering)