import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
dp = [100000000 for _ in range(n + 1)]

for i in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append([e, c])

start, end = map(int, sys.stdin.readline().split())


def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if dp[n] < w:
            continue
        for n_n, wei in graph[n]:
            n_w = w + wei
            if dp[n_n] > n_w:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])


dijkstra(start)
print(dp[end])
