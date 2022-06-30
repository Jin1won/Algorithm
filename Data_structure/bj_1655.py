import sys
import heapq

n = int(sys.stdin.readline().strip())

left_heap = [] #max heap
right_heap = [] #min heap

result = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if len(left_heap) == len(right_heap): #현재 부른것들의 갯수가 홀수면
        heapq.heappush(left_heap,-num)
    else: #현재 부른것들의 갯수가 짝수면
        heapq.heappush(right_heap,num)
    if right_heap and -left_heap[0] > right_heap[0]:#왼쪽 값이 오른쪽 값보다 큰 경우
        temp_min = heapq.heappop(right_heap)
        temp_max = heapq.heappop(left_heap)
        heapq.heappush(left_heap,-temp_min)
        heapq.heappush(right_heap,-temp_max)

    result.append(-left_heap[0])

for r in result:
    print(r)