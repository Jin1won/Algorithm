import sys

n = int(sys.stdin.readline().strip())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def dfs(v):  # v번째 줄에서 연속적으로 연결될 수 있는 경로가 있는지 찾는다
    for i in range(n):
        if not visited[i] and graph[v][i] == 1:
            visited[i] = True
            dfs(i)


result = []

for i in range(n):
    visited = [False for _ in range(n + 1)]
    dfs(i)
    for j in range(n):
        if visited[j]:  # 한줄 쭉 탐색하면서 연속되게 방문한것들은 1로 출력 아니면 0으로 출력
            print(1, end=" ")
        else:
            print(0, end=" ")
    if i != n - 1:
        print()
