dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
route = [(0, 0)]
block = []
direction = 0 
graph = [["#"] * 102 for _ in range(102)] 
n = int(input())
order = list(input())
i, j = 0, 0
visited = set([(i, j)]) 
graph[i][j] = "."

for index, o in enumerate(order):
    if o == "L":
        direction = (direction + 3) % 4
    elif o == "R":
        direction = (direction + 1) % 4
    elif o == "F":
        i, j = i + dy[direction], j + dx[direction]
        if (i, j) not in visited:
            graph[i][j] = "."
            visited.add((i, j))
            route.append((i, j))

    if index == len(order) - 1:
        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]
            if (ni, nj) not in visited:
                block.append((ni, nj))
                graph[ni][nj] = "#"

route_y = sorted(route, key=lambda x: x[0])
route_x = sorted(route, key=lambda x: x[1])
minimum_y, maximum_y = route_y[0][0], route_y[-1][0]
minimum_x, maximum_x = route_x[0][1], route_x[-1][1]

for i in range(minimum_y, maximum_y+1):
    for j in range(maximum_x, minimum_x-1,-1):
        print(graph[i][j], end="")
    print()
