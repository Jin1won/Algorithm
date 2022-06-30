import sys

n,m,k = map(int,sys.stdin.readline().split())

#처음엔 그래프에 파이어볼 도착하면 1씩 더해서 2 이상인 칸에 해당하는 애들거 더해주려 했는데 for문 너무 많이 써야해서 포기
graph = [[0]*(n+1) for _ in range(n+1)]

fireballs=[]
for _ in range(m):
    r,c,m,s,d = map(int,sys.stdin.readline().split())
    fireballs.append([r,c,m,s,d])
    #그래프에 파이어볼 넣기
    graph[r][c] += 1

direction_r = [-1,-1,0,1,1,1,0,-1] #0부터 7까지의 방향 저장
direction_c = [0,1,1,1,0,-1,-1,-1]
# #명령에 따른 이동 시작
for i in range(k):
    for _ in range(len(fireballs)):
        r,c,m,s,d = fireballs.pop()
        graph[r][c] -= 1
        nr = r + s * direction_r[d] #d방향으로 s만큼 이동
        nc = c + s * direction_c[d]
        if 1 <= nr <= r and 1<= nc <= c:
            fireballs.append([nr,nc,m,s,d])
            graph[nr][nc] += 1
    for j in range(n):
        for l in range(n):
            if graph[j][l] > 1:
                total_mass = 0
                total_velocity = 0
                total_direction = 0
                for fireball in fireballs:
                    if fireball[0] == j and fireball[1] == l:
                        total_mass += fireball[2]
                        total_velocity += fireball[3]
                        total_direction += fireball[4]
                        fireballs.pop(fireball)
                divided_mass=total_mass//5
                divided_velocity=total_velocity//graph[j][l]
                if total_direction % 2 == 0:
                    four_direction = [0,2,4,6]
                else:
                    four_direction = [1,3,5,7]
                if divided_mass != 0:
                    for d in four_direction:
                        ni = i + divided_velocity * direction_r[d] #d방향으로 s만큼 이동
                        nl = l + divided_velocity * direction_c[d]
                        fireballs.append([ni,nl,divided_mass,divided_velocity,d])
                        graph[ni][nl] += 1
                graph[i][l] = 0
    print(fireballs)

result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            for fireball in fireballs:
                    if fireball[0] == i and fireball[1] == j:
                        result += fireball[2]
print(fireballs)
print(result)