from heapq import heappush 
from heapq import heappop

def dijkstra(adj, source):
    # since nodes are labeled from 0 to n list idxes are used as node values
    result = [float("inf")] * len(adj) 
    
    heap = [(0, source)]
    
    while heap:
        nodeWeight, nodeVal = heappop(heap)
        # we dont need to add neighbors of same node, we will just add redundant nodes with longer paths
        if result[nodeVal] != float("inf"):
            continue
        
        result[nodeVal] = nodeWeight
        # I can check if i found all shortest paths and break this loop early
        # there might be the case, where i find all the paths and there are some elements in heap
        
        for neighborVal, neighborWeight in adj[nodeVal]:
            # there is no need to add neighbor for which we already found the path
            # since we are doing this like bfs, we are guaranteed that, the path we found before, is less than the path we 
            # will be adding now
            # why? because if this path was shorter, we would have gone through this path earlier
            # we didn't choose this path, because it was longer than the other path, and that shorter path lead us to this neighbor
            if result[neighborVal] == float("inf"):
                heappush(heap, (neighborWeight + nodeWeight, neighborVal))
    
    return result

graph = [
    [[2,1], [1,5]],
    [[0, 2], [2, 3]],
    [[0, 2], [1, 2]]
]

source = 0
res = dijkstra(graph, source)
print(res)