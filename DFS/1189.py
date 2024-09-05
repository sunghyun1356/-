r, c, k = map(int, input().split())
graph = [list(input()) for _ in range(r)]
count = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False] * c for _ in range(r)]

def dfs(graph,visited, y,x,time):
    global count
    if y == 0 and x == c-1:
        if time == k:
            count+=1
            return 
        else:
            return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<c and 0<=ny<r:
            if visited[ny][nx] == False and graph[ny][nx] == ".":
                visited[ny][nx] = True
                dfs(graph, visited, ny, nx, time+1)
                visited[ny][nx] = False
visited[r-1][0] = True
dfs(graph, visited, r-1, 0, 1)
print(count)