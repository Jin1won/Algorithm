import sys

n, c = map(int, sys.stdin.readline().split())

house = []
result = 0

for i in range(n):
    house.append(int(sys.stdin.readline().strip()))

house.sort()

start, end = 1, (house[n-1]-house[0]) #거리

while(start <= end):
    mid = (start + end)//2
    current_start = house[0] #현재 시작점 집 좌표
    cnt = 1

    for i in range(1, n):
        distance = house[i] - current_start
        if (mid <= distance):
            cnt += 1
            current_start = house[i]
    
    if(cnt >= c): #공유기 수를 줄이자 = 간격을 넓히자
        start = mid+1
        result = mid
    else: #공유기 수를 늘리자 = 간격을 좁히자
        end = mid - 1

print(result)