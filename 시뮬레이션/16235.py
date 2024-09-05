n, m, k = map(int, input().split())
tree_graph = [list(map(int, input().split())) for _ in range(n)]
tree_info_graph = [[[5, [], []] for j in range(n)] for i in range(n)]
tree_location_info = []

tree_number = 0

for _ in range(m):
    y, x, old = map(int, input().split())
    tree_info_graph[y-1][x-1][1].append(old)
    tree_location_info.append((y-1, x-1))
    tree_number += 1

dx = [0, -1, 1, -1, 1, -1, 1, 0]
dy = [-1, -1, 0, 0, 1, 1, 0, 1]

def spring(tree_number, tree_location_info, tree_info_graph):
    new_tree_location_info = []
    for y, x in tree_location_info:
        tree_info_graph[y][x][1].sort()  # 어린 나무부터 양분을 먹기 위해 정렬
        alive_trees = []
        dead_trees = []
        for t in tree_info_graph[y][x][1]:
            if tree_info_graph[y][x][0] >= t:
                tree_info_graph[y][x][0] -= t
                alive_trees.append(t + 1)
            else:
                dead_trees.append(t)
                tree_number -= 1
        tree_info_graph[y][x][1] = alive_trees
        tree_info_graph[y][x][2] = dead_trees
        if alive_trees:
            new_tree_location_info.append((y, x))
    tree_location_info = list(set(new_tree_location_info))  # 갱신된 나무 위치 정보로 대체
    return tree_number, tree_location_info, tree_info_graph

def summer(tree_location_info, tree_info_graph):
    for y, x in tree_location_info:
        for t in tree_info_graph[y][x][2]:
            tree_info_graph[y][x][0] += (t // 2)
        tree_info_graph[y][x][2] = []  # 죽은 나무 리스트 초기화
    return tree_info_graph

def fall(tree_number, tree_location_info, tree_info_graph):
    new_tree_location_info = []
    for y, x in tree_location_info:
        for t in tree_info_graph[y][x][1]:
            if t % 5 == 0:
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n:
                        tree_info_graph[ny][nx][1].append(1)
                        new_tree_location_info.append((ny, nx))
                        tree_number += 1
    tree_location_info.extend(new_tree_location_info)  # 새로운 나무 위치 추가
    tree_location_info = list(set(tree_location_info))  # 중복 제거를 위해 set을 사용하여 리스트로 변환

    return tree_number, tree_location_info, tree_info_graph

def winter(tree_info_graph, tree_graph):
    for i in range(n):
        for j in range(n):
            tree_info_graph[i][j][0] += tree_graph[i][j]
    return tree_info_graph

def solution():
    global tree_number, tree_location_info, tree_info_graph  # 전역 변수 선언
    for _ in range(k):
        tree_number, tree_location_info, tree_info_graph = spring(tree_number, tree_location_info, tree_info_graph)
        tree_info_graph = summer(tree_location_info, tree_info_graph)
        tree_number, tree_location_info, tree_info_graph = fall(tree_number, tree_location_info, tree_info_graph)
        tree_info_graph = winter(tree_info_graph, tree_graph)
        for i in range(n):
            for j in range(n):
                print(tree_info_graph[i][j][0], end=" ")
            print()
            
    print(tree_number)

solution()
