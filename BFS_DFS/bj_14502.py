import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

empty = []
virus = []
wall = [0 for _ in range(3)]
max_result = 0

for i in range(n): #빈 칸과 바이러스가 있는 칸의 좌표를 저장한다.
    for j in range(m):
        if graph[i][j] == 0:
            empty.append([i,j])
        elif graph[i][j] == 2:
            virus.append([i,j])

def bfs(wall):
    global max_result

    temp = [[0] * m for _ in range(n)]

    for i in range(n): #temp에 graph의 형태를 복사한다.
        for j in range(m):
            temp[i][j] = graph[i][j]

    visited = [[False] * m for _ in range(n)] #방문한 곳과 cnt를 매 시행마다(새로운 벽을 세울때마다) 초기화해준다.
    cnt=0
    queue = deque()
    for i in wall: #각 시행마다 새로운 벽을 3개 세운다.
        a,b = empty[i]
        temp[a][b] = 1
    for i in virus: #바이러스의 위치를 다 넣어놓고 시작한다.
        x,y = i
        queue.append((x,y))
        visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0<= ny < m:
                if not visited[nx][ny] and temp[nx][ny] == 0: #0번 칸이면 감염시킨다
                    visited[nx][ny] = True
                    temp[nx][ny] = 2
                    queue.append((nx, ny))
    for i in range(n): #감염된 뒤 0의 갯수를 센다
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    max_result = max(max_result, cnt) #매 시행마다 0의 갯수의 총 합을 최댓값으로 갱신시킨다

def makeWall(last, num): #재귀를 사용해서 마지막 시행에서 뽑은 값과, num값을 파라미터로 넣는다. num이 3이 되면 bfs함수를 실행시켜 벽을 세운 후 0인 칸의 갯수를 센다.
    if num == 3: 
        bfs(wall)
        return
    for i in range(last+1,len(empty)): #조합처럼 겹치지 않고 각각 다른 값들의 인덱스번호를 3개씩 바꿔줄 수 있다.
        wall[num] = i
        makeWall(i,num+1)

makeWall(-1,0)

print(max_result)