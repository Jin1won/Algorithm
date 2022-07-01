import sys

n = int(sys.stdin.readline().strip())
towers = list(map(int,sys.stdin.readline().split()))
stack = [0]
index = [i for i in range(len(towers))]
result = [0 for _ in range(len(towers))]

for i in range(1,n):
    while stack:
        if towers[stack[-1]] > towers[i]:
            result[i] = index[stack[-1]]+1
            break
        else:
            stack.pop()
    stack.append(i)
print(" ".join(map(str, result)))
