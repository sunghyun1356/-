from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0

def on(i, j, visited):
    light_candidate = []
    for direction in graph[i][j]:
        y, x = direction
        light[y][x] = True
        if not visited[y][x]:
            light_candidate.append((y, x))
    return light_candidate

n, m = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
light = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    x -= 1
    y -= 1
    a -= 1
    b -= 1
    if 0 <= y < n and 0 <= x < n and 0 <= a < n and 0 <= b < n:
        graph[y][x].append((b, a))

q = deque([(0, 0)])
light[0][0] = True
visited[0][0] = True
on(0, 0, visited)

candidate = set()
light_candidate = set()

while q:
    y, x = q.popleft()
    light_candidate.update(on(y, x, visited))
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            if light[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
            else:
                candidate.add((ny, nx))

    for c in list(candidate):
        if c in light_candidate:
            q.append(c)
            visited[c[0]][c[1]] = True
            candidate.remove(c)

# 최종 결과 계산
for i in range(n):
    for j in range(n):
        if light[i][j]:
            result += 1

print(result)
