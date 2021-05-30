'''
we will use bfs algorithm in this
'''
from collections import defaultdict

def division(self,equations,quereis):

    graph = defaultdict(dict)
    for(u,v), value in zip(equations,quereis):
        graph[u][v] = value
        graph[v][u] = 1/value

    def bfs(src,dest):
        if not src in graph and not dest in graph: return -1.0
        q = [(src,1.0)]
        seen = set()

        for x,v in q:
            if x == dest:
                return v
            for y in graph[x]:
                if y not in seen:
                    q.append((y,v*graph[x][y]))

        return -1.0

    return [bfs(s,d) for s,d in quereis]