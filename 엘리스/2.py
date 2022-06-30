import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    f = [[False]*n for _ in range(n)]
    for i in range(m):
        a,b = map(int,sys.stdin.readline().split())
        f[a][b] = True
        f[b][a] = True
    if f[0][1] and f