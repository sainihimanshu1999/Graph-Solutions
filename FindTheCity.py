'''
we have to use dijkstra theoram for this every time for each city
'''

from collections import defaultdict
from heapq import *


def findCity(self,edges,n, threshold):

    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))

    def dijkstra(city):
        heap = [(0,city)]
        dist = {}

        while heap:
            gap,node = heappop(heap)

            if node in dist: 
                continue
            
            if node!=city:
                dist[node] = gap

            for v,w in graph[node]:
                if v in dist: continue
                if gap+w <= threshold:
                    heappush(heap,(gap+w,v))
        return len(dist)

    return max([(dijkstra(city),city) for city in range(n)],key=lambda x:(-x[0],x[1]))[-1]

