'''
we find abs(i-j) > 1
'''

def couple(self,row):
    dic = {x:i for i,x in enumerate(row)}
    swaps = 0

    for i in range(len(row)):
        x = row[i]
        y = x+1 if x%2==0 else x-1
        j = dic[y]

        if abs(j-i)>1:
            row[i+1],row[j] = row[j],row[i+1]
            swaps +=1
            dic[row[i+1]] = i+1
            dic[row[j]] = j

    return swaps