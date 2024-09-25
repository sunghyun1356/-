from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def up(graph):
    for j in range(n):
        temp = []
        for i in range(n):
            if graph[i][j] != 0:
                temp.append(graph[i][j])
        
        k = 0
        for q in range(n):
            if k < len(temp):
                graph[q][j] = temp[k]
                k += 1
            else:
                graph[q][j] = 0
        
        for q in range(n - 1):  
            if graph[q][j] == graph[q + 1][j] and graph[q][j] != 0:
                graph[q][j] *= 2
                graph[q + 1][j] = 0  

        temp = []
        for i in range(n):
            if graph[i][j] != 0:
                temp.append(graph[i][j])

        for q in range(n):
            if q < len(temp):
                graph[q][j] = temp[q]
            else:
                graph[q][j] = 0

    return graph

def down(graph):
    for j in range(n):
        temp = []
        
        for i in range(n - 1, -1, -1):
            if graph[i][j] != 0:
                temp.append(graph[i][j])
        
        k = 0
        for q in range(n - 1, -1, -1):
            if k < len(temp):
                graph[q][j] = temp[k]
                k += 1
            else:
                graph[q][j] = 0
        
        for q in range(n - 1, 0, -1):
            if graph[q][j] == graph[q - 1][j] and graph[q][j] != 0:
                graph[q][j] *= 2
                graph[q - 1][j] = 0  

        temp = []
        for i in range(n):
            if graph[i][j] != 0:
                temp.append(graph[i][j])

        for q in range(n - 1, -1, -1):
            if n - 1 - q < len(temp):
                graph[q][j] = temp[n - 1 - q]
            else:
                graph[q][j] = 0

    return graph

def left(graph):
    for i in range(n):
        temp = []
        for j in range(n):
            if graph[i][j] != 0:
                temp.append(graph[i][j])
        
        k = 0
        for q in range(n):
            if k < len(temp):
                graph[i][q] = temp[k]
                k += 1
            else:
                graph[i][q] = 0
        
        for q in range(n - 1):  
            if graph[i][q] == graph[i][q + 1] and graph[i][q] != 0:
                graph[i][q] *= 2
                graph[i][q + 1] = 0  

        temp = []
        for j in range(n):
            if graph[i][j] != 0:
                temp.append(graph[i][j])

        for q in range(n):
            if q < len(temp):
                graph[i][q] = temp[q]
            else:
                graph[i][q] = 0

    return graph

def right(graph):
    for i in range(n):
        temp = []
        for j in range(n - 1, -1, -1):
            if graph[i][j] != 0:
                temp.append(graph[i][j])
        
        k = 0
        for q in range(n - 1, -1, -1):
            if k < len(temp):
                graph[i][q] = temp[k]
                k += 1
            else:
                graph[i][q] = 0
        
        for q in range(n - 1, 0, -1):
            if graph[i][q] == graph[i][q - 1] and graph[i][q] != 0:
                graph[i][q] *= 2
                graph[i][q - 1] = 0  

        temp = []
        for j in range(n):
            if graph[i][j] != 0:
                temp.append(graph[i][j])

        for q in range(n - 1, -1, -1):
            if n - 1 - q < len(temp):
                graph[i][q] = temp[n - 1 - q]
            else:
                graph[i][q] = 0

    return graph

candidate = []

def bfs(graph):
    q = deque([(graph, 0)])
    max_value = 0  

    while q:
        now_graph, time = q.popleft()
        
        if time == 5:
            max_value = max(max_value, max(max(row) for row in now_graph))
            continue 
        
        for direction in [up, down, left, right]:
            new_graph = [row[:] for row in now_graph]  
            direction(new_graph)

            q.append((new_graph, time + 1))
    
    return max_value

result = bfs(graph)
print(result)


for row in down(graph):
    print(row)
print("down")
for row in up(graph):
    print(row)
print("up")
for row in left(graph):
    print(row)
print("left")
for row in right(graph):
    print(row)
print("right")