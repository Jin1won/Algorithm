import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j == 1:
            dp[i][j] = 1;
        else:
            if i == 1:
                dp[i][j] = j;
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n][k]%1000000000)