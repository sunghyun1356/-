

# 방향 설정 (동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 초기 상태
dice = [0, 0, 0, 0, 0, 0]  # 윗면, 뒷면, 오른쪽, 왼쪽, 앞면, 아랫면

# 주사위 회전 함수
def roll_dice(direction):
    global dice
    if direction == 1:  # 동
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 2:  # 서
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 3:  # 북
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direction == 4:  # 남
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

# 입력 받기
N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 명령 처리
for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]

    # 이동할 위치가 지도를 벗어나면 무시
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    # 주사위 굴리기
    roll_dice(command)

    # 이동한 칸의 수가 0인 경우
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]  # 주사위의 밑면 값 복사
    else:
        dice[5] = graph[nx][ny]  # 칸의 값을 주사위 밑면으로 복사
        graph[nx][ny] = 0  # 칸의 값은 0으로 설정

    # 주사위의 윗면 값 출력
    print(dice[0])

    # 위치 갱신
    x, y = nx, ny
