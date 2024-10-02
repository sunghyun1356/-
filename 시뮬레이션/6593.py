from collections import deque
import sys
input = sys.stdin.readline

# 방향: 오른쪽, 왼쪽, 위, 아래, 위층, 아래층
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    # 건물과 방문 배열 초기화
    building = []
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]

    # 건물 구조 읽기
    for k in range(l):
        layer = [list(input().rstrip()) for _ in range(r)]
        building.append(layer)
        if k < l - 1:
            input()  # 층 사이의 빈 줄을 읽기 위한 입력 (마지막 층 제외)
    input()
    start = None
    end = None

    # 시작과 끝 위치 찾기
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if building[k][i][j] == "S":
                    start = (k, i, j)
                elif building[k][i][j] == "E":
                    end = (k, i, j)

    q = deque([start])
    sz, sy, sx = start
    visited[sz][sy][sx] = 0

    # BFS 구현
    while q:
        z, y, x = q.popleft()
        
        # 끝에 도달했는지 확인
        if (z, y, x) == end:
            print(f"Escaped in {visited[z][y][x]} minute(s)")
            break

        # 이웃 탐색
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c:
                if building[nz][ny][nx] == "." and visited[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nz, ny, nx))
    else:
        # break 없이 while을 종료하면 끝을 찾지 못한 것
        print("Trapped")
