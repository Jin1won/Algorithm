import sys
from heapq import heappush, heappop

v,e = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline().strip())

graph = [[] for _ in range(v + 1)]
dp = [100000000 for _ in range(v + 1)]

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

def dijkstra(k):
    dp[k] = 0
    heap = []
    heappush(heap, [0, k]) # k번째 정점까지의 가중치
    while heap:
        w, n = heappop(heap) # heap에 들어있는 값들 중 가장 왼쪽 값이(가장 작은 가중치에 해당하는 값이) 나온다.
        for n_n, wei in graph[n]:
            n_w = wei + w # 새로 찾은 정점까지의 가중치
            if n_w < dp[n_n]: # 어떤 값이 더 작은지 비교한다.
                dp[n_n] = n_w # 더 작다면 갱신해준다. 
                heappush(heap, [n_w, n_n]) # 가장 작은 값을 갱신한 정점과 연결된 다른 정점이 있는지 찾기 위해 push해준다.

dijkstra(k)

for i in range(1,len(dp)):
    if dp[i] != 100000000:
        print(dp[i])
    else:
        print("INF")

# 그냥 queue써도 되지만 queue는 모든 경우를 다 넣어서 오래걸릴수 있는 반면 heap은 더 작은 가중치부터 넣어지기 때문에 더 짧은 시간에 경로를 찾을 수 있다.(어짜피 없어질 경로들을 더 추가하지 않아도 된다)