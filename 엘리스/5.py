import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())

graph=[]
visited = [[False]*c for _ in range(r)]

for _ in range(r):
    graph.append(list(sys.stdin.readline().strip()))
total_sheep = 0
total_wolf = 0
def bfs(x,y):
    global total_sheep
    global total_wolf
    queue = deque()
    queue.append((x,y))
    sheep = 0
    wolf = 0
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        if graph[x][y] == "o":
            sheep += 1
        elif graph[x][y] == "v":
            wolf += 1
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] != "#":
                    queue.append((nx,ny))
                    visited[nx][ny] = True
    if sheep > wolf:
        total_sheep += sheep
    else:
        total_wolf += wolf

for i in range(r):
    for j in range(c):
        if graph[i][j] != "#" and not visited[i][j]:
            bfs(i,j)
print(total_sheep, end=" ")
print(total_wolf)