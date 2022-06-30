import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
graph = []
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

mouse = []
normal = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            mouse.append((i,j))
        elif graph[i][j] == 0:
            normal += 1

def bfs():
    global normal
    queue = deque()
    for x,y in mouse:    
        queue.append((x,y,0))
        visited[x][y] = True
    end = 0
    while queue:
        x,y,year = queue.popleft()
        end = max(end,year)   
        for dx, dy in (1,0),(0,1),(-1,0),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    normal -= 1
                    visited[nx][ny] = True
                    queue.append((nx,ny,year+1))
    return end


if normal == 0:
    print(0)

result=bfs()

if normal != 0:
    print(-1)
else:
    print(result)