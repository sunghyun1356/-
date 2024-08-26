import sys
input = sys.stdin.readline

# 방향 정의 (좌, 하, 우, 상)
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 비율 배열 (왼쪽 기준) 및 방향 회전 함수
def rotate_90(proportion):
    new_proportion = list(reversed(list(zip(*proportion))))
    return new_proportion

p = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)
proportions = [p, p1, p2, p3]
alphas = [(2, 1), (3, 2), (2, 3), (1, 2)] 

def rotate(graph, y, x, d, value, n, left):
    proportion = proportions[d]
    alpha = alphas[d]

    left_sand = value

    # 비율에 따른 모래 이동
    for r in range(5):
        for c in range(5):
            if proportion[r][c] == 0:
                continue
            move_sand = int(value * proportion[r][c])
            ny = y + r - 2
            nx = x + c - 2
            if 0 <= ny < n and 0 <= nx < n:
                graph[ny][nx] += move_sand
            else:
                left += move_sand
            left_sand -= move_sand

    # 알파 위치에 남은 모래 이동
    alpha_y = y + alpha[0] - 2
    alpha_x = x + alpha[1] - 2
    if 0 <= alpha_y < n and 0 <= alpha_x < n:
        graph[alpha_y][alpha_x] += left_sand
    else:
        left += left_sand

    return left

def move(graph, n):
    y, x = n // 2, n // 2  # 허리케인 시작 위치 (중앙)
    left = 0  # 격자 밖으로 나간 모래의 총량
    d = 0  # 초기 방향 (왼쪽)
    curl = 0  # 현재 토네이도 방향
    turn = 2  # 방향 전환 기준
    length = 1  # 현재 이동 길이

    while not (y == 0 and x == 0):
        for _ in range(2):  # 같은 길이로 두 번 이동
            for _ in range(length):
                if y == 0 and x == 0:
                    print(left)
                    return

                y += delta[curl][0]
                x += delta[curl][1]

                if graph[y][x] > 0:
                    left = rotate(graph, y, x, curl, graph[y][x], n, left)
                    graph[y][x] = 0

            curl = (curl + 1) % 4
            if curl % 2 == 0:
                length += 1

    print(left)

def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    move(graph, n)

if __name__ == "__main__":
    main()
