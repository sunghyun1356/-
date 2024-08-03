from collections import deque

n, m = map(int, input().split(" "))
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

maximum = 0

# 테트리미노를 만들어야하니까 각각을 하나씩 모양을 잡아주기 위해서 만들어준다
# dfs에서는 방문 했던 곳을 다시 풀어줘서 dfs가 끝나고 나서 다시 방문을 할 수 있게 만들어준다


def dfs(x,y,tmp,cnt):
    global maximum
    if cnt == 4:
        maximum = max(maximum, tmp)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<ny<n and 0<nx<m and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny,nx, tmp+graph[ny][nx], cnt+1)
            visited[ny][nx] = False
    
def ya(y,x):
    global maximum
    tmp = graph[y][x]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            arr.append(graph[ny][nx])
    length = len(arr)
    if length == 4:
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum((arr) + graph[y][x]))
    elif length == 3:
        maximum  = max(maximum, sum(arr) + graph[y][x])
    return

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,graph[i][j], 1)
        ya(i,j)
        visited[i][j] = False
        


# ㅗ ㅏ ㅓ ㅜ 모양빼고는 한가지모양에서 파생되어서 만들 수 있다
# 처음부터 끝까지 돌아주기



def bfs(i,j, temp, cnt):
    global maximum
    y = i
    x = j
    if cnt == 4:
        maximum = max(temp, maximum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
            visited[ny][nx] = True
            bfs(ny, nx, temp+graph[ny][nx], cnt+1)
            visited[ny,nx] = False

def ya(i,j, temp):
    # 상하좌우 모두다 보면서 그중에서 가장 작은거 빼준다
    global maximum
    arr = []
    for i in range(4):
        nx = j + dx[i]
        ny = i + dy[i]
        arr.append(graph[ny][nx])
    arr.sort(reverse=True)
    arr.pop()
    maximum = max(temp, sum(arr))

def main():
    for i in range(n):
        for j in range(m):
            visited[i,j] = True
            bfs(i,j)
            
            ya(i,j,maximum)
            visited[i,j] = False


import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# INPUT
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최대값 변수
maxValue = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            visited[ni][nj] = False


# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j):
    global maxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxValue)