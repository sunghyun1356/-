import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def falling(graph):
    for j in range(6):
        for i in range(10, -1, -1):  # 바닥부터 위로
            if graph[i][j] != '.':
                ni = i
                while ni < 11 and graph[ni + 1][j] == '.':
                    graph[ni + 1][j], graph[ni][j] = graph[ni][j], '.'
                    ni += 1

def popping(graph):
    count_sum = 0
    visited = [[False for _ in range(6)] for _ in range(12)]

    def dfs(y, x, color):
        q = deque([(y, x)])
        popped = []
        while q:
            cy, cx = q.popleft()
            if visited[cy][cx]:
                continue
            visited[cy][cx] = True
            popped.append((cy, cx))
            for k in range(4):
                ny = cy + dy[k]
                nx = cx + dx[k]
                if 0 <= ny < 12 and 0 <= nx < 6 and graph[ny][nx] == color and not visited[ny][nx]:
                    q.append((ny, nx))
        return popped

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                popped = dfs(i, j, graph[i][j])
                if len(popped) >= 4:
                    count_sum += 1
                    for y, x in popped:
                        graph[y][x] = '.'

    return count_sum

def main():
    graph = [list(input().strip()) for _ in range(12)]
    total_pops = 0

    while True:
        temp = popping(graph)

        if temp == 0:
            break
        else:
            total_pops+=1
        falling(graph)

    print(total_pops)

if __name__ == "__main__":
    main()
