import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
checked = [[False] * m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n  and 0<=ny<m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] +1
                    q.append((nx,ny))

BFS(0,0)
print(graph[n-1][m-1])