"""문제
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

예제 입력 1 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1 
27
예제 입력 2 
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
예제 출력 2 
9
예제 입력 3 
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
예제 출력 3 
3"""
import sys
input = sys.stdin.readline
from collections import deque


import copy

# 계속 구할 것인가, 어디에 막을 것인가 -> 2근처에 바로 다 막는것이 최고다 2를 먼저 찾고 그 상하좌우에 넣는데 느게 안되면 끝이다.
# 3개보다 더 많을 때 어떻게 할 것인가
# 2주변의 모든 부분의 값들을 설정해놓고 할것인가?
# 그냥 기준이 애매하니까 0인거 찾아서 하나씩 넣어주고 빼고를 반복해주자
# BFS는 기준에 따라서 계속 새로운거 COPY하고 2로 채워주기
from itertools import combinations


def BFS(buildings):
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(n):
        for j in range(m):
            if buildings[i][j] == 2:
                q.append((i, j))
                
    while q:
        iy, ix = q.popleft()
        for i in range(4):
            nx = dx[i] + ix
            ny = dy[i] + iy
            if 0 <= nx < m and 0 <= ny < n:
                if buildings[ny][nx] == 0:
                    buildings[ny][nx] = 2
                    q.append((ny, nx))
    
    # 바이러스 전파 후 안전 영역 크기 계산
    cnt = sum(row.count(0) for row in buildings)
    return cnt

n, m = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]

# 0인 위치의 조합을 뽑아내는 부분
empty_spaces = [(i, j) for i in range(n) for j in range(m) if building[i][j] == 0]
combinations_empty = combinations(empty_spaces, 3)

answer = 0

for combination in combinations_empty:
    # 가능한 벽을 미리 세운 후에 BFS를 통해 안전 영역 크기 계산
    temp_building = [row[:] for row in building]
    for i, j in combination:
        temp_building[i][j] = 1
    answer = max(answer, BFS(temp_building))

print(answer)

     
                    
                
