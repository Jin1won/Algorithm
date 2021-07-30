import sys

n,m = map(int, sys.stdin.readline().split())

height = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(height)

while start <= end:
    mid = (start+end) // 2

    sum = 0

    for i in height:
        if i > mid:
            sum += (i-mid)
        
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)