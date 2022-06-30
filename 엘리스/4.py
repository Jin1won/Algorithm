import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
coin = list(map(int,sys.stdin.readline().split()))

coin=list(reversed(coin))

result = 0
cnt=0
for i in range(len(coin)):
    r = m
    while r // coin[i] != 0:
        r = r % coin[i]
        cnt += 1
        for j in range(i+1,len(coin)):
            while r // coin[i] != 0:
                r = r % coin[j]
                cnt += 1
                print(r)
print(cnt)