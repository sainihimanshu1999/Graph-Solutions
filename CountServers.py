'''
count servers per row and servers per col, if count of any of the them is greater than 1, increase connect
'''

def servers(self,grid):
    m,n = len(grid),len(grid[0])

    if not m and not n:
        return 0

    connected = 0
    points = []
    row_server = [0]*m
    col_server = [0]*n

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                points.append((i,j))
                row_server[i]+=1
                col_server[j]+=1
    
    for row,col in points:
        if row_server[row]>1 or col_server[col]>1:
            connected += 1

    return connected