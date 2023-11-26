"""문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1"""

#check로 누적을 구해주기
# 벽 부섰는지 튜플로 저장하기
# 벽을 부순 곳이 있다면 그 위치를 저장해주기
# BFS(인 곳을 하나씩 0으로 처리해주고 할것인가 아니면 그냥 바로 돌면서 처리를 해줄것인가)
import sys
input = sys.stdin.readline


# 뚫은 곳 위치를 저장해주고 그걸 pop하고 나서 욺직여 준다
# checking으로 누적된것을 해주고
from collections import deque

n, m = map(int, input().split())
building = [list(input().strip()) for _ in range(n)]
checking = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)] 

def BFS():
    q = deque()
    q.append((0, 0, 0))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        now_y, now_x, choice = q.popleft()

        if now_y == n-1 and now_x == m-1:
            return checking[now_y][now_x][choice] +1

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if building[ny][nx] == "1" and choice == 0:
                    checking[ny][nx][1] = checking[now_y][now_x][0] + 1
                    q.append((ny, nx,1))
                elif building[ny][nx] == "0" and checking[ny][nx][choice] == 0:
                    checking[ny][nx][choice] = checking[now_y][now_x][choice] + 1
                    q.append((ny, nx, choice))

    return -1

print(BFS())