import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())

add = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
area = [[5] * n for _ in range(n)]
for _ in range(m):  
    x,y,z=map(int,sys.stdin.readline().split())
    tree[x-1][y-1].append(z)

def spring():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] <= area[i][j]: #양분을 먹을 수 있으면
                    area[i][j] -= tree[i][j][k] #나무 나이만큼 양분 없어지고
                    tree[i][j][k] += 1 #나무나이는 1증가
                else: #먹을 수 없으면   
                    for _ in range(k,len(tree[i][j])): #여름
                        area[i][j] += tree[i][j].pop() // 2 #뒤는 어짜피 다 양분을 못먹으므로 pop시킨다
                    break

def fall(): #가을이면
    for i in range(n):
        for j in range(n):
            for k in tree[i][j]:
                if k % 5 == 0:
                    for dx, dy in (1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1): #8칸에 나무 심기
                        x = dx + i
                        y = dy + j
                        if 0 <= x < n and 0 <= y <n:
                            tree[x][y].appendleft(1)
            area[i][j] += add[i][j] #i,j번째 칸에 대한 가을처리가 끝났으므로 겨울을 처리해준다.

for _ in range(k):
    spring()
    fall()

cnt = 0

for i in range(n):
    for j in range(n):
        cnt += len(tree[i][j])

print(cnt)