import sys
input = sys.stdin.readline
from collections import deque

n,l,r = map(int, input().split())
graph = [list(map, int, input().split())for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = 0

def bfs(y,x,visited):
    global result
    candidate = []
    candidate.append([y,x])
    q= deque([(y,x,candidate)])
    visited[y][x] = True
    total = graph[y][x]
    while q:
        y,x,candidate = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if l<=abs(graph[y][x] - graph[ny][nx]) <=r and visited[ny][nx] == False:
                    candidate.append((ny,nx))
                    total+=graph[ny][nx]
                    q.append((ny,nx,candidate))
                    visited[ny][nx] = True
    each = total // len(candidate)
    for i in candidate:
        graph[i[0]][i[1]] = each
    result +=1

answer = 0

while result != n*n:
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                bfs(i,j,visited)
    answer+=1
print(answer-1)