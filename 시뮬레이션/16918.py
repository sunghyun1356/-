r,c,n = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


# 폭탄이 있는지 체크 하고 이걸 터지기 직전이 x로 바꾼다
def bomb_check(graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                graph[i][j] = "X"
# 터지기 직전인 폭탄 말고 다른 곳들은 모두 o로 가득채운다
def bomb_fill(graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == ".":
                graph[i][j] = "O"

def explosion(graph):
    to_explode = set()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X":
                to_explode.add((i, j))
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0<=ny<r and 0<=nx<c:
                        to_explode.add((ny, nx))
    for (i, j) in to_explode:
        graph[i][j] = "."

def final(graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X":
                graph[i][j] = "O"

if n == 1:
    for row in graph:
        print("".join(row))
    exit()

bomb_check(graph)
for i in range(1,n):
    if i % 2 == 1:
        bomb_fill(graph)
    elif i%2 == 0 and i!= n:
        explosion(graph)
        bomb_check(graph)
        print(graph)
    elif i%2 ==0 and i==n:
        explosion(graph)
final(graph)
for row in graph:
    print("".join(row))

