import sys

n,m = map(int, sys.stdin.readline().split())

height = list(map(int, sys.stdin.readline().split()))

saw = max(height)
total = 0

while(True):
    for i in range(n):
        diff = height[i] - saw

        if diff <= 0:
            total += 0
        else:
            total += diff
            height[i] -= diff
    if total >= m:
        break
    saw = saw - 1

print(saw)