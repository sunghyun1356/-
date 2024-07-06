from collections import deque

r, l, n = map(int, input().split())
graph = [[0 for _ in range(l)] for _ in range(r)]
check = [[False for _ in range(l)] for _ in range(r)]



for i in range(n):
    row, col = map(int, input().split())
    graph[row - 1][col - 1] = 1

q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(a, b):
    q.append((a, b))
    check[a][b] = True  
    count = 1
    
    while q:
        row, col= q.popleft()
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if 0 <= nx < r and 0 <= ny < l:
                if not check[nx][ny] and graph[nx][ny] == 1:
                    check[row][col] = True
                    count+=1
                    q.append((nx, ny))

    return count

maximum = 0
for i in range(r):
    for j in range(l):
        if graph[i][j] == 1 and not check[i][j]: 
            maximum = max(maximum, BFS(i, j))
print(maximum)
