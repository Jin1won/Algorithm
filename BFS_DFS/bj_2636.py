import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def melt(x, y):
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx = x + dx
        ny = y + dy
        if 0 < nx < n and 0 < ny < m and graph[nx][ny] == 0:
            return True
    return False


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if melt(x, y):
            graph[x][y] = 0
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx = x + dx
            ny = y + dy
            if 0 < nx < n and 0 < ny < m and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))


def checkArea():  # 다 녹았는지 체크
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                return False
    return True


hour = 0

while True:
    if checkArea():
        print(hour)
        print(area)
        break
    area = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 0:
                bfs(i, j)
                area += 1
    hour += 1
