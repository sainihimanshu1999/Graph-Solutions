'''
here we have to connect maximum number of roads connected to a singel node
'''
from collections import defaultdict

def maximalRank(self,roads,m):
    graph = defaultdict(set)
    for u,v in roads:
        graph[u].append(v)
        graph[v].append(u)

    rank = 0
    for i in range(m):
        for j in range(1+1,m):
            rank = max(rank, len(graph[i])+len(graph[j]) - (i in graph[j]))
    return rank