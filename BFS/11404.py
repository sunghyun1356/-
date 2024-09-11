import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

bus_route = [[] for _ in range(n)]

def dajistra(start):
    heap = [(0,start)]
    values = [1e9]*n
    values[start] = 0
    while heap:
        now_value, now = heapq.heappop(heap)
        for bus in bus_route[now]:
            next_value, next = bus
            if now_value > values[now]:
                continue
            if now_value + next_value < values[next]:
                values[next] = now_value + next_value
                heapq.heappush(heap, (values[next], next))
    return values


for _ in range(m):
    a,b,c = map(int, input().split())
    # 인덱스 값 조절
    bus_route[a-1].append((c,b-1))
results = []
for i in range(n):
    distances = dajistra(i)
    results.append(" ".join(str(d) if d < 1e9 else "0" for d in distances))
print("\n".join(results) + "\n")