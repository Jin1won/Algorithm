import sys

m,n = map(int,sys.stdin.readline().split())

maps = []
dp = [[-1] * n for _ in range(m)]

for _ in range(m):
    maps.append(list(map(int,sys.stdin.readline().split())))

def dfs(x,y):
    if x == m-1 and y == n-1: # 끝까지 가는 경로 찾으면 1 return
        return 1
    if dp[x][y] != -1: # 이미 탐색 한 경우에는 다시 탐색을 안하도록
        return dp[x][y]
    dp[x][y] = 0 # 지날 때 마다 0으로 바꿔서 지나갔다고 표시해준다.
    for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if maps[nx][ny] < maps[x][y]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))