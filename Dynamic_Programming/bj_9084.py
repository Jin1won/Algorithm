import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    coins = list(map(int,sys.stdin.readline().split()))
    coins = [0] + coins
    m = int(sys.stdin.readline().strip())
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(1, m+1): #n번째 코인을 쓰냐 마냐에 따라 케이스를 나눈다.
            #만드려는 값이 새로 사용할 코인의 최소 단위보다 작은 경우
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            # n번째 코인 안쓴경우 + 쓴 경우(dp[i][j-coins[i]] = dp[i-1][j-coins[i]] + dp[i-2][j-2*coins[i]])
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
    print(dp[n][m])