import sys

S = list(map(str,sys.stdin.readline().strip()))
T = list(map(str,sys.stdin.readline().strip()))

while True:
    if S == T:
        print(1)
        break
    else:
        if len(T) == len(S):
            print(0)
            break
        else:
            if T[-1] == 'A':
                T.pop()
            else:
                T.pop()
                T.reverse()