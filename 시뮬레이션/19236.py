import sys
import copy

input = sys.stdin.readline

fish_graph = [[(0, 0) for _ in range(4)] for _ in range(4)]
fish_orders = []

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def fish_change(shark_y, shark_x, fish_graph, fish_orders):
    fish_orders = sorted(fish_orders, key=lambda x: x[0])
    for fish in fish_orders:
        fish_number, fish_direction, y, x = fish
        original_direction = fish_direction
        if fish_number == 0:
            continue
        temp = False
        for _ in range(8):
            ny = y + dy[fish_direction]
            nx = x + dx[fish_direction]

            if 0 <= ny < 4 and 0 <= nx < 4 and (ny != shark_y or nx != shark_x):
                fish_graph[y][x], fish_graph[ny][nx] = fish_graph[ny][nx], fish_graph[y][x]
                a,b = fish_graph[ny][nx]
                fish_graph[ny][nx]= (a, fish_direction)
                for f in fish_orders:
                    if f[0] == fish_number:
                        f[1], f[2], f[3] = fish_direction, ny, nx
                    elif f[2] == ny and f[3] == nx:
                        f[2], f[3] = y, x
                temp = True
                break
            fish_direction = (fish_direction + 1) % 8
            fish[1] = fish_direction
        if temp == False:
            fish[1] = original_direction
            
def shark_way_dfs(shark_y, shark_x, fish_graph, fish_orders, current_sum):
    global max_sum
    current_sum += fish_graph[shark_y][shark_x][0]
    max_sum = max(max_sum, current_sum)
    new_fish_graph = copy.deepcopy(fish_graph)
    new_fish_orders = copy.deepcopy(fish_orders)
    
    fish_number, shark_direction = new_fish_graph[shark_y][shark_x]
    fish_orders = [f for f in fish_orders if f[0] != fish_number]
    new_fish_graph[shark_y][shark_x] = (0, -1)
    for f in new_fish_orders:
        if f[0] == fish_number:
            f[0] = 0

    fish_change(shark_y, shark_x, new_fish_graph, new_fish_orders)
    for step in range(1, 4):
        ny = shark_y + dy[shark_direction] * step
        nx = shark_x + dx[shark_direction] * step
        if 0 <= ny < 4 and 0 <= nx < 4 and new_fish_graph[ny][nx][0] != 0:
            shark_way_dfs(ny, nx, new_fish_graph, new_fish_orders, current_sum)

def main():
    global max_sum
    max_sum = 0

    fish_orders = []
    for i in range(4):
        line = list(map(int, input().split()))
        for j in range(4):
            fish_number = line[2 * j]
            fish_direction = line[2 * j + 1] - 1
            fish_graph[i][j] = (fish_number, fish_direction)
            fish_orders.append([fish_number, fish_direction, i, j])

    first_fish_number, first_shark_direction = fish_graph[0][0]
    fish_orders = [f for f in fish_orders if f[0] != first_fish_number]

    shark_way_dfs(0, 0, fish_graph, fish_orders, first_fish_number)
    print(max_sum)

def solution():
    main()

solution()
