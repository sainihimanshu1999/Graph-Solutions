'''
Topological sort or BFS in graph is used
'''

def minimalHeight(self,n,edges):
    tree = [set() for i in range(n)]
    for u,v in edges:
        edges[u].add[v]
        edges[v].add[u]

    q = [x for x in range(n) if len(tree[x])<2]
    level = []

    while True:
        for x in q:
            for y in tree[x]:
                tree[y].remove(x)
                if len(tree[y])==1: level.append(y)

        if not level: break
        level,q=[],level

    return q