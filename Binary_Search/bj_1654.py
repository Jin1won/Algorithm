import sys

n, k = map(int,sys.stdin.readline().split())

lines = []
cnt = 0
result = 0

for i in range(n):
    lines.append(int(sys.stdin.readline().strip()))

start, end = 1, max(lines)

while(start <= end):
    mid = (start + end) // 2
    cnt = 0

    for i in range(n):  
        cnt += lines[i] // mid
    
    if cnt >= k:
        start = mid + 1
        result = mid
    else:
        end = mid - 1 

print(result)