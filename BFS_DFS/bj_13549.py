import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
graph = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]

def bfs():
  queue = deque()
  queue.append(n)
  visited[n] = True
  while queue:
    position = queue.popleft()
    for nextPosition in (2*position, position+1, position-1):
      if 0 <= nextPosition <=100000:
        if not visited[nextPosition]:
          if nextPosition == 2*position:
            visited[nextPosition] = True
            graph[nextPosition] = graph[position]
            queue.appendleft(nextPosition)
          else:
            visited[nextPosition] = True
            graph[nextPosition] = graph[position]+1
            queue.append(nextPosition)

bfs();

print(graph[k])