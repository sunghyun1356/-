h, w, x, y = map(int, input().split())
b_graph = [list(map(int, input().split())) for _ in range(h + x)]
a_graph = [[0 for _ in range(w)] for _ in range(h)]

def solution(b_graph, a_graph):
    # 1번, 2번 영역을 그대로 채움
    for i in range(h):
        for j in range(w):
            a_graph[i][j] = b_graph[i][j]

    # 3번 영역에서 겹치는 부분을 조정
    for i in range(x, h):
        for j in range(y, w):
            a_graph[i][j] = b_graph[i][j] - a_graph[i-x][j-y]

    for row in a_graph:
        print(' '.join(map(str, row)))

solution(b_graph, a_graph)