import sys

n,m = map(int,sys.stdin.readline().split())

paper = []

for _ in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

visited = [[False] * m for _ in range(n)]
result = 0

f = [[(0,0),(0,1),(0,2),(1,1)], [(0,0),(1,0),(2,0),(1,1)],
    [(0,0),(0,1),(0,2),(-1,1)], [(0,0),(1,0),(2,0),(1,-1)]]

def tetromino(x,y,cnt,sum):
    global result
    if cnt == 4:
        result = max(result,sum)
        return
    for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            tetromino(nx,ny,cnt + 1,sum+paper[nx][ny])
            visited[nx][ny] = False
def fu(x,y):
    global result
    for i in f:
        try:
            sum = paper[x+i[0][0]][y+i[0][1]] + paper[x+i[1][0]][y+i[1][1]] + paper[x+i[2][0]][y+i[2][1]] + paper[x+i[3][0]][y+i[3][1]]
        except:
            sum = 0
        result = max(result,sum)
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        tetromino(i,j,1,paper[i][j])
        visited[i][j] = False
        fu(i, j)

print(result)