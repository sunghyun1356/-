n, m, t = map(int, input().split())
round_round = [list(map(int, input().split())) for _ in range(n)]
order = []
for _ in range(t):
    a, b, c = map(int, input().split())
    order.append((a, b, c))

def rotate(board, num, way, times):
    for index in range(len(board)):
        if (index + 1) % num == 0:
            if way == 1:
                # 반시계 방향 회전
                board[index] = board[index][times:] + board[index][:times]
            else:
                # 시계 방향 회전
                board[index] = board[index][-times:] + board[index][:-times]
    return board

def delete(board):
    temp_temp = False
    n, m = len(board), len(board[0])
    temp_board = [row[:] for row in board]  # 기존 값을 복사해 둠

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                # 상하좌우 비교
                if i > 0 and board[i][j] == board[i-1][j]:
                    temp_board[i][j] = temp_board[i-1][j] = 0
                    temp_temp = True
                if i < n - 1 and board[i][j] == board[i+1][j]:
                    temp_board[i][j] = temp_board[i+1][j] = 0
                    temp_temp = True
                if board[i][j] == board[i][(j+1) % m]:
                    temp_board[i][j] = temp_board[i][(j+1) % m] = 0
                    temp_temp = True
                if board[i][j] == board[i][(j-1) % m]:
                    temp_board[i][j] = temp_board[i][(j-1) % m] = 0
                    temp_temp = True

    if not temp_temp:
        # 인접한 것이 없을 경우 평균 처리
        total, count = 0, 0
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    total += board[i][j]
                    count += 1
        if count > 0:
            avg = total / count
            for i in range(n):
                for j in range(m):
                    if board[i][j] != 0:
                        if board[i][j] > avg:
                            board[i][j] -= 1
                        elif board[i][j] < avg:
                            board[i][j] += 1
    else:
        board = temp_board
    return board

for time in range(t):
    round_round = rotate(round_round, order[time][0], order[time][1], order[time][2])
    round_round = delete(round_round)

# 최종 합 계산
result = sum(sum(row) for row in round_round)
print(result)
