import sys
from collections import deque
from itertools import product, permutations

# 상하좌우위아래로 움직이기
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

total_maze = []
for i in range(5):
    total_maze.append([list(map(int, input().split())) for _ in range(5)])

def rotate(order):
    rotations = [order]  # 0도 회전 상태 그대로 추가
    for _ in range(3):
        order = [list(row) for row in zip(*order[::-1])]
        rotations.append(order)
    return rotations

# 각 층을 회전시켜 가능한 모든 상태를 만듭니다.
def graph_rotate(graph):
    return [rotate(graph[i]) for i in range(5)]

# 미로를 BFS로 탐색하여 최단 거리를 찾습니다.
def bfs(graph):
    if graph[0][0][0] == 0 or graph[4][4][4] == 0:  # 시작점이나 도착점이 막혀있는 경우
        return -1
    
    q = deque([(0, 0, 0, 0)])
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True

    while q:
        z, y, x, time = q.popleft()
        if z == 4 and y == 4 and x == 4:
            return time
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and not visited[nz][ny][nx] and graph[nz][ny][nx] == 1:
                visited[nz][ny][nx] = True
                q.append((nz, ny, nx, time + 1))
    return -1

def main(graph):
    minimum_time = float('inf')  # 최단 시간을 무한대로 초기화
    graph_rotations = graph_rotate(graph)  # 미로의 모든 회전 상태를 미리 계산

    # 각 층의 순서를 조합하고, 중복되는 경우는 제외합니다.
    for order in permutations(range(5)):
        for rotations in product(*[graph_rotations[i] for i in order]):
            result = bfs(rotations)
            if result != -1:
                minimum_time = min(minimum_time, result)
    
    if minimum_time == float('inf'):
        minimum_time = -1
    print(minimum_time)

main(total_maze)
