import sys

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
dist = [100000000 for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

def bellman_ford(start):
    dist[start] = 0
    for _ in range(n-1):
        for i in range(1,n+1): 
            for j,k in graph[i]: 
                if dist[i] != 100000000:
                    dist[j] = min(dist[j],dist[i]+k);
    negativeCycle = False
    for i in range(1,n+1): 
        for j,k in graph[i]: 
            if dist[i] != 100000000 and dist[j] > dist[i] + k:
                negativeCycle=True
                return negativeCycle
if bellman_ford(1):
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] != 100000000:
            print(dist[i])
        else:
            print(-1)
