import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))
answer = 0
start = min(arr)
end = m * max(arr)
 
while start <= end:
    mid = (start + end) // 2
 
    people = 0
    for t in arr:
        people += mid // t
    
    if people < m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
 
print(answer)