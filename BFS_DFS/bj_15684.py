import sys

n,m,h = map(int,sys.stdin.readline().split())

visited = [[False] * (n+1) for _ in range(h+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    visited[a][b] = True # 먼저 그은 가로선들

def simulation(): # 각 라인이 몇 번 째로 가는지 체크
    for i in range(1,n+1):  
        current_line = i
        for j in range(1,h+1):
            if current_line != n and visited[j][current_line]: # 맨 오른쪽 라인은 오른쪽으로 이동할 수 없으므로 제외시켜 준다.
                current_line += 1
            elif current_line != 1 and visited[j][current_line-1]: # 맨 왼쪽 라인은 왼쪽으로 이동할 수 없으므로 제외시켜 준다.
                current_line -= 1
        if current_line != i:
            return False
    return True

def dfs(x,y,cnt):  # 콤비네이션 공식 형태
    global result
    if simulation():
        result = min(result,cnt)
        return
    if cnt == 3: # 3개를 만들었는데도 sinulation을 통과하지 못하면 그 뒤는 볼 필요가 없으므로 return시킨다.
        return
    for i in range(x, h+1):
        for j in range(1,n): # 1번부터 시작하는 이유는 i가 x+1이 됬을때는 j가 1부터 돌아야되서
            if visited[i][j]: continue #이미 가로선이 있는 경우
            if i == x and j < y: continue # 순서상 이전 차례를 뽑은 경우
            if j > 1 and visited[i][j-1]: continue #왼쪽에 가로선이 있는 경우
            if j < n-1 and visited[i][j+1]: continue #오른쪽에 가로선이 있는 경우
            visited[i][j] = True # 가로선 추가
            dfs(i,j, cnt + 1)
            visited[i][j] = False

result = 4

dfs(1,1,0)

if result == 4:
    print(-1)
else:
    print(result)