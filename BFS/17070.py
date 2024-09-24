def dfs(position):
    global result
    x, y, dir = position
    if x == n - 1 and y == n - 1:
        result += 1
        return
    if x + 1 < n and y + 1 < n: # 대각선 이동
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs((x + 1, y + 1, 2))
    if dir == 0 or dir == 2: # 세로 이동
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs((x, y + 1, 0))
    if dir == 1 or dir == 2: # 가로 이동
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs((x + 1, y, 1))


n = int(input())
graph = [[] for _ in range(n)]
result = 0
# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

dfs((0, 1, 0))

print(result)