import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

hx,hy = map(int,sys.stdin.readline().split())
ex,ey = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

visited=[[1000000000]*m for _ in range(n)] #찬스 안쓰고 방문한 시간
visited_chance=[[1000000000]*m for _ in range(n)] #찬스 쓰고 방문한 시간

def bfs(x,y):
    queue=deque()
    visited[x][y]=0
    queue.append((x,y,1))
    while queue:
        x,y,chance=queue.popleft()
        if x == ex-1 and y == ey-1:
            if chance:
                return visited[ex-1][ey-1]
            else:
                return visited_chance[ex-1][ey-1]
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx=dx+x
            ny=dy+y
            if 0<= nx < n and 0<= ny < m:
                if chance: #찬스 있는 경우
                    if graph[nx][ny] == 1 and visited[x][y] + 1 < visited_chance[nx][ny]: #벽 뚫는 경우
                        visited_chance[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny,0))
                    elif graph[nx][ny] == 0 and visited[x][y] + 1 < visited[nx][ny]: #벽 안뚫는 경우
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny,1))
                elif graph[nx][ny] == 0 and visited_chance[x][y] + 1 < visited_chance[nx][ny]: #찬스 없는데 벽 없는 경우
                    visited_chance[nx][ny] = visited_chance[x][y] + 1
                    queue.append((nx,ny,0))
    return -1

print(bfs(hx-1,hy-1))