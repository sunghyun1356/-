from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[[1e9] * 2 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
visited[0][0][0][1] = 1 

q = deque([(0, 0, True, 0, 1)])

while q:
    y, x, day, stop, now = q.popleft()
    day_flag = 1 if day else 0
    
    if y == n - 1 and x == m - 1:
        print(now)
        exit()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < m:
            # 벽을 부수고 이동 (낮이어야 가능)
            if graph[ny][nx] == 1 and day and stop < k and visited[stop + 1][ny][nx][0] == 1e9:
                visited[stop + 1][ny][nx][0] = now + 1
                q.append((ny, nx, False, stop + 1, now + 1))
            
            # 벽이 아닌 경우 이동
            elif graph[ny][nx] == 0 and visited[stop][ny][nx][1 - day_flag] == 1e9:
                visited[stop][ny][nx][1 - day_flag] = now + 1
                q.append((ny, nx, not day, stop, now + 1))
    
            # 밤에 벽을 부술 수 없을 때 대기
            elif not day and visited[stop][y][x][1] == 1e9 and stop < k:
                q.append((y, x, True, stop, now + 1))
                visited[stop][y][x][1] = now + 1

# 도달할 수 없으면 -1 출력
print(-1)
