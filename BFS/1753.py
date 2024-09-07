import heapq
import sys
input = sys.stdin.readline

def dajistra(graph, s):
    v = len(graph)
    dist = [float('inf')] * v 
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        current_distance, u = heapq.heappop(heap)

        if current_distance > dist[u]:
            continue
        
        for next, weight in graph[u]:
            # 돌아가면서 현재까지 온 거리에 가중치를 더해준다
            distance = current_distance + weight
            # 만약에 거리가 현재 저장되어있는 것 보다 작다면 -> 굳이 탐색할 필요가 없는 것
            if distance < dist[next]:
                dist[next] = distance
                heapq.heappush(heap, (distance, next))

    return dist

v, e = map(int, input().split())
starting = int(input()) - 1  # 입력이 1부터 시작하므로 0-based index로 변환

# graph를 빈 리스트로 초기화
graph = [[] for _ in range(v)]

for _ in range(e):
    start, end, value = map(int, input().split())
    graph[start - 1].append((end - 1, value))  # 입력이 1부터 시작하므로 0-based index로 변환

distances = dajistra(graph, starting)

for i in distances:
    print(i if i < float('inf') else "INF")
