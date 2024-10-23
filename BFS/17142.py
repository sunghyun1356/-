from itertools import combinations
from collections import deque
from copy import deepcopy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 총 n 개 중에 m개를 골라서 이 위치에서 BFS를 시켜준다.
n, m = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]
virus = []
visited = [[False] * n for _ in range(n)]
empty_cells =0
virus_total =0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))
        elif graph[i][j] == 0:
            empty_cells +=1
if empty_cells == 0:
    print(0)
    exit()

virus_combination = list(combinations(virus,m))

# 다같이 바이러스를 한번에 돌려줘야한다. -> q에 한번에 넣어서 가능할까
timing = []
# 각각 끝나는 초를 어떻게 카운트 해주지? q의 길이만큼 계산해준다고 생각하자
for virus_combi in virus_combination:
    visited_copy = deepcopy(visited)
    q = deque([])
    for vi in virus_combi:
        q.append(vi)
        y,x = vi
        visited_copy[y][x] = True
    time = 0
    filled_cells = 0
    # 맨처음 시작할 때 m개

    while q:
        for _ in range(len(q)):
            y,x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # 그래프 안이고 아직 방문 안했고 벽도 아닐때
                if 0<=ny<n and 0<=nx<n and visited_copy[ny][nx] == False:
                    if  graph[ny][nx] == 0:
                        q.append((ny,nx))
                        visited_copy[ny][nx] = True
                        filled_cells +=1
                    elif graph[ny][nx] == 2:
                        q.append((ny,nx))
                        visited_copy[ny][nx] = True
                        
        time+=1
        if filled_cells == empty_cells:
            timing.append(time)
            break
if len(timing) == 0:
    print(-1)
else:
    print(min(timing))