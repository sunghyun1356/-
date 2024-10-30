from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
early = [False] * n
for _ in range(n-1):
    first, second = map(int, input().split())
    graph[first-1].append(second-1)
    graph[second-1].append(first-1)

q = deque()
for i in range(len(graph)):
    if len(graph[i]) == 1:
        q.append(i)
cnt = 0

while q:
    now = q.pop()
    for next in graph[now]:
        for next_next in graph[next]:
            graph[next_next].remove(next)
            if len(graph[next_next]) == 1:
                q.append(next_next)
        visited[next] = True
        graph[next] = []
print(sum(visited))