import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

INF = 100000000
dist = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if dist[a][b] > c:
        dist[a][b] = c

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            dist[i][j] = 0

for k in range(1,n+1): #k번째 노드를 지난다
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()