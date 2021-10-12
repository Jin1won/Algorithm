import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int,sys.stdin.readline().split()))
operators=list(map(int,sys.stdin.readline().split()))

max_result = -1000000000
min_result = 1000000001
visited = [False for _ in range(n-1)]
operator_list=[]

def dfs(cnt):
    global max_result
    global min_result
    s=numbers[0]
    if cnt == n-1:
        for i in range(len(operator_list)):
            if operator_list[i] == 0:
                s += numbers[i+1]
            elif operator_list[i] == 1:
                s -= numbers[i+1]
            elif operator_list[i] == 2:
                s *= numbers[i+1]
            elif operator_list[i] == 3:
                if s >= 0:
                    s = s // numbers[i+1]
                elif s < 0:
                    s = -(abs(s)//numbers[i+1])   
        max_result=max(max_result,s)
        min_result=min(min_result,s)
    for j in range(4):
        if operators[j] != 0:
            operator_list.append(j)
            operators[j] -= 1
            dfs(cnt + 1)
            operator_list.pop()
            operators[j] += 1
dfs(0)
print(max_result)
print(min_result)
