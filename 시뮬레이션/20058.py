"""문제
마법사 상어는 파이어볼과 토네이도를 조합해 파이어스톰을 시전할 수 있다. 오늘은 파이어스톰을 크기가 2N × 2N인 격자로 나누어진 얼음판에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 얼음의 양을 의미한다. A[r][c]가 0인 경우 얼음이 없는 것이다.

파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정해야 한다. 파이어스톰은 먼저 격자를 2L × 2L 크기의 부분 격자로 나눈다. 그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다. 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다. 아래 그림의 칸에 적힌 정수는 칸을 구분하기 위해 적은 정수이다.

		
마법을 시전하기 전	L = 1	L = 2
마법사 상어는 파이어스톰을 총 Q번 시전하려고 한다. 모든 파이어스톰을 시전한 후, 다음 2가지를 구해보자.

남아있는 얼음 A[r][c]의 합
남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.

입력
첫째 줄에 N과 Q가 주어진다. 둘째 줄부터 2N개의 줄에는 격자의 각 칸에 있는 얼음의 양이 주어진다. r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.

마지막 줄에는 마법사 상어가 시전한 단계 L1, L2, ..., LQ가 순서대로 주어진다.

출력
첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고, 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력한다. 단, 덩어리가 없으면 0을 출력한다.

제한
2 ≤ N ≤ 6
1 ≤ Q ≤ 1,000
0 ≤ A[r][c] ≤ 100
0 ≤ Li ≤ N
예제 입력 1 
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1
예제 출력 1 
284
64
예제 입력 2 
3 2
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2
예제 출력 2 
280
64
예제 입력 3 
3 5
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 0 3 2
예제 출력 3 
268
64
예제 입력 4 
3 10
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 0 3 2 1 2 3 2 3
예제 출력 4 
248
62
예제 입력 5 
3 10
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 1 2 3 1 2 3 1
예제 출력 5 
246
60
예제 입력 6 
3 10
1 0 3 4 5 6 7 0
8 0 6 5 4 3 2 1
1 2 0 4 5 6 7 0
8 7 6 5 4 3 2 1
1 2 3 4 0 6 7 0
8 7 0 5 4 3 2 1
1 2 3 4 5 6 7 0
0 7 0 5 4 3 2 1
1 2 3 1 2 3 1 2 3 1
예제 출력 6 
37
9"""

import sys
input = sys.stdin.readline
from collections import deque
n,q = map(int, input().split())


N = 2**n

graph =[]
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

L = list(map(int,input().split()))


# 돌려주기
def rotate_matrix(matrix):
    # 주어진 행렬의 행과 열의 길이
    rows = len(matrix)
    cols = len(matrix[0])

    # 새로운 행렬 생성 (행과 열이 바뀜)
    rotated_matrix = [[0] * rows for _ in range(cols)]

    # 원본 행렬을 90도 시계 방향으로 회전
    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - 1 - i] = matrix[i][j]

    return rotated_matrix

def divide(graph, l):
    # 원래 그래프의 크기
    N = len(graph)
    
    # 1번째 2번쨰.... 부터 
    for i in range(0, N, 2**l):
        for j in range(0, N, 2**l):
            row_index = i
            col_index = j
            focus_graph = [row[col_index:col_index+(2**l)] for row in graph[row_index:row_index+(2**l)]]
            # 나눠진 부분을 90도 시계 방향으로 회전
            rotated_focus_graph = rotate_matrix(focus_graph)

            # 회전된 부분을 원래 위치에 업데이트
            for r in range(2**l):
                for c in range(2**l):
                    graph[row_index + r][col_index + c] = rotated_focus_graph[r][c]



check = [[0 for _ in range(N)] for _ in range(N)]

def BFS(i, j, cnt):
    q = deque()
    global check
    q.append((i, j))
    check[i][j] = cnt
    component_size = 1  # Initialize the size of the connected component
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        y, x = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[ny][nx] != 0 and check[ny][nx] == 0:
                    check[ny][nx] = cnt  # Assign the component number to the current point
                    q.append((ny, nx))
                    component_size += 1  # Increment the size of the connected component

    return component_size
    
            
#주위에 얼음이 있는 칸이 3개또는 그 이상이 있는지 체크
def ice():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                dx = [1,-1,0,0]
                dy = [0,0,1,-1]
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0<=nx<N  and 0<=ny<N:
                        if graph[ny][nx] > 0:
                            cnt+=1
                if cnt <3:
                    graph[i][j] -=1


def first(graph):
    result_1 = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                result_1 += graph[i][j]
    return result_1

def second(check):
    maximum = 0
    for i in range(N):
        for j in range(N):
            if maximum <= check[i][j]:
                maximum = check[i][j]
    return maximum

for i in L:
    divide(graph,i)
    print(graph)
    print()
    ice()
    print(graph)
    print()
cnt = 0
maximum = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] >0 and check[i][j]==0:
            cnt+=1
            maximum = max(maximum, BFS(i,j,cnt))

print(first(graph)-3*q)
print(maximum)