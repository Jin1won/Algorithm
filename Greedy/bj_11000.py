import sys
import heapq

n = int(sys.stdin.readline().strip())
classes = []
for i in range(n):
    classes.append(list(map(int,sys.stdin.readline().split())))

classes.sort()

heap = [];
heapq.heappush(heap,classes[0][1])

for i in range(1,n):
    if classes[i][0]<heap[0]:
        heapq.heappush(heap,classes[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,classes[i][1])

print(len(heap))