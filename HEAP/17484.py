import sys
import heapq
input = sys.stdin.readline

dy = [1, 1, 1]
dx = [-1, 0, 1]

# 다익스트라는 그 전의 방향에 대해서도 알고 있어야한다.
def dijkstra(graph, n, m):
    pq = []
    
    dist = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]
    
    for j in range(m):
        for d in range(3):
            heapq.heappush(pq, (graph[0][j], 0, j, d))
            dist[0][j][d] = graph[0][j]
    
    while pq:
        cost, y, x, prev_d = heapq.heappop(pq)
        
        if y == n - 1:
            continue
        
        for d in range(3):
            if d == prev_d:
                continue
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                new_cost = cost + graph[ny][nx]
                if new_cost < dist[ny][nx][d]:
                    dist[ny][nx][d] = new_cost
                    heapq.heappush(pq, (new_cost, ny, nx, d))
    
    return min(dist[n-1][j][d] for j in range(m) for d in range(3))

def main():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    result = dijkstra(graph, n, m)
    print(result)

if __name__ == "__main__":
    main()
