import sys

s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

# dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
# result = 0

# for i in range(1,len(s1)+1):
#     for j in range(1,len(s2)+1):
#         if s1[i-1] == s2[j-1]:
#             dp[i][j] = dp[i-1][j-1]+1
#             result = max(dp[i][j],result)

# print(result)

dp = [0 for _ in range(len(s2)+1)]
result = 0

for i in range(1,len(s1)+1):
    for j in range(len(s2),0,-1):
        if s1[i-1] == s2[j-1]:
            dp[j] = dp[j-1]+1
        else:
            dp[j] = 0
        result = max(result,dp[j])

print(result)