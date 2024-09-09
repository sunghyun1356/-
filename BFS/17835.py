import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]

# 그래프 입력 받기 (역방향으로 저장)
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v-1].append((c, u-1))  # 도로를 역방향으로 저장

# 면접장이 위치한 도시들
testing = list(map(int, input().split()))
# 각 도시의 최단 거리 초기화
dist = [INF] * n

# 우선순위 큐를 이용한 다익스트라 알고리즘
def dijkstra():
    heap = []
    # 면접장이 위치한 도시들을 시작점으로 다익스트라 실행
    for t in testing:
        heapq.heappush(heap, (0, t-1))  # (거리, 도시)
        dist[t-1] = 0  # 면접장은 거리가 0
    
    while heap:
        now_value, now = heapq.heappop(heap)
        if now_value > dist[now]:
            continue
        
        for next_value, next_city in graph[now]:
            if now_value + next_value < dist[next_city]:
                dist[next_city] = now_value + next_value
                heapq.heappush(heap, (dist[next_city], next_city))

# 다익스트라 알고리즘 실행
dijkstra()

# 최대 거리와 해당 도시 찾기
max_dist = -1
max_city = -1

for i in range(n):
    if dist[i] > max_dist:
        max_dist = dist[i]
        max_city = i
    elif dist[i] == max_dist and i < max_city:
        max_city = i

# 결과 출력
print(max_city + 1)  # 도시 번호는 1부터 시작
print(max_dist)
