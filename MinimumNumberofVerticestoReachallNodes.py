'''
it's a directed graph and if we don't have any way to reach this node(not having any inward connections),
then this node must be added into the answer
'''

def verticesNode(self,edges,n):
    answer = set(range(n))
    for i,j in edges:
        if j in answer:
            answer.remove(j)

    return list(answer)