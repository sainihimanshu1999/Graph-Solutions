'''
We do this question by bfs and we just have to check wheter it is possible or not
'''

def courseSchedule(self,n, preq):
    source = [set() for _ in range(n)]
    destination = [set() for _ in range(n)]

    for d,s in preq:
        source[d].add(s)
        destination[s].add(d)

    result = [x for x in range(n) if not source[x]]

    for s in result:
        for d in destination[s]:
            source[d].remove(s)
            if not source[d]:
                result.append(d)

    return len(result) == n