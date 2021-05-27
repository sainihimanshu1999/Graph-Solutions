'''
we have to reconstruct directed graph iternary in lexicrographical order
'''
from collections import defaultdict

def itenary(self,ticeks):

    graph = defaultdict(list)
    for u,v in ticeks:
        graph[u].append(v)


    for u in graph.keys():
        graph[u].sort(reverse=True)

    stack = []
    res = []
    stack = ['JFK']

    while stack:
        element = stack[-1]
        if element in graph and len(graph[element])>0:
            stack.append(graph[element].pop())

        else:
            res.append(stack.pop())

    return res[::-1]