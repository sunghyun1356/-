import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

# 동전의 시작 위치를 찾기 위한 리스트
coins = []

dx = [1, -1, 0, 0]  # x 방향 이동 (오른쪽, 왼쪽)
dy = [0, 0, 1, -1]  # y 방향 이동 (아래, 위)

# 동전 위치 찾기
def find_coins(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "o":
                coins.append((i, j))
    return coins

# 범위 체크 함수
def out(y, x):
    return not (0 <= y < n and 0 <= x < m)

# BFS 탐색
def bfs(fy, fx, sy, sx):
    q = deque([(fy, fx, sy, sx, 0)])  # y1, x1, y2, x2, 시간
    visited = set()  # 방문한 상태 기록
    visited.add((fy, fx, sy, sx))
    
    while q:
        fy, fx, sy, sx, time = q.popleft()
        
        # 동전 하나가 떨어졌을 경우
        if out(fy, fx) and out(sy, sx):
            continue
        if out(fy, fx) or out(sy, sx):
            return time  # 하나의 동전이 떨어진 경우
        
        # 이동
        for i in range(4):
            nfy, nfx = fy + dy[i], fx + dx[i]  # 첫 번째 동전 이동
            nsy, nsx = sy + dy[i], sx + dx[i]  # 두 번째 동전도 같은 방향으로 이동

            # 벽 처리
            if 0 <= nfy < n and 0 <= nfx < m and graph[nfy][nfx] == "#":
                nfy, nfx = fy, fx  # 첫 번째 동전은 원래 위치 유지
            if 0 <= nsy < n and 0 <= nsx < m and graph[nsy][nsx] == "#":
                nsy, nsx = sy, sx  # 두 번째 동전은 원래 위치 유지
            
            # 새로운 상태가 방문한 적 없는 상태라면 큐에 추가
            if (nfy, nfx, nsy, nsx) not in visited:
                visited.add((nfy, nfx, nsy, nsx))
                q.append((nfy, nfx, nsy, nsx, time + 1))

    return -1  # 둘 다 떨어지지 않는 경우

# 동전 위치 찾기
coins = find_coins(graph)
if len(coins) != 2:
    print(-1)
else:
    first_coin = coins[0]
    second_coin = coins[1]

    # BFS 실행
    result = bfs(first_coin[0], first_coin[1], second_coin[0], second_coin[1])
    print(result if result < 10 else -1)  # 결과 출력
