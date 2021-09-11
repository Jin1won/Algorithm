import sys
from collections import deque

s = list(map(str,sys.stdin.readline().strip()))
bomb = list(map(str,sys.stdin.readline().strip()))

ans =deque()

for i in range(len(s)):
    ans.append(s[i])
    if ans[-1] == bomb[-1] and len(ans) >= len(bomb):
        flag = True
        for j in range(-1,-1-len(bomb),-1):
            if ans[j] != bomb[j]:
                flag = False
                break
        if(flag):
            for _ in range(len(bomb)):
                ans.pop()

if len(ans) == 0:
    print("FRULA")
else:
    for i in ans:
        print(i,end="")