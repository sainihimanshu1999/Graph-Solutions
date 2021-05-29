'''
This question can be solved by two ways, on is dijkstra and other bfs or shortest path algorithm
'''

#Dijkstra Algo

from collections import defaultdict
from heapq import *
from typing import Deque

def network(self,times,k,n):
    graph = defaultdict(list)

    for u,v,w in times:
        graph[u].append((v,w))

    visited = {}
    q = [(0,k)]

    while q:
        time,node = heappop(q)

        if node not in visited:
            visited[node] = time

            for w,v in graph[node]:
                w = time+w
                heappush(q,(w,v))

    return max(visited.values()) if len(visited) == n else -1


#Shortest Path Fast Algo

def delay(self,times,n,k):
    graph = defaultdict(list)

    for u,v,w in times:
        graph[u].append((v,w))

    q = Deque([(0,k)])
    visited = [0]+[float('inf')]*n

    while q:
        time, node = q.popleft()
        if time<visited[node]:
            visited[node] = time

            for v,w in graph[node]:
                w += time
                q.append((w,v))
    mx = max(visited)
    return mx if mx<float('inf') else -1



    
