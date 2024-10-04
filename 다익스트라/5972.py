import heapq
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    first, second, weight = map(int, input().split())
    graph[first-1].append((second-1, weight))
    graph[second-1].append((first-1, weight))

weights =[1e9] * (n+1)

def dajistra():
    heap = []
    heapq.heappush(heap, (0, 0))
    weights[0] = 0
    while heap:
        now, now_weight = heapq.heappop(heap)
        if weights[now] < now_weight:
            continue
        for next, next_value in graph[now]:
            new_weight = now_weight + next_value
            if new_weight < weights[next]:
                weights[next] = new_weight
                heapq.heappush(heap,(next, new_weight))
result = dajistra()
print(weights[n-1])