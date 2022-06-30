import sys

n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(n+1)]
dp[1] = 1

for i in range(2,n+1):
    for j in range(1,i):
        dp[i] += dp[j]
print(dp[n]%99999)