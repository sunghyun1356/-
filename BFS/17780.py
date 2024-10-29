dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
record = [[[] for _ in range(n)] for _ in range(n)]

horses_info = [[] for _ in range(k+1)]

# 말의 초기 위치와 방향 입력
for i in range(1, k+1):
    y, x, d = map(int, input().split())
    horses_info[i] = [i, y-1, x-1, d-1]
    record[y-1][x-1].append(i)

# 해당 말이 가장 아래에 있는지 확인
def is_bottom_horse(num, y, x):
    return record[y][x][0] == num

# 방향을 반대로 바꾸는 함수
def reverse_direction(direction):
    return 1 - direction if direction < 2 else 5 - direction

# 파란색 칸 상태를 확인하고 방향을 반대로 바꿔 처리
def next_move(y, x, d):
    ny, nx = y + dy[d], x + dx[d]

    # 경계 밖이거나 파란색 칸일 경우 방향 반대로
    if ny < 0 or nx < 0 or ny >= n or nx >= n or graph[ny][nx] == 2:
        d = reverse_direction(d)
        ny, nx = y + dy[d], x + dx[d]
        # 다시 이동할 위치가 경계 밖이거나 파란색일 경우 이동하지 않음
        if ny < 0 or nx < 0 or ny >= n or nx >= n or graph[ny][nx] == 2:
            return y, x, d

    # 다음 칸이 빨간색
    if graph[ny][nx] == 1:
        record[y][x].reverse()  # 말 순서 뒤집기
    # 말들을 이동시키기
    moving_horses = record[y][x]
    record[ny][nx].extend(moving_horses)
    record[y][x] = []
    # 말 정보 갱신
    for h in moving_horses:
        horses_info[h][1], horses_info[h][2], horses_info[h][3] = ny, nx, d

    return ny, nx, d

# 모든 말을 이동시키는 함수
def next_move_all():
    for horse in range(1, k+1):
        horse_num, y, x, d = horses_info[horse]
        if is_bottom_horse(horse_num, y, x):
            nx, ny, nd = next_move(y, x, d)
            horses_info[horse_num] = [horse_num, nx, ny, nd]

# 게임 종료 조건을 확인하는 함수
def finish():
    for i in range(n):
        for j in range(n):
            if len(record[i][j]) >= 4:
                return True
    return False

answer = -1
time = 1
while time <= 1000:
    next_move_all()
    if finish():
        answer = time
        break
    time += 1

print(answer)
