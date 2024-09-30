from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

tomato_now = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                tomato_now.append((i, j))

def bfs(tomato_now):
    tomato = []
    temp = False
    for now_tomato in tomato_now:
        for i in range(4):
            y, x = now_tomato
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    tomato.append((ny, nx))
                    temp = True
    return temp, tomato

check(graph)

temp = True
count = 0

while temp:
    temp, tomato_now = bfs(tomato_now)
    if temp:
        count += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)  # Unripe tomatoes exist
            exit()

print(count)
