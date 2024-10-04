# 딱 하나의 벽을 부술 수 있다.
# q에 담을때 이걸 뚫었는지 아닌지만 체크해주면 된다
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(input().rstrip())for _ in range(n)]
check = [[[0] * m for _ in range(n)] for _ in range(2)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque([(0,0,False)])
    check[False][0][0] = 1
    while q:
        y,x,choice = q.popleft()

        if y == n-1 and x == m-1:
            return check[True][n-1][m-1]+2
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if choice == False:
                    if graph[ny][nx] == "1":
                        check[choice][ny][nx] = check[choice][y][x] + 1
                        q.append((ny,nx,True))
                    else:
                        check[choice][ny][nx] = check[choice][y][x] + 1
                        q.append((ny,nx,False))
                else:
                    if graph[ny][nx] == "0":
                        check[choice][ny][nx] = check[choice][y][x] + 1
                        q.append((ny,nx,True))
    return -1
print(bfs())
