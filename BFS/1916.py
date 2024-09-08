import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s-1].append((v, e-1))

start, end = map(int, input().split())

dist = list(1e9 for _ in range(m))

def dijstra():
    heap = [(0,start-1)]
    while heap:
        now_value, now = heapq.heappop(heap)
        if now_value > dist[now]:
            continue
        for next_value, next in graph[now]:
            if now_value+next_value < dist[next]:
                dist[next] = now_value+next_value
                heapq.heappush(heap, (now_value+next_value, next))

dijstra()

print(dist[end-1])
