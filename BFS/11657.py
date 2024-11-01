from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
new_graph = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 그룹별 크기와 그룹 번호 저장
group_sizes = {}
group_id = 2  # 0, 1과 구분하기 위해 2부터 시작

# 0으로 연결된 영역을 BFS로 그룹화하여 크기를 저장하는 함수
def mark_group(i, j):
    queue = deque([(i, j)])
    graph[i][j] = group_id  # 그룹 번호로 마킹
    size = 1
    
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = group_id
                size += 1
                queue.append((ny, nx))
    
    group_sizes[group_id] = size  # 그룹 크기 저장

# 0 영역을 그룹화
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            mark_group(i, j)
            group_id += 1

# 벽에 대해 인접한 그룹의 크기 합산
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            adjacent_groups = set()
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] > 1:
                    adjacent_groups.add(graph[ni][nj])  # 인접한 그룹 번호 추가
            
            # 인접한 그룹의 크기 합산 + 1 (자기 자신 포함)
            new_graph[i][j] = (sum(group_sizes[g] for g in adjacent_groups) + 1) % 10

# 결과 출력
for row in new_graph:
    print("".join(map(str, row)))
