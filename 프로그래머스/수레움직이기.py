from collections import deque

# 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(maze):
    # 각각의 정보 저장
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                red_car = (i, j)
            elif maze[i][j] == 2:
                blue_car = (i, j)
            elif maze[i][j] == 3:
                red_dest = (i, j)
            elif maze[i][j] == 4:
                blue_dest = (i, j)
    
    def bfs(red_car, blue_car, red_dest, blue_dest):
        # 각각의 차에 대해 방문 체크
        red_visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        blue_visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        
        red_visited[red_car[0]][red_car[1]] = True
        blue_visited[blue_car[0]][blue_car[1]] = True
        
        # 큐에 초기 상태 (red, blue, 시간) 저장
        q = deque([(red_car, blue_car, 0, red_visited, blue_visited)])
        
        while q:
            red, blue, time, red_visited, blue_visited = q.popleft()
            ry, rx = red
            by, bx = blue
            
            # 두 차 모두 목적지에 도착한 경우
            if red == red_dest and blue == blue_dest:
                return time
            
            # 4방향 탐색
            for i in range(4):
                for j in range(4):
                    nry = ry + dy[j]
                    nrx = rx + dx[j]
                    nby = by + dy[i]
                    nbx = bx + dx[i]
                    
                    if red == red_dest:
                        nry, nrx = ry, rx

                    if blue == blue_dest:
                        nby, nbx = by, bx

                    if nry == nby and nrx == nbx:
                        continue
                    if (nry == by and nrx == bx) and (nby == ry and nbx == rx):
                        continue
                        
                    # 범위 체크 및 벽 확인
                    if (0 <= nry < len(maze) and 0 <= nrx < len(maze[0])) and (0 <= nby < len(maze) and 0 <= nbx < len(maze[0])) and (maze[nry][nrx] != 5) and (maze[nby][nbx] != 5):

                        # 방문 체크
                        if not red_visited[nry][nrx] or not blue_visited[nby][nbx]:
                            new_red_visited = [row[:] for row in red_visited]
                            new_blue_visited = [row[:] for row in blue_visited]
                            new_red_visited[nry][nrx] = True
                            new_blue_visited[nby][nbx] = True
                            q.append(((nry, nrx), (nby, nbx), time + 1, new_red_visited, new_blue_visited))
        
        return 0  # 도달 불가능할 경우
    
    return bfs(red_car, blue_car, red_dest, blue_dest)
