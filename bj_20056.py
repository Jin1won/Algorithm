import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())

graph = [[deque() for _ in range(n)] for _ in range(n)]
fireballs=deque()
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])#맵에 파이어볼 넣기
    fireballs.append([r-1, c-1]) #파이어볼 위치

direction_r = [-1,-1,0,1,1,1,0,-1] #0부터 7까지의 방향 저장
direction_c = [0,1,1,1,0,-1,-1,-1]
#명령에 따른 이동 시작
for i in range(k):
    f_len = len(fireballs)
    for _ in range(f_len):
        r,c = fireballs.popleft()
        m,s,d = graph[r][c].popleft()
        nr = r + (s * direction_r[d]) #d방향으로 s만큼 이동
        nc = c + (s * direction_c[d])
        while nr >= n:
            nr -= n
        while nc >= n:
            nc -= n
        while nr < 0:
            nr += n
        while nc < 0:
            nc += n
        if [nr,nc] not in fireballs:
            fireballs.append([nr,nc])
        graph[nr][nc].append([m,s,d])
    f_length = len(fireballs)
    print(graph)
    for q in range(f_length):
        j,l = fireballs.popleft()
        g_len=len(graph[j][l])
        if g_len > 1: #2개 이상의 파이어볼 만났을 때
            total_mass = 0
            total_velocity = 0
            total_direction = graph[j][l][0][2] % 2
            for f in range(len(graph[j][l])):
                total_mass += graph[j][l][f][0]
                total_velocity += graph[j][l][f][1]
                total_direction.append(graph[j][l][f][2])
                graph[j][l].popleft()
            divided_mass=total_mass//5
            divided_velocity=total_velocity//g_len
            a = total_direction[0]%2
            four_direction = [0,2,4,6]
            for i in range(1,len(total_direction)):
                if total_direction[i] % 2 != a:
                    four_direction = [1,3,5,7]
                    break                
            if divided_mass != 0:
                for d in four_direction:
                    if [j,l] not in fireballs:
                        fireballs.append([j,l])
                    graph[j][l].append([divided_mass,divided_velocity,d])
        else:
            fireballs.append([j,l])
print(graph)
# print(fireballs)
result = 0
for i in range(n):
    for j in range(n):
        if len(graph[i][j]) != 0:
            for fireball in graph[i][j]:
                result += fireball[0]
print(result)