import sys
input = sys.stdin.readline

# 방향 벡터 (0: 위, 1: 아래, 2: 왼쪽, 3: 오른쪽)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def each_shark_move(shark_number, shark_y, shark_x, shark_direction, shark_info, shark_graph, shark_smell, n):
    moved = False
    for dir in shark_info[shark_number-1][shark_direction-1]:
        ny = shark_y + dy[dir-1]
        nx = shark_x + dx[dir-1]
        if 0 <= ny < n and 0 <= nx < n:
            # 냄새가 없는 칸으로 이동
            if all(shark_smell[k][ny][nx] == 0 for k in range(len(shark_smell))):
                shark_graph[shark_y][shark_x] = 0  # 현재 위치에서 상어 제거
                shark_graph[ny][nx] = shark_number  # 새로운 위치로 이동
                shark_direction = dir  # 방향 업데이트
                moved = True
                break

    if not moved:
        # 아무 냄새가 없는 칸이 없다면, 자신의 냄새가 있는 칸으로 이동
        for dir in shark_info[shark_number-1][shark_direction-1]:
            ny = shark_y + dy[dir-1]
            nx = shark_x + dx[dir-1]
            if 0 <= ny < n and 0 <= nx < n:
                if shark_smell[shark_number-1][ny][nx] > 0:
                    shark_graph[shark_y][shark_x] = 0
                    shark_graph[ny][nx] = shark_number
                    shark_direction = dir
                    break
    return ny, nx, shark_direction

def shark_move(shark_directions, shark_info, shark_graph, shark_smell, n):
    new_shark_directions = []
    new_positions = {}

    for shark in shark_directions:
        shark_number, shark_y, shark_x, shark_direction = shark
        new_y, new_x, new_direction = each_shark_move(shark_number, shark_y, shark_x, shark_direction, shark_info, shark_graph, shark_smell, n)
        
        if (new_y, new_x) in new_positions:
            if shark_number < new_positions[(new_y, new_x)]:
                # 더 작은 번호의 상어만 남기고 제거
                new_positions[(new_y, new_x)] = shark_number
        else:
            new_positions[(new_y, new_x)] = shark_number

    for (y, x), shark_number in new_positions.items():
        for sd in shark_directions:
            if sd[0] == shark_number:
                new_shark_directions.append((shark_number, y, x, sd[3]))
                break

    shark_directions.clear()
    shark_directions.extend(new_shark_directions)
    return shark_directions

def decrease_smell(shark_smell, n, m):
    for i in range(n):
        for j in range(n):
            for k in range(m):
                if shark_smell[k][i][j] > 0:
                    shark_smell[k][i][j] -= 1

def main():
    n, m, k = map(int, input().split())
    shark_graph = [list(map(int, input().split())) for _ in range(n)]
    shark_directions = []
    shark_direction = list(map(int, input().split()))
    shark_smell = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]
    shark_info = [[] for _ in range(m)]

    # 상어 초기 설정
    for i in range(n):
        for j in range(n):
            if shark_graph[i][j] != 0:
                shark_number = shark_graph[i][j]
                shark_directions.append((shark_number, i, j, shark_direction[shark_number - 1]))
                shark_smell[shark_number-1][i][j] = k

    # 각 상어의 우선순위 정보 입력
    for i in range(m):
        temp = []
        for _ in range(4):
            temp.append(list(map(int, input().split())))
        shark_info[i] = temp

    time = 0
    while time <= 1000:
        if len(shark_directions) == 1:
            shark_number, _, _, _ = shark_directions[0]
            if shark_number == 1:
                print(time)
                return
        
        # 상어 이동
        shark_directions = shark_move(shark_directions, shark_info, shark_graph, shark_smell, n)

        # 냄새 감소
        decrease_smell(shark_smell, n, m)

        # 새로운 냄새 추가
        for shark_number, y, x, _ in shark_directions:
            shark_smell[shark_number-1][y][x] = k

        time += 1

    print(-1)

def solution():
    main()

solution()
