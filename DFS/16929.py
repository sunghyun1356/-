# 사이클을 찾아야한다
# 어떻게 찾을까?
# while로 오른쪽이랑 아래를 쭉 찾아주고 거기서 다시 하나는 아래로 하나는 밑으로 가는 걸로

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
# dfs 로 총 4번의 꺽이는 점이 존재하고 이때 마지막 값이 처음 값이 되면 된다

def dfs(y, x, color, start_y, start_x, time):
    global answer
    if answer:
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if time >= 4 and ny == start_y and nx == start_x:
            answer = True
            return
        if graph[ny][nx] == color and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, color, start_y, start_x, time + 1)
            visited[ny][nx] = False

answer = False
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, graph[i][j], i, j, 1)
            if answer:
                print("Yes")
                exit()
            visited[i][j] = False

print("No")

