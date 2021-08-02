import sys

n,b = map(int,sys.stdin.readline().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))

temp = [[0] * n for _ in range(n)]
answer = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            answer[i][j] = 1
        answer[i][j] = 0

while(b>0):
    if b % 2 == 1:
        for i in range(n):
            for j in range(n):
                temp[i][j] = 0
                for k in range(n):
                    temp[i][j] += answer[i][k] * matrix[k][j]