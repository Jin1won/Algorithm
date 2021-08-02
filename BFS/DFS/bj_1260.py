import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]
line = []

for i in range(m): #간선들 저장
    line.append(list(map(int, sys.stdin.readline().split())))

for i in line:
    a,b = i[0], i[1]
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort() #append는 늦게 된 숫자라도 우선순위가 먼저일수도 있으므로 sort 시켜준다
    graph[b].sort()

def dfs(v):
    print(v,end=" ")
    visited_dfs[v] = True
    for i in graph[v]:
        if visited_dfs[i] != True:
            dfs(i)
    return

def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if visited_bfs[i] != True:
                queue.append(i)
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)