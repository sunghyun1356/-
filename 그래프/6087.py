import sys
import heapq

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, end_x, end_y, h, w, graph):
    # 방향애 따라 다르기때문에 각각의 방향에 대한 것도 고려해준다.
    dist = [[[float('inf')] * 4 for _ in range(w)] for _ in range(h)]
    q = []
    
    for i in range(4):
        heapq.heappush(q, (0, start_x, start_y, i))
        dist[start_x][start_y][i] = 0
    
    while q:
        mirrors, x, y, direction = heapq.heappop(q)
        
        if x == end_x and y == end_y:
            return mirrors
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            new_mirrors = mirrors
            
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '*':
                if direction != i:
                    new_mirrors += 1
                
                if new_mirrors < dist[nx][ny][i]:
                    dist[nx][ny][i] = new_mirrors
                    heapq.heappush(q, (new_mirrors, nx, ny, i))
    
    return float('inf')

w, h = map(int, input().split())
graph = [list(input().strip()) for _ in range(h)]
c_positions = []

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            c_positions.append((i, j))

start_x, start_y = c_positions[0]
end_x, end_y = c_positions[1]

print(bfs(start_x, start_y, end_x, end_y, h, w, graph))
