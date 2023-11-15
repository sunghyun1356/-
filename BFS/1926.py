"""문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

예제 입력 1 
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
예제 출력 1 
4
9"""
# 총 가로 세로 대각선으로 3번 이동한다
# 만약에 세로 대각선 가로가 모두 1 이면 이동을 하고 아니면 안한다
import sys
input = sys.stdin.readline
from collections import deque

n , m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            
            if nx <0 or nx >= n or ny <0 or ny >=m:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] =0
                q.append((nx,ny))
                count +=1
    return count
                        
    
paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] ==1:
            paint.append(bfs(graph, i, j))                

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))         
    