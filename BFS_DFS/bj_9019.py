import sys
from collections import deque

t = int(sys.stdin.readline().strip())

def D(n):
    n *= 2
    if n >= 10000:
        n = n%10000
    return n

def S(n):
    if n == 0:
        n = 9999
    else:
        n -= 1
    return n

def L(n):
    t = n // 1000
    n = (n - t*1000)*10 + t
    return n

def R(n):
    o = n % 10
    n = (n // 10) + (o * 1000)
    return n

def bfs():
    visited = [False for _ in range(10000)]
    queue = deque()
    visited[a] = True
    queue.append([a, ""])
    while queue:
        num, result = queue.popleft()
        if num == b:
            return result
        d = D(num)
        if not visited[d]:
            visited[d] = True
            queue.append([d,result+"D"])
        s = S(num)
        if not visited[s]:
            visited[s] = True
            queue.append([s,result+"S"])
        l = L(num)
        if not visited[l]:
            visited[l] = True
            queue.append([l,result+"L"])
        r = R(num)
        if not visited[r]:
            visited[r] = True
            queue.append([r,result+"R"])

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(bfs())