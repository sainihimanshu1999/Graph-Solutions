'''
In this question we clone method by using hashmap/dictionary and using 3 methods, DFS iterative,
DFS recursive and BFS(always iterative)
'''

#dfs iter
from typing import no_type_check_decorator


def clone(self,node):
    dic = {}
    dic[node] = Node(node.val)
    stack =[node]

    while stack:
        currNode = stack.pop()
        for neig in node.neighbors:
            if neig not in dic:
                dic[neig] = Node(neig.val)
                stack.append(neig)
            dic[neig].neighbors.append(dic[currNode])

    return dic[node]



#DFS clone

def clone2(self,node):
    def dfs(node):
        mapp[node] = Node.(node.val)

        for nieg in node.neighbors:
            if nieg not in mapp: dfs(nieg)

            mapp[node].neighbors += [[mapp[nieg]]]

    if not node: return
    mapp = {}
    dfs(node)
    return mapp[node]
