from collections import deque
our = 0
enemy = 0

m,n = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x,value):
    count = 1
    q = deque([(y,x)])
    visited[y][x] = True
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == False and graph[ny][nx] == value:
                    count+=1
                    visited[ny][nx] = True
                    q.append((ny,nx))
    return count

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            value = bfs(i,j,graph[i][j])
            if graph[i][j] == "W":
                our += value**2
            else:
                enemy += value**2

print(our, enemy)
    