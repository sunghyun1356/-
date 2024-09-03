from collections import deque

# 사용자로부터 3x3 퍼즐을 입력받음
graph = [list(map(int, input().split())) for _ in range(3)]

# 상하좌우로 이동하기 위한 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check_zero(graph):
    """
    퍼즐에서 0(빈 공간)의 위치를 찾는 함수
    """
    for i in range(3):
        for j in range(3):
            if graph[i][j] == 0:
                return (i, j)
    return None

def check_all(graph):
    """
    현재 퍼즐 상태가 목표 상태와 일치하는지 확인하는 함수
    """
    return graph == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def bfs(graph):
    """
    퍼즐을 해결하기 위해 최단 이동 횟수를 찾는 BFS 함수
    """
    q = deque()
    # 큐에 초기 상태 추가: (그래프, 이동 횟수)
    q.append((graph, 0))

    # 방문한 상태를 저장하기 위한 집합
    visited = set()
    visited.add(tuple(map(tuple, graph)))

    while q:
        current_graph, time = q.popleft()
        y, x = check_zero(current_graph)

        # 목표 상태에 도달했는지 확인
        if check_all(current_graph):
            print(time)
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                # 현재 그래프의 깊은 복사 생성
                new_graph = [row[:] for row in current_graph]
                
                # 0과 인접한 숫자 위치를 교환
                new_graph[ny][nx], new_graph[y][x] = new_graph[y][x], new_graph[ny][nx]

                # 새로운 그래프를 튜플로 변환하여 해싱 가능하게 만듦
                new_graph_tuple = tuple(map(tuple, new_graph))

                # 새로운 상태가 방문한 적이 없는 경우
                if new_graph_tuple not in visited:
                    visited.add(new_graph_tuple)
                    q.append((new_graph, time + 1))

    print(-1)

# 초기 그래프 상태로 BFS 함수 실행
bfs(graph)
