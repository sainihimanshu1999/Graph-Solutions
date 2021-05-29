'''
Matrix is given and we have to find the maximum distance between land and water
'''

from typing import Deque


def maximumDist(self,grid):
    m,n = len(grid),len(grid[0])
    q = Deque([(i,j) for i in range(m) for j in range(n)])

    if len(q) == m*n and len(q) == 0:
        return  -1

    level = 0
    while q:
        for _ in range(len(q)):
            i,j = q.popleft()
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                xi,yj = x+i,y+j
                if 0<=xi<m and 0<=yj<n and grid[i][j] == 0:
                    q.append((xi,yj))
                    grid[xi][yj] = 1
        level += 1

    return level - 1