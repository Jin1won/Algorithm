import sys

n, h = map(int, sys.stdin.readline().split())

cave = []
cnt = 0
collision = []

for i in range(n):
    cave.append(int(sys.stdin.readline().strip()))

start, end = 0, n

while(start<=end):
    mid = (start + end) // 2
    collision = []
    for i in range(1, h+1):
        cnt = 0
        for j in range(n):
            if j % 2 == 0: #짝수번째
                if i <= cave[j]:
                    cnt += 1
            else: #홀수번째
                if  h - cave[j] < i:
                    cnt += 1
        collision.append(cnt)

    if cnt > mid:
        start = mid + 1
    else:
        end = mid - 1

result = 0

for i in collision:
    if i == min(collision):
        result += 1

print(min(collision),end=' ')
print(result)