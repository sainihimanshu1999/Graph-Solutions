'''
we use dijkstra algorithm here
'''
from heapq import *
def minEffort(self,heights):
    m,n = len(heights),len(heights[0])

    dist = [[float('inf')]*n for _ in range(m)]

    heap = [(0,0,0)]

    moves = [0,1,0,-1,0]

    while heap:
        d,row,col = heappop(heap)

        if d>dist[row][col]: continue

        if row == m-1 and col == n-1:
            return d
        
        for i in range(4):
            nr,nc = row+moves[i],col+moves[i+1]
            if 0<=nr<m and 0<=nc<n:
                newDist = max(d,abs(heights[nr][nc]-heights[row][col]))
                if dist[nr][nc]>newDist:
                    dist[nr][nc] = newDist
                    heappush(heap,(dist[nr][nc],nr,nc))