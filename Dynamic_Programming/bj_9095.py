import sys

t = int(sys.stdin.readline().strip())

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(t):

    n = int(sys.stdin.readline().strip())

    for j in range(4, n+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

    print(dp[n])