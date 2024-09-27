import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited_original = [[False] * n for _ in range(n)]
visited_change = [[False] * n for _ in range(n)]

def bfs_original(y, x, color):
    q = deque([(y, x)])
    visited_original[y][x] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < n and not visited_original[ny][nx]:
                if graph[ny][nx] == color:
                    visited_original[ny][nx] = True
                    q.append((ny, nx))

def bfs_change(y, x, color):
    q = deque([(y, x)])
    visited_change[y][x] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < n and not visited_change[ny][nx]:
                # 적록색약인 경우 R과 G를 동일하게 취급
                if (color == "R" or color == "G") and (graph[ny][nx] == "R" or graph[ny][nx] == "G"):
                    visited_change[ny][nx] = True
                    q.append((ny, nx))
                elif color == "B" and graph[ny][nx] == "B":
                    visited_change[ny][nx] = True
                    q.append((ny, nx))

count_original = 0
count_change = 0

for i in range(n):
    for j in range(n):
        if not visited_original[i][j]:
            bfs_original(i, j, graph[i][j])
            count_original += 1
        if not visited_change[i][j]:
            bfs_change(i, j, graph[i][j])
            count_change += 1

print(count_original, count_change)
