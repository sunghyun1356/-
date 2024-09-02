from collections import deque
import sys
input = sys.stdin.readline

# 말의 이동 방향 (8방향)
horse_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
# 일반 이동 방향 (4방향)
monkey_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(graph, k, w, h):
    queue = deque([(0, 0, 0, k)])  # (y, x, 이동 횟수, 남은 말의 움직임 수)
    visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][k] = True

    while queue:
        y, x, dist, horse_left = queue.popleft()

        # 목적지 도달 시
        if y == h - 1 and x == w - 1:
            return dist

        # 말의 이동
        if horse_left > 0:
            for dy, dx in horse_moves:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx][horse_left - 1] and graph[ny][nx] == 0:
                    visited[ny][nx][horse_left - 1] = True
                    queue.append((ny, nx, dist + 1, horse_left - 1))

        # 일반 이동
        for dy, dx in monkey_moves:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx][horse_left] and graph[ny][nx] == 0:
                visited[ny][nx][horse_left] = True
                queue.append((ny, nx, dist + 1, horse_left))

    return -1  # 목적지에 도달할 수 없는 경우

# 입력 받기
k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

# 결과 출력
result = bfs(graph, k, w, h)
print(result)




