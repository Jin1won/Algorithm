import sys

n = int(sys.stdin.readline().strip())

distance = []
result = 0
sum = 0

for i in range(n):
    distance.append(int(sys.stdin.readline().strip()))

for i in range(n):
    sum += distance[i]

start, end = 1, sum//2

while(start <= end):
    make_long = False
    mid = (start + end)//2

    for i in range(n):
        clockwise_distance = 0
        counterclockwise_distance = 0
        for j in range(i,n):
            clockwise_distance += distance[j]
            counterclockwise_distance = sum - clockwise_distance
            if (mid <= min(clockwise_distance, counterclockwise_distance)):
                make_long = True
                break
        if(make_long):
            break
    
    if(make_long):
        start = mid+1
        result = mid
    else: 
        end = mid - 1
        

print(result)