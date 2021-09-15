import sys

r,c,t = map(int,sys.stdin.readline().split())

m = []
air_purifier = []
for _ in range(r):
    m.append(list(map(int,sys.stdin.readline().split())))


def spread():
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if m[i][j] > 0:
                for dx,dy in (1,0),(0,1),(-1,0),(0,-1): #확산
                    x = dx+i
                    y = dy+j
                    if 0 <= x < r and 0 <= y < c and m[x][y] != -1:
                        temp[x][y] += (m[i][j] // 5)
                        temp[i][j] -= (m[i][j] // 5)
            elif m[i][j]<0 and len(air_purifier) < 2: #공기청정기 위치
                air_purifier.append([i,j])
    for i in range(r): #확산된 칸에 확산된만큼 더해준다
        for j in range(c):
            m[i][j] += temp[i][j]

def circulation():
    x1,y1 = air_purifier[0]
    dic1 = [(-1,0),(0,1),(1,0),(0,-1)]
    for i in range(len(dic1)):
        while 0 <= x1 + dic1[i][0] <= air_purifier[0][0] and 0 <= y1 + dic1[i][1] < c and m[x1+dic1[i][0]][y1+dic1[i][1]] != m[air_purifier[0][0]][air_purifier[0][1]]:
            x1 += dic1[i][0]
            y1 += dic1[i][1]
            if 0 <= x1 + dic1[i][0] <= air_purifier[0][0] and 0 <= y1 + dic1[i][1] < c:
                if m[x1+dic1[i][0]][y1+dic1[i][1]] == -1:
                    m[x1][y1] = 0
                else:
                    m[x1][y1] = m[x1+dic1[i][0]][y1+dic1[i][1]]
            else:
                m[x1][y1] = m[x1+dic1[i+1][0]][y1+dic1[i+1][1]]


    x2,y2 = air_purifier[1]
    dic2 = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(len(dic2)):
        while air_purifier[1][0] <= x2 + dic2[i][0] < r  and 0 <= y2 + dic2[i][1] < c and m[x2+dic2[i][0]][y2+dic2[i][1]] != m[air_purifier[1][0]][air_purifier[1][1]]:
            x2 += dic2[i][0]
            y2 += dic2[i][1]
            if air_purifier[1][0] <= x2 + dic2[i][0] < r  and 0 <= y2 + dic2[i][1] < c:
                if m[x2+dic2[i][0]][y2+dic2[i][1]] == -1:
                    m[x2][y2] = 0
                else:
                    m[x2][y2] = m[x2+dic2[i][0]][y2+dic2[i][1]]
            else:
                m[x2][y2] = m[x2+dic2[i+1][0]][y2+dic2[i+1][1]]

result = 0
for _ in range(t):
    spread()
    circulation()
for i in range(r):
    for j in range(c):
        if m[i][j] > 0:
            result += m[i][j]
print(result)