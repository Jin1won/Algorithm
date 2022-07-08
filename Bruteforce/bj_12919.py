import sys

s = list(map(str,sys.stdin.readline().strip()))
t = list(map(str,sys.stdin.readline().strip()))

def solution(t):
    global flag
    if len(t) == len(s):
        if t == s:
            flag = True
        return

    if t[0] == 'B':
        t = t[::-1]
        t.pop()
        solution(t)
        t.append('B')
        t = t[::-1]
    if t[-1] == 'A':
        t.pop()
        solution(t)
        t.append('A')

flag = False
solution(t)

if flag:
    print(1)
else:
    print(0)