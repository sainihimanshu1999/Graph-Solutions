'''
This question is a very basic graph question, we just have to see the if we start with room 0 or node 0
we can traverse the whole graph
'''

def keys(self,rooms):
    visited = set([0])

    def dfs(room):
        for ni in rooms[room]:
            if ni not in visited:
                visited.add(ni)
                dfs(ni)

    dfs(0)
    return len(visited) == len(rooms)