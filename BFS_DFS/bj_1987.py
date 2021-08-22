import sys

sys.setrecursionlimit(
    400
)  # 최대 400번의 recursion이 발생할 수 있으므로 그 이상 recursion이 안 발생하게 리밋을 걸어준다.

r, c = map(int, sys.stdin.readline().split())

graph = []

for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().strip())))

visited = [False] * 26  # 알파벳 방문했는지 체크

result = 1


def dfs(x, y, cnt):
    global result

    result = max(result, cnt)

    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx = dx + x
        ny = dy + y

        if 0 <= nx < r and 0 <= ny < c and not visited[ord(graph[nx][ny]) - 65]:
            # 아스키 코드는 65부터 시작하므로 A부터 나타내기 위해 65를 빼준다
            visited[ord(graph[nx][ny]) - 65] = True
            dfs(nx, ny, cnt + 1)
            visited[ord(graph[nx][ny]) - 65] = False


visited[ord(graph[0][0]) - 65] = True  # 첫 알파벳 방문 처리
dfs(0, 0, result)
print(result)
