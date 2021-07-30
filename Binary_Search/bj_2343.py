import sys

n, m = map(int, sys.stdin.readline().split())
lesson = list(map(int,sys.stdin.readline().split()))
result = 0

start = max(max(lesson),sum(lesson)//m) #블루레이에서 가질 수 있는 최소 길이에 해당하는 값이 lesson중에서 가장 큰 값보다는 커야 최소 1개 이상의 레슨이 모든 블루레이에 들어갈 수 있으므로 맥스값을 start로 설정해준다.
end = sum(lesson)

while(start <= end):
    mid = (start + end)//2
    sum = 0
    cnt = 1

    for i in lesson:
        sum += i
        if sum > mid:
            cnt += 1
            sum = i
    
    if cnt > m: #길이가 짧다 크기를 늘리자
        start = mid + 1
    else: #길이가 길다 크기를 줄이자
        result = mid #end 값이 변하기 전에 result에 먼저 넣어야 한다.
        end = mid - 1

print(result)
