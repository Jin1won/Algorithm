import sys
n,m = map(int,sys.stdin.readline().split())
answer = []
visited = [False for _ in range(n+1)]

def dfs():
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        answer.append(i)
        dfs()
        answer.pop()
        visited[i] = False

dfs()