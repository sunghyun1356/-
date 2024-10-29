# 모든 공간을 모두 다 가볼 것인가??

stack = []

graph = [list(map(int, input().split())) for _ in range(5)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
candidates = set()
def dfs(i,j,candidate):
    if len(candidate)==6:
        candidates.add(candidate)
        return
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if 0<=ny<5 and 0<=nx<5:
            dfs(ny,nx,candidate+str(graph[ny][nx]))
for i in range(5):
    for j in range(5):
        dfs(i,j,"")
print(len(candidates))