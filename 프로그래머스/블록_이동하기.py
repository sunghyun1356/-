from collections import deque

def bfs(board, length):
    # 큐에 블록의 초기 상태(가로로 (0, 0)과 (0, 1)에 위치)를 추가합니다.
    q = deque([(0, 0, 0, 1)])  # 시작점 (0, 0)과 (0, 1) (가로 상태)
    # 이동 횟수를 저장할 배열을 초기화합니다.
    counting = [[[[1e9] * length for _ in range(length)] for _ in range(length)] for _ in range(length)]
    counting[0][0][0][1] = 0
    visited = set()  # 방문한 위치를 저장할 집합
    visited.add((0, 0, 0, 1))
    
    # BFS 루프
    while q:
        fy, fx, sy, sx = q.popleft()
        
        # 블록이 목표 지점에 도착했는지 확인합니다.
        if (fy == length - 1 and fx == length - 1) or (sy == length - 1 and sx == length - 1):
            return counting[fy][fx][sy][sx]
        
        # 이동 가능한 방향 (상, 하, 좌, 우)와 회전 처리
        moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # 위, 아래, 왼쪽, 오른쪽
        ]
        
        # 블록을 이동시킵니다 (두 부분이 함께 이동)
        for dy, dx in moves:
            nfy, nfx = fy + dy, fx + dx
            nsy, nsx = sy + dy, sx + dx
            if 0 <= nfy < length and 0 <= nfx < length and 0 <= nsy < length and 0 <= nsx < length:
                if board[nfy][nfx] == 0 and board[nsy][nsx] == 0:
                    if (nfy, nfx, nsy, nsx) not in visited:
                        q.append((nfy, nfx, nsy, nsx))
                        visited.add((nfy, nfx, nsy, nsx))
                        counting[nfy][nfx][nsy][nsx] = counting[fy][fx][sy][sx] + 1
        
        # 블록이 가로로 놓여 있을 때 회전 처리
        if fy == sy:  # 블록이 가로로 놓인 경우
            # 시계 방향 및 반시계 방향 회전
            for dy in [-1, 1]:  # 블록 위쪽과 아래쪽을 확인
                if 0 <= fy + dy < length and board[fy + dy][fx] == 0 and board[sy + dy][sx] == 0:
                    # 왼쪽 부분을 오른쪽을 기준으로 회전
                    if (fy + dy, fx, fy, fx) not in visited:
                        q.append((fy + dy, fx, fy, fx))
                        visited.add((fy + dy, fx, fy, fx))
                        counting[fy + dy][fx][fy][fx] = counting[fy][fx][sy][sx] + 1
                    # 오른쪽 부분을 왼쪽을 기준으로 회전
                    if (sy + dy, sx, sy, sx) not in visited:
                        q.append((sy + dy, sx, sy, sx))
                        visited.add((sy + dy, sx, sy, sx))
                        counting[sy + dy][sx][sy][sx] = counting[fy][fx][sy][sx] + 1

        # 블록이 세로로 놓여 있을 때 회전 처리
        if fx == sx:  # 블록이 세로로 놓인 경우
            # 시계 방향 및 반시계 방향 회전
            for dx in [-1, 1]:  # 블록 왼쪽과 오른쪽을 확인
                if 0 <= fx + dx < length and board[fy][fx + dx] == 0 and board[sy][sx + dx] == 0:
                    # 위쪽 부분을 아래쪽을 기준으로 회전
                    if (fy, fx + dx, fy, fx) not in visited:
                        q.append((fy, fx + dx, fy, fx))
                        visited.add((fy, fx + dx, fy, fx))
                        counting[fy][fx + dx][fy][fx] = counting[fy][fx][sy][sx] + 1
                    # 아래쪽 부분을 위쪽을 기준으로 회전
                    if (sy, sx + dx, sy, sx) not in visited:
                        q.append((sy, sx + dx, sy, sx))
                        visited.add((sy, sx + dx, sy, sx))
                        counting[sy][sx + dx][sy][sx] = counting[fy][fx][sy][sx] + 1

    return -1  # 목표에 도달할 수 없으면 -1 반환

def solution(board):
    length = len(board)
    return bfs(board, length)
