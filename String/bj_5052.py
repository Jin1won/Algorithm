import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    number = []
    for _ in range(n):
        number.append(list(map(int,sys.stdin.readline().strip())))
    number.sort() #소트를 하면 자기 뒤랑 자기만 비교하면 된다.
    flag=True
    for i in range(n-1):
        if len(number[i]) >= len(number[i+1]):
            continue
        if number[i] == number[i+1][:len(number[i])]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
