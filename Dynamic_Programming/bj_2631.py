import sys

n = int(sys.stdin.readline().strip())

children = []

dp = [1 for _ in range(n)]

for _ in  range(n):
    children.append(int(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))

# idx        0 1 2 3 4 5 6
# children   3 7 5 2 6 1 4
# dp         1 2 2 1 3 1 2