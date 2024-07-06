import heapq
import sys
input = sys.stdin.readline

heap =[]
answer =[]
N = int(input())
for i in range(N):
    value = int(input())
    if value == 0:
        if len(heap) == 0:
            answer.append(0)
        else:
            answer.append(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -value)

for k in answer:
    print(k)