import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, n, graph):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        now_value, now = heapq.heappop(heap)
        if now_value > dist[now]:
            continue
        for next_value, next in graph[now]:
            if now_value + next_value < dist[next]:
                dist[next] = now_value + next_value
                heapq.heappush(heap, (dist[next], next))
    
    return dist

n, e = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(e):
    s, en, v = map(int, input().split())
    graph[s-1].append((v, en-1))
    graph[en-1].append((v, s-1))

start, end = map(int, input().split())
start -= 1
end -= 1

# 예를 들어 2번에서 시작해서 n 까지 가는거 구하기
dist_from_start = dijkstra(start, n, graph)

# 예를 들어 3번에서 시작해서 n 까지 가는거 구하기
dist_from_end = dijkstra(end, n, graph)

dist_from_first = dijkstra(0, n, graph)

# 0 - start - end - n
# start에서 1까지 가는거랑 , start에서 end 까지 가는거 그리고 end에서 n까지 가는거
result1 = dist_from_first[start] + dist_from_start[end] + dist_from_end[n-1]

# 0 - end - start - n
# start에서 1까지 가는 거 + end에서 end까지 + start에서 n-1까지
result2 = dist_from_first[end] + dist_from_end[start] + dist_from_start[n-1]

# start랑 end 둘중 어디를 먼저 들리는가
result = min(result1, result2)

print(result if result < float('inf') else -1)
