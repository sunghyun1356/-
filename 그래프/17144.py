import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def spread_dust(graph, r, c):
    new_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0: 
                spread_amount = graph[i][j] // 5
                spread_count = 0
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]
                    if 0 <= ni < r and 0 <= nj < c and graph[ni][nj] != -1:
                        new_graph[ni][nj] += spread_amount
                        spread_count += 1
                new_graph[i][j] += graph[i][j] - spread_amount * spread_count
            else:
                new_graph[i][j] += graph[i][j]
    return new_graph

def operate_air_cleaner(graph, upper, lower, r, c):
    for i in range(upper - 1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(0, c - 1):
        graph[0][i] = graph[0][i + 1]
    for i in range(0, upper):
        graph[i][c - 1] = graph[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
        graph[upper][i] = graph[upper][i - 1]
    graph[upper][1] = 0

 
    for i in range(lower + 1, r - 1):
        graph[i][0] = graph[i + 1][0]
    for i in range(0, c - 1):
        graph[r - 1][i] = graph[r - 1][i + 1]
    for i in range(r - 1, lower, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        graph[lower][i] = graph[lower][i - 1]
    graph[lower][1] = 0 

def main():
    r, c, t = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(r)]

    air_cleaner = []
    for i in range(r):
        if graph[i][0] == -1:
            air_cleaner.append(i)

    upper, lower = air_cleaner

    for _ in range(t):
        graph = spread_dust(graph, r, c) 
        operate_air_cleaner(graph, upper, lower, r, c)

    result = sum(sum(row) for row in graph) + 2
    print(result)

if __name__ == "__main__":
    main()
