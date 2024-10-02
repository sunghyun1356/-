from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

blue, red, hole = None, None, None

# 오른쪽, 왼쪽, 아래, 위 순서로 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 파란 구슬, 빨간 구슬, 구멍 위치 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == "B":
            blue = (i, j)
        elif graph[i][j] == "R":
            red = (i, j)
        elif graph[i][j] == "O":  # 구멍은 "O"로 가정
            hole = (i, j)

# 구슬을 벽이나 구멍을 만날 때까지 이동시키는 함수
def move(y, x, dy, dx):
    steps = 0
    while graph[y + dy][x + dx] != "#" and graph[y][x] != "O":  # 벽 또는 구멍에 도달할 때까지 이동
        y += dy
        x += dx
        steps += 1
    return y, x, steps

def bfs():
    q = deque([(blue, red, 0)])
    visited = set()
    visited.add((blue, red))

    while q:
        now_blue, now_red, time = q.popleft()
        if time >= 10:
            return -1  # 10번 이상의 이동은 실패
        if now_blue == hole:  # 파란 구슬이 구멍에 들어가면 실패
            continue
        if now_red == hole:  # 빨간 구슬이 구멍에 들어가면 성공
            return time

        for i in range(4):  # 4방향으로 각각 이동
            # 파란 구슬과 빨간 구슬을 각각 움직임
            nby, nbx, blue_steps = move(*now_blue, dy[i], dx[i])
            nry, nrx, red_steps = move(*now_red, dy[i], dx[i])

            if (nby, nbx) == (nry, nrx):  # 두 구슬이 같은 위치에 도착하면
                if graph[nby][nbx] == "O":  # 구멍에 도착한 경우 무시
                    continue
                # 더 많이 이동한 구슬을 한 칸 뒤로
                if blue_steps > red_steps:
                    nby -= dy[i]
                    nbx -= dx[i]
                else:
                    nry -= dy[i]
                    nrx -= dx[i]

            # 두 구슬의 새로운 위치가 방문한 적 없는 상태라면 큐에 추가
            if ((nby, nbx), (nry, nrx)) not in visited:
                visited.add(((nby, nbx), (nry, nrx)))
                q.append(((nby, nbx), (nry, nrx), time + 1))

    return -1  # 10번 이내에 성공하지 못하면 실패

result = bfs()
print(result if 1 <= result <= 10 else -1)
