
def kthElement(self,lo,hi,k):
    cache = {1:1}
    def power(x):
        if x not in cache:
            if x%2==0:
                cache[x] = 1+power(x/2)
            else:
                cache[x] = 1+power(3*x+1)

        return cache[x]

    return sorted((power(i),i) for i in range(lo,hi+1))[k-1][1]