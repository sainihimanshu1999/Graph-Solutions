'''
We are going to use basic dfs in this question
'''

def allPath(self,graph):

    def dfs(path):
        if path[-1] == n-1:
            ret.append(path)
            return ret 
        
        for x in graph[path[-1]]:
            dfs(path + [x])

    ret,n = [0],len(graph)-1
    dfs([0])
    return ret