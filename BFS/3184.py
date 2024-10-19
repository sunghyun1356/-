from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    w = 0
    s = 0
    if graph[i][j] == "v":
        w += 1
    elif graph[i][j] == "o":
        s += 1

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] != "#":
                visited[ny][nx] = True
                if graph[ny][nx] == "v":
                    w += 1
                elif graph[ny][nx] == "o":
                    s += 1
                q.append((ny, nx))

    return s, w

sheep = 0
wolf = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != "#" and not visited[i][j]:
            s, w = bfs(i, j)
            if w >= s:
                wolf += w
            else:
                sheep += s

print(sheep, wolf)
