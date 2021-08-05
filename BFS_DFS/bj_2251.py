import sys
from collections import deque

a,b,c = map(int, sys.stdin.readline().split())
visited = [[False]*201 for _ in range(201) ]
result = []

queue = deque()
queue.append((0,0))
visited[0][0] = True

def visit(na, nb):
    if not visited[na][nb]:
        visited[na][nb] = True
        queue.append((na,nb))
        
def bfs():
    while queue:
        na, nb = queue.popleft()
        nc = c - na - nb
        if na == 0:
            result.append(nc)

        if na + nb < b: #a->b
            visit(0, na+nb)
        else: 
            visit(na-(b-nb), b)

        if na + nc < c: #a->c
            visit(0, nb)
        else: 
            visit(na-(c-nc), nb)

        if nb + na < a: #b->a
            visit(na+nb, 0)
        else: 
            visit(a, nb-(a-na))

        if nb + nc < c: #b->c
            visit(na, 0)
        else: 
            visit(na, nb-(c-nc))

        if nc + na < a: #c->a
            visit(na+nc, nb)
        else: 
            visit(a, nb)

        if nc + nb < b: #c->b
            visit(na, nb+nc)
        else: 
            visit(na, b)

bfs()
result.sort()
print(' '.join(map(str,result)))