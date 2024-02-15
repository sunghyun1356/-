import sys
input = sys.stdin.readline

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int, input().split())
graph = [list(map(str, input().rstrip()))for _ in range(n)]
check = [[0]*m for _ in range(n)]

water = deque()
kaktus = deque()

def watering():
    for _ in range(len(water)):
        y,x = water.popleft()
        for i in range(4):
            ny = y +dy[i]
            nx = x +dx[i]
            if 0<=ny<n and 0<=nx<m and graph[ny][nx] ==".":
                graph[ny][nx] = "*"
                water.append((ny,nx))

def kaktusing(y,x):
    check[y][x] =1
    kaktus.append((y,x))
    while kaktus:
        for _ in range(len(kaktus)):
            y,x = kaktus.popleft()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<n and 0<=nx<m:
                    if check[ny][nx] == 0 and graph[ny][nx] == ".":
                        check[ny][nx] = check[y][x] +1
                        kaktus.append((ny,nx))
                    elif graph[ny][nx] == 'D':
                        print(check[y][x])
                        return
        watering()
    print("KAKTUS")
    return

for i in range(n):
    for j in range(m):
        if graph[i][j] == "S":
            si,sj = i,j
            graph[i][j] ="."
        if graph[i][j] == "*":
            water.append((i,j))
watering()
kaktusing(si,sj)