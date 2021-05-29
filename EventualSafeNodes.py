'''
In this question we just have to detect a cycle, it is done using dfs
'''
from collections import defaultdict

def safeNodes(self,graph):
    color = defaultdict(int)
    white,gray,black =0,1,2

    def dfs(node):
        if color[node] != white:
            return color[node] == black

        color[node] = gray
        for ni in graph[node]:
            if color[ni] == black:
                continue
            
            if color[ni]==gray or not dfs(ni):
                return False
        color[node] =  black
        return True

    return filter(dfs, range(len(graph)))