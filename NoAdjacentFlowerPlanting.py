'''
This question was interesting
'''
from collections import defaultdict

def flowers(self,paths,n):
    graph = defaultdict(list)

    for u,v in paths:
        graph[u].append(v)
        graph[v].append(u)

    plant = {i:0 for i in range(1,n+1)}

    for garden in graph:
        pick = set(range(1,5))
        for g in graph[garden]:
            if plant[g] !=0 and plant[g] in pick:
                pick.remove(plant[g])

        plant[garden] = pick.pop()

    return [plant[x] if plant[x]!=0 else 1 for x in range(1,n+1)]