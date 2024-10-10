from collections import deque

def solution(board):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    graph = [list(row) for row in board]
    
    red, green = None, None
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "R":
                red = (i, j)
            elif graph[i][j] == "G":
                green = (i, j)
    
    def slide(position, direction, graph):
        y, x = position
        if direction == 0: 
            while x + 1 < len(graph[0]) and graph[y][x + 1] != "D":
                x += 1
        elif direction == 1: 
            while x - 1 >= 0 and graph[y][x - 1] != "D":
                x -= 1
        elif direction == 2: 
            while y + 1 < len(graph) and graph[y + 1][x] != "D":
                y += 1
        elif direction == 3:
            while y - 1 >= 0 and graph[y - 1][x] != "D":
                y -= 1
        return (y, x)
    
    def bfs(red, green):
        q = deque([(red, 0)])
        visited = [[False] * len(graph[0]) for _ in range(len(graph))]
        visited[red[0]][red[1]] = True
        
        while q:
            red_p, time = q.popleft()
            if red_p == green:
                return time
            for i in range(4):
                ny, nx = slide(red_p, i, graph)
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append(((ny, nx), time + 1))
        
        return -1
    
    return bfs(red, green)
