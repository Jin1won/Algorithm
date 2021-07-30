import sys

n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    work = list(map(int, sys.stdin.readline().split()))
    
    dp[i] = work[0]
    
    for j in range(2, len(work)): #완료해야 하는 작업에 해당하는 dp 값들 중 최댓값에 i번째 작업시간을 더한 값을 dp값으로 저장
        dp[i] = max(dp[i], dp[work[j]]+work[0])
        
print(max(dp))