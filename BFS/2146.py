# 맨 처음부터 돌면서 섬인 것들을 체크 한다. 
# 마지막 곳의 위치를 알아야한다
# 섬들의 가장가리들을 알 때 이 때의 거리를 구할 수 있는 함수가 필요 -> 리스트 2개를 비교하는 방향으로 가자


# 만약에 2,1이고 4,2라면 
from collections import deque
from itertools import combinations

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def calculate(a, b):
    minimum_distance = float('inf')
    for i in a:
        for j in b:
            distance = abs(i[0] - j[0]) + abs(i[1] - j[1]) - 1
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance

def bfs(i, j, visited, n, graph):
    q = deque([(i, j)])
    visited[i][j] = True
    island = []
    edge = []
    
    while q:
        y, x = q.popleft()
        island.append((y, x))
        is_edge = False
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                elif graph[ny][nx] == 0:
                    is_edge = True
            else:
                is_edge = True
        
        if is_edge:
            edge.append((y, x))
    
    return edge

def main():
    edges = []
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                edge = bfs(i, j, visited, n, graph)
                if edge:
                    edges.append(edge)
    
    cal_candis = combinations(edges, 2)
    minimum_distance = float('inf')
    
    for cal_candi in cal_candis:
        distance = calculate(cal_candi[0], cal_candi[1])
        if distance < minimum_distance:
            minimum_distance = distance
    
    print(minimum_distance)

if __name__ == "__main__":
    main()
