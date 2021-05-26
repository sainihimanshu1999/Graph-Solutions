def start(self,edges):
    x,y = edges[0][0], edges[1][0]

    if x ==edges[1][0] or x == edges[1][1]:
        return x

    return y