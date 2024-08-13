import sys
input = sys.stdin.readline
import heapq
n = int(input())
q = []
for _ in range(n):
    number = int(input())
    if number > 0:
        heapq.heappush(q, number)
    elif number == 0:
        if len(q) == 0:
            print("0")
        else:
            print(heapq.heappop(q))
    