import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y, graph, visited):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        if graph[y][x] == 1:
            for dx, dy in (1,0), (-1,0):

        if graph[y][x] == 2:
            for dx, dy in (1,0), (-1,0):

        if graph[y][x] == 3:
            for dx, dy in (1,0), (-1,0):

        if graph[y][x] == 4:
            for dx, dy in (1,0), (-1,0):
    


print(graph)