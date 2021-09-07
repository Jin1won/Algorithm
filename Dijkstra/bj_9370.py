import sys
from heapq import heappush, heappop

# g -> h -> 목적지인 경우, h -> g -> 목적지인 경우
def dijkstra(s):
    dist = [100000000 for _ in range(n + 1)]
    dist[s] = 0
    heap = []
    heappush(heap, [0, s]) 
    while heap:
        we, nu = heappop(heap) 
        for ne, nw in graph[nu]:
            wei = we + nw 
            if wei < dist[ne]: 
                dist[ne] = wei 
                heappush(heap, [wei, ne])
    return dist

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n,m,t = map(int,sys.stdin.readline().split())
    s,g,h = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a,b,d = map(int,sys.stdin.readline().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    de = []

    for k in range(t):
        de.append(int(input()))

    s_list = dijkstra(s)
    g_list = dijkstra(g)
    h_list = dijkstra(h)
    answer = []

    for i in de:
        if s_list[i] == s_list[g] + g_list[h] + h_list[i] or s_list[i] == s_list[h] + h_list[g] + g_list[i]:
            answer.append(i)
    answer.sort()
    for i in answer:
        print(i, end=" ")
    print()