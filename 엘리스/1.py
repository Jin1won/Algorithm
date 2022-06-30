import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = list(sys.stdin.readline().strip())
    s.insert(1,"a")
    flag=True
    for i in range(len(s) // 2):     
        if s[i] != s[-1 - i]:
            flag = False
            break
    if not flag:
        print("YES")
    else:
        print("NO")