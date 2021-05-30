'''
In this question we use bfs,so that we can go in each level and maximize the height difference by one
'''

from typing import Deque


def peak(self,isWater):
    m,n = len(isWater),len(isWater[0])
    height = [[-1]*n for _ in range(m)]
    q = Deque([])

    for row in range(m):
        for col in range(n):
            if isWater[row][col] == 1:
                q.append((row,col))
                height[row][col] = 0


    moves = [0,1,0,-1,0]
    while q:
        r,c = q.popleft()

        for i in range(4):
            nr,nc = r+moves[i],c+moves[i+1]

            if nr<0 or nr == m or nc<0 or nc == n or height[nr][nc]!= -1:
                continue
            
            height[nr][nc] = height[r][c] +1
            q.append((nr,nc))

    return height
