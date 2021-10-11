import sys
from collections import deque

n = int(sys.stdin.readline().strip())

population = list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    l = list(map(int,sys.stdin.readline().split()))
    for j in l[1:]:
        graph[i].append(j)

def bfs(group):
    queue=deque()
    queue.append(group[0])
    visit = [False for _ in range(n+1)]
    visit[group[0]] = True
    cnt = 1
    answer = 0
    while queue:
        point = queue.popleft()
        answer += population[point-1]
        for i in graph[point]:
            if i in group and not visit[i]:
                visit[i] = True
                cnt += 1
                queue.append(i)
    if cnt == len(group):
        return answer
    else:
        return False

result = 100000000000

def dfs(idx,cnt,end):
    global result
    if cnt == end:
        g1,g2 = deque(),deque()
        for i in range(1,n+1):
            if visited[i]:#방문했으면 g1으로 아니면 g2로
                g1.append(i)
            else:
                g2.append(i)
        num1 = bfs(g1)
        if not num1:
            return
        num2 = bfs(g2)   
        if not num2:
            return 
        result = min(result,abs(num1-num2))
    for i in range(idx, n+1):
        visited[i] = True
        dfs(i + 1, cnt + 1,end)
        visited[i] = False

for i in range(1,n//2+1):
    visited = [False for _ in range(n+1)]
    dfs(1,0,i)

if result != 100000000000:
    print(result)
else:
    print(-1)