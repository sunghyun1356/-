from collections import deque

n, m = map(int, input().split())
graph_demo = [list(map(int, input().split())) for _ in range(n)]

maximum = 0
for i in range(n):
    for j in range(m):
        maximum = max(maximum, graph_demo[i][j])

real_graph = [[[0] * (maximum + 2) for _ in range(m + 2)] for _ in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, graph_demo[i-1][j-1] + 1):
            real_graph[i][j][k] = 1

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

visited = [[[False] * (maximum + 2) for _ in range(m + 2)] for _ in range(n + 2)]

q = deque()
total = 0

for i in range(1,n + 1):
    for j in range(1, m + 1):
        for k in range(1, maximum + 1):
            if real_graph[i][j][k] == 1:
                q.append((i,j,k))
            
while q:
    y, x, z = q.popleft()
    for k in range(6):
        ny = y + dy[k]
        nx = x + dx[k]
        nz = z + dz[k]
        if 0 <= ny < n + 2 and 0 <= nx < m + 2 and 0 <= nz < maximum + 2:
            if real_graph[ny][nx][nz] == 0:
                total += 1

print(total)
