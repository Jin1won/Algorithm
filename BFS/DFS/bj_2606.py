import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]

visited_dfs = [False for _ in range(m+1)]
visited_bfs = [False for _ in range(m+1)]

cnt = 0

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# def dfs(v):
#     global cnt
#     visited_dfs[v] = True
#     for i in graph[v]:
#         if visited_dfs[i] != True:
#             cnt += 1
#             dfs(i)
#     return

# dfs(1)
# print(cnt)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True
    global cnt
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited_bfs[i] != True:
                cnt += 1
                queue.append(i)
                visited_bfs[i] = True
    print(cnt)            
bfs(1)
