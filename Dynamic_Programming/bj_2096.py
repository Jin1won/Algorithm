import sys

n = int(sys.stdin.readline().strip())

dp_max = [[0] * 3 for _ in range(2)]
dp_min = [[0] * 3 for _ in range(2)]

for i in range(0,n):
    graph = list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        if j == 0:
            dp_max[i%2][j] = max(dp_max[(i+1)%2][j],dp_max[(i+1)%2][j+1]) + graph[j]
            dp_min[i%2][j] = min(dp_min[(i+1)%2][j],dp_min[(i+1)%2][j+1]) + graph[j]
        elif j == 1:
            dp_max[i%2][j] = max(dp_max[(i+1)%2][j-1],dp_max[(i+1)%2][j],dp_max[(i+1)%2][j+1]) + graph[j]
            dp_min[i%2][j] = min(dp_min[(i+1)%2][j-1],dp_min[(i+1)%2][j],dp_min[(i+1)%2][j+1]) + graph[j]
        else:
            dp_max[i%2][j] = max(dp_max[(i+1)%2][j-1],dp_max[(i+1)%2][j]) + graph[j]
            dp_min[i%2][j] = min(dp_min[(i+1)%2][j-1],dp_min[(i+1)%2][j]) + graph[j]

print(max(dp_max[(n-1)%2]),end=" ")
print(min(dp_min[(n-1)%2]))