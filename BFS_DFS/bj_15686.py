import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

chicken = []
house = []

visited = [False for _ in range(13)]

for i in range(n):  # 집과 치킨집의 좌표
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))


def dfs(idx, cnt):  # 콤비네이션 공식 형태
    global result
    if cnt == m:
        s = 0
        for i in range(len(house)):
            d = 100
            for j in range(len(chicken)):
                if visited[j]:
                    hx, hy = house[i]
                    cx, cy = chicken[j]
                    d = min(abs(hx - cx) + abs(hy - cy), d)  # 치킨거리
            s += d  # 도시의 치킨거리
        result = min(result, s)  # 도시의 치킨거리 최솟값
        return
    for i in range(idx, len(chicken)):
        visited[i] = True
        dfs(i + 1, cnt + 1)
        visited[i] = False


result = 10000

dfs(0, 0)

print(result)
