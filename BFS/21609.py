# 검은색 -1, 무지개 0, 일반 아무 숫자
# 최소 블록수는 2개고 일반 아무숫자는 무조건 숫자가 서로 같고 무지개는 아무거나 상관없다

# 블럭 합 찾아줄 때 개수가 같고 무지개 색이 같은 것을 기준으로 찾아준다

# 블록의 크기에 대한 i,j값을 한번에 넣어준다.

# 중력이 발생하면 격자를 벗어나거나 -1을 만날때 까지 밑으로 내려간다

from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split()))for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 벗어나기 전이나 -1을 만나기 전까지 쭉 밑으로 내려준다
def move_down(graph):
    # 각 열만큼
    for j in range(n):
        # 맨 및에 있는거 부터
        for i in range(n-1,-1,-1):
            if graph[i][j] != None and graph[i][j] != -1:
                while i+1<n:
                    if graph[i+1][j] == None:
                        graph[i+1][j] = graph[i][j]
                        graph[i][j] = None
                        i+=1
                    else:
                        break


def rotate(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    return new_graph



# 남은거 있는지 체크
def check(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] !=0 and graph[i][j] !=-1:
                return False
    return True

def bfs(i,j):
    q = deque([(i,j)])
    # 최적화 가능
    visited = [[False]* n for _ in range(n)]
    visited[i][j] = True
    value = graph[i][j]
    candidate = [[(i,j)],[],0]
    while q:
        y, x = q.popleft()
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx] == False:
                    if graph[ny][nx] == value:
                        q.append((ny,nx))
                        visited[ny][nx] = True
                        candidate[0].append((ny,nx))
                    elif graph[ny][nx] == 0:
                        q.append((ny,nx))
                        visited[ny][nx] = True
                        candidate[1].append((ny,nx))
                        candidate[2]+=1
    candidate[0] = sorted(candidate[0], key = lambda x : (x[0], x[1]))
    return candidate
temp = False
answer = 0
while temp == False:
    # 제일 큰 놈 찾아주고 지워주기
    candidates = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1 and graph[i][j] != None and graph[i][j] != 0 and graph[i][j] > 0:
                candidates.append(bfs(i,j))
    candidates = sorted(candidates, key = lambda x : (-1*(len(x[0]) + len(x[1])),-x[2],-x[0][0][0],-x[0][0][1]))
    if len(candidates) == 0:
        break
    if len(candidates[0][0]) < 2:
        break
    
    answer += (len(candidates[0][0]))**2
    for c in candidates[0][0]:
            y,x = c
            graph[y][x] = None
    # 중력
    move_down(graph)

    # 90도 전환
    graph = rotate(graph)

    # 중력
    move_down(graph)

    temp = check(graph)




print(answer)