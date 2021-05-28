'''
In this question we use BFS or Topological sort algorithm
'''

def courses(self,n,prereq):
    source,destination = [set() for _ in range(n)],[set() for _ in range(n)]
    for d,s in prereq:
        source[d].add(s)
        destination[s].add(d)

    answer = [x for x in range(n) if not source[x]]

    for s in answer:
        for d in destination[s]:
            source[d].remove(s)
            if not source[d]:
                answer.append(d)

    return answer if len(answer)==n else []