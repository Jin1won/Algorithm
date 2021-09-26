from collections import deque

def bfs(x,y,cnt,graph):
    queue=deque()
    visited = [[False]*5 for _ in range(5)]
    queue.append((x,y,cnt))
    while queue:
        x,y,cnt = queue.popleft()
        visited[x][y] = True
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if cnt < 2:
                    if graph[nx][ny] == "O":
                        queue.append((nx,ny,cnt+1))
                    elif graph[nx][ny] == "P":
                        return False
    return True

def solution(places):
    answer = []
    for i in range(len(places)):
        graph = []
        person = []
        for j in range(5):
            graph.append(list(map(str,places[i][j])))
            for k in range(5):
                if graph[j][k] == "P":
                    person.append((j,k))
        check = True
        for x,y in person:
            if not bfs(x,y,0,graph):
                check=False
                break
        if check:
            answer.append(1)
        else:
            answer.append(0)
    return answer