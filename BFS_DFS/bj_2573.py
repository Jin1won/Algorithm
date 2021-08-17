import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    while queue:
        dx, dy = queue.popleft()
        for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and after_temp[nx][ny] != 0
            ):
                after_temp[nx][ny] = 0  # 0인곳 다시 방문 안하게 하려고
                visited[nx][ny] = True
                queue.append((nx, ny))


def check(i, j):  # 주변 0 갯수 세는 함수
    cnt = 0
    for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx = i + x
        ny = j + y
        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
            cnt += 1
    return cnt


def checkArea():  # 다 녹을때까지 분리 안됐는지 체크
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                return False
    return True


year = 1  # 햇수

while True:
    if checkArea():
        print(0)
        break
    temp = graph[:]  # 그래프 임시값 저장
    for i in range(n):  # 빙산 녹이기
        for j in range(m):
            if temp[i][j] != 0:
                t = graph[i][j] - check(i, j)
                if t > 0:
                    graph[i][j] = t
                else:
                    graph[i][j] = 0

    after_temp = graph[:]  # 빙산 녹은 뒤 그래프 임시값 저장

    area = 0

    for i in range(n):  # 빙산 녹은 뒤 영역 갯수 세기
        for j in range(m):
            if after_temp[i][j] != 0:
                after_temp[i][j] = 0  # 0으로 만들어서 다시 방문 못 하게 하려고
                bfs(i, j)
                area += 1

    if area >= 2:
        print(year)
        break
    year += 1
