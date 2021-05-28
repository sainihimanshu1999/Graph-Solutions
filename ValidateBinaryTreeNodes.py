'''
We have to keep two things in mind that binary tree has only n-1 edges and
binary tree every node strictly have one parent only
'''

def validateBinary(self,n,leftChild,rightChild):
    leftEdges = [i for i in leftChild if i != -1]
    rightEdges = [i for i in rightChild if i != -1]

    if leftEdges + rightChild != n-1:
        return False

    parent = [[] for _ in range(n)]

    for i in range(n):
        if leftChild[i] != -1: parent[leftChild[i]].append(i)
        if rightChild[i] != -1: parent[rightChild[i]].append(i)

    for i in range(n):
        if parent[i] and parent[parent[i][0]]==[i]:
            return False

    roots = [i for i in range(len(parent)) if not parent[i]]

    if len(roots) != 1:
        return False

    root = roots[0]

    return max(leftChild[root],rightChild[root]) != -1 or n==1