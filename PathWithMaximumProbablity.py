'''
In this question we used dijkstra algorithm with maximum heap to get the path with maximum probablity
'''
from collections import defaultdict
from heapq import *

def maxProb(self,start,end,succProb,edges):
    graph = defaultdict(list)
    prob = defaultdict(list)

    for i,(u,v) in enumerate(edges):
        graph[u].append(v)
        graph[v].append(u)
        prob[u,v]=prob[v,u]=succProb[i]

    maxHeap = [(-1,start)]
    visited = set()

    while maxHeap:
        pr,node = heappop(maxHeap)
        if node == end: return -pr

        for ni in graph.get(node,[]):
            if ni in visited: continue
            heappush(maxHeap,(pr*prob.get((node,ni),0), ni))

    return 0
