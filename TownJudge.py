'''
we are given an trust array, the intution is inner-outer = n-1
'''

def townJudge(self,n,trust):
    ret = [0]*(n+1)

    for i,j in trust:
        ret[i] -= 1
        ret[j] += 1

    for i in range(1,n+1):
        if ret[i] == n-1:
            return i

    return -1