"""문제
상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.

매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
각 지도에 @의 개수는 하나이다.

출력
각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

예제 입력 1 
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
예제 출력 1 
2
5
IMPOSSIBLE
IMPOSSIBLE
IMPOSSIBLE"""

# 불 + 상근이 두개의 움직임 check를 두개를 둬야 할라나
# 불이 옮겨진 칸이나 옮겨질 칸으로 이동이 불가능하다
# 얼마나 빨리 가능한지
# 상근이가 욺직인 칸은 불이 붙을 곳이 아니면 .으로 변한다
# 불을 다 설정해놓고 이 곳의 시간보다 상근이의 시간이 적을때 이동이 가능하다
import sys
input = sys.stdin.readline

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(choice, queue, checking):
    while (queue):
        y, x, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 탈출 조건
                # 만약에 그 다음곳이 비엇거나 시작 단계쪽일때
                if building[ny][nx] == '.' or building[ny][nx] == '@':
                    # 만약에 불이난곳에 도달하는 시간이 지금까지의 시간보다 크다면
                    if checking[ny][nx] > cnt +1:
                        # 모든 곳을 가는데 그 중에 가장 시간이 적게 걸리는 것으로 만들어주기
                        # 왜냐면 방문한 곳인지 알 수 있는 곳이 없기 때문에
                        checking[ny][nx] = cnt +1
                        queue.append((ny,nx,checking[ny][nx]))
            # 탈출 조건에 도달 했다면
            elif choice == 's':
                print(cnt+1)
                return
    # 다 돌았는대도 탈출 조건에 도달하지 못했다면
    if choice == 's':
        print("IMPOSSIBLE")




n = int(input())
for z in range(n):
    n,m = map(int, input().split())
    building = [list(input().strip()) for _ in range(m)]
    # 안 간 곳이거나 더 많다면 초기화 해주기 위한 것
    check = [[1e9 for _ in range(n)] for _ in range(m)]
    
    fire = deque()
    sang = deque()
    for i in range(m):
        for j in range(n):
            if building[i][j] == '@':
                sang.append((i,j,0))
            elif building[i][j] == '*':
                check[i][j] = 0
                fire.append((i,j,0))
    bfs('f', fire, check)
    # 불이 도달하는 시간을 모두다 check로 설정해 놓는다
    bfs('s', sang, check)
    # s로 돌았을때 본인의 시간보다 check가 더 크다면 이동이 가능하다
    