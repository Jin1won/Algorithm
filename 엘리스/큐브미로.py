import sys

l,r,c = map(int,sys.stdin.readline().split())

graph = []
elice = []
exit = []
visited = [[[False]*c for _ in range(r)]for _ in range(l)]

for z in range(l):
    li = []
    for y in range(r):
        li.append(list(sys.stdin.readline().strip()))
    graph.append(li)
    sys.stdin.readline().strip()
sys.stdin.readline().strip()

for z in range(l):
    for y in range(r):
        for x in range(c):
            if graph[z][y][x] == 'S':
                elice.append((z,y,x))
            elif graph[z][y][x] == 'E':
                exit.append((z,y,x))

answer = 10000000000000

def dfs(z,y,x,cnt):
    global answer
    if graph[z][y][x] == "E":
        answer = min(answer,cnt)
        return
    for dz, dy, dx in (1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1):
        nx = x + dx
        ny = y + dy
        nz = z + dz
        if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and not visited[nz][ny][nx]:
            if graph[nz][ny][nx] == '.':
                visited[nz][ny][nx] = True
                dfs(nz,ny,nx,cnt+1)
                visited[nz][ny][nx] = False
dfs(elice[0][0],elice[0][1],elice[0][2],0)
print(answer)