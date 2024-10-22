# 부셨는지 아닌지를 체크해야한다.
# 일단 부수고 보고 아니면 지나간다

from collections import deque
import heapq
n,m,k = map(int, input().split())
graph = [list(map(int,input()))for _ in range(n)]
values = [[[1e9] * (k+1) for _ in range(m)] for _ in range(n)]
visited = [[[False]* (k+1) for _ in range(m)]for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque([(0,0,0)])
values[0][0][0] = 1
visited[0][0][0] = True
while q:
    y,x,time = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 그래프안이고 방문안한 곳일 때
        if 0<=ny<n and 0<=nx<m and visited[ny][nx][time] == False:
            # 벽이라면 
            if graph[ny][nx] == 1:
                # 뚫을 수 있다면
                if time < k:
                    if values[y][x][time] + 1 < values[ny][nx][time+1]:
                        values[ny][nx][time+1] = values[y][x][time] + 1
                        visited[ny][nx][time+1] = True
                        q.append((ny,nx,time+1))
            else:
                if values[y][x][time] + 1 < values[ny][nx][time]:
                    values[ny][nx][time] = values[y][x][time] + 1
                    visited[ny][nx][time] = True
                    q.append((ny,nx,time))
print(min(values[n-1][m-1]) if min(values[n-1][m-1]) != 1e9 else -1)