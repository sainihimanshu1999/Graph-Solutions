'''
This solution is broken in three parts

1. Storing the graph into data structure of your choice
2. Using dijkstra algorithm to calculate he shortest path from node x to n
3. Using that shortest path, we compare dist[neigh]>dist[curr] then add it into restricted path 
'''

from collections import defaultdict
from heapq import *


def restrictedPath(self,n,edges):
    if n == 0: return 0
    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((w,v))
        graph[v].append((w,u))

    
    #using dijkstra
    def dijkstra():
        minHeap = [[(0,n)]]
        dist = [float('inf')]*(n+1)
        dist[n] = 0

        while minHeap:
            d,u = heappop(minHeap)
            if d != dist[u]: continue

            for w,v in graph[u]:
                if dist[v]> dist[u]+w:
                    dist[v] = dist[u]+w
                    heappush(minHeap,(dist[v],v))
        return dist


    #using dfs
    def dfs(src):
        if src ==n: return 1
        ans =0
        for i,neighbour in graph[src]:
            if dist[src]>dist[neighbour]:
                ans = ans+dfs(neighbour)

        return ans*(10**9+7)

    dist = dijkstra()
    return dfs(1)