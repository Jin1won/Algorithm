import sys
from heapq import heappop, heappush

n,m,d = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(sys.stdin.readline().split())

def count_enemy():
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt +=1
    return cnt

def enemy_forward():
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i == 0:
                graph[i][j] = 0
            else:
                graph[i][j] = graph[i-1][j]

def archer_attack(a,b,c):
    cnt=0
    delete_list = []
    archers = [a,b,c]
    for archer in archers:
        q = []
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if graph[i][j] == 1:
                    dist=abs(n-i) + abs(archer-j)
                    if dist <= d:
                        heappush(q, [dist, j, i])
        if q:
            distance,x,y = q.heappop()
            delete_list.append((x,y))
        for x,y in delete_list:
            graph[x][y] = 0
            cnt += 1
    return cnt

def game(a,b,c):
    print(a,end=" ")
    print(b,end=" ")
    print(c,end=" ")
    print()
    cnt=0
    while count_enemy() != 0:
        cnt += archer_attack(a,b,c)
        enemy_forward()
    return cnt

position = []
result=0
#궁수의 위치를 정한 후, game시작
def archer_position(idx,cnt):
    global result
    if cnt == 3:
        result = max(result,game(position[0],position[1],position[2]))
        return
    for i in range(idx, m): 
        position.append(idx)
        archer_position(i + 1, cnt + 1)
        position.pop()

archer_position(0,0)
print(result)