'''
In this question we use Union Find Method, Union Find method is generally used where we need to group the
elements together
'''

def satisfy(self,equations):
    parent = {}

    def find(x):
        if x not in parent:
            return x
        else:
            return find(parent[x])

    for eq in equations:
        if eq[1] == '=':
            a = eq[0]
            b = eq[-1]
            x = find(a)
            y = find(b)
            if x!=y: parent[y] = x

    for eq in equations:
        if eq[1] == '!' and find(eq[0])== find(eq[-1]):
            return False


    return True