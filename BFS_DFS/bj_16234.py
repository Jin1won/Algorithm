import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().split())
skip = True #연합 없을시 while문 종료하기 위한 변수
cities = []

for i in range(n):
    cities.append(list(map(int,sys.stdin.readline().split())))

def bfs(x,y):
    global skip
    if visited[x][y]: #이미 연합 완료되면 함수 종료
        return
    queue = deque()
    queue.append((x,y))
    alliance = []
    while queue:
        x,y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        alliance.append((x,y))
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(cities[x][y] - cities[nx][ny]) <= r:
                    queue.append((nx,ny))
    if len(alliance) == 1: #연합 없으면 종료
        return

    sum = 0
    skip = True
    for i in alliance:
        x,y = i
        sum += cities[x][y]
    for i in alliance:
        x,y = i
        cities[x][y] = sum // len(alliance)

day = -1

while skip:
    visited = [[False]*n for _ in range(n)]
    skip = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)

    day += 1

print(day)