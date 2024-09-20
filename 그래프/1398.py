from collections import deque

n, m = map(int, input().split())
result = [[0 for i in range(n + 1)] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

def BFS(a, b, n):
    visited = [False] * (n + 1)
    q = deque()
    q.append(a)
    visited[a] = True
    distance = [0] * (n + 1) 
    while q:
        current = q.popleft()
        if current == b:
            return distance[b]
        for neighbor in graph[current]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_bacon = float('inf')
min_person = 0

for i in range(1, n + 1):
    total_bacon = sum(BFS(i, j, n) for j in range(1, n + 1))
    if total_bacon < min_bacon:
        min_bacon = total_bacon
        min_person = i

print(min_person)
