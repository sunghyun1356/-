import sys
input = sys.stdin.readline
from collections import deque

# 각 deque에는 움직인거리랑 부순 벽의 개수를 구해준다

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
candidate = []
visited = [[float('inf')] * m for _ in range(n)]
visited[0][0] = 0

def bfs():
    q = deque([(0,0,0)])
    while q:
        y, x, b = q.popleft()
        if y == n-1 and x == m-1:
            candidate.append(b)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] =="1":
                    if b+1 < visited[ny][nx]:
                        visited[ny][nx] = b+1
                        q.append((ny,nx,b+1))
                else:
                    if b < visited[ny][nx]:
                        visited[ny][nx] = b
                        q.append((ny, nx,b))
    return candidate

print(min(bfs()))


