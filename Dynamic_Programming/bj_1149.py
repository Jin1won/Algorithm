import sys

n = int(sys.stdin.readline().strip())
dp = [[0] * 3 for _ in range(n)]
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(0, n):
    for j in range(3):
        if i == 0:
            dp[i][j] = graph[i][j]
        else:
            dp[i][j] = min(dp[i-1][0:j], dp[i-1][j+1:]) +  graph[i][j]

print(min(dp[n]))