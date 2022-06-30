import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().strip())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):  # 상어의 좌표
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j


def bfs(x, y, size):  # 먹을 수 있는 물고기가 있나 체크
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    queue = deque()
    queue.append((x, y))
    heap = []
    while queue:
        x, y = queue.popleft()
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] > size:  # 물고기 크기가 사이즈보다 크면 스킵
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if 0 < graph[nx][ny] < size:  # 물고기 크기가 사이즈보다 작으면 먹는다.
                    heapq.heappush(heap, (visited[nx][ny], nx, ny))
                    # heapq는 가장 왼쪽이 가장 작은 값이다.
    return heap


time = 0
eat = 0
size = 2
while True:
    heap = bfs(shark_x, shark_y, size)
    print(heap)
    # 이전에 먹은 물고기 좌표는 없어지고, 계속 먹을 수 있는 물고기 좌표가 갱신되어야 하므로 heap을 계속 선언해준다.
    if not heap:
        break
    dist, x, y = heapq.heappop(heap)
    graph[x][y] = 9
    graph[shark_x][shark_y] = 0
    shark_x, shark_y = x, y
    eat += 1
    time += dist
    if eat == size:  # 상어 사이즈 만큼 물고기를 먹으면 성장
        size += 1
        eat = 0

print(time)
