from collections import defaultdict
n, m ,s= map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)
for i in range(1,n+1):
    graph[i].sort()
visited = [False] * (n + 1)
result = {}
for i in range(n+1):
    result[i] = 0

def dfs(now, time):
    visited[now] = True
    result[now] = time
    for next in graph[now]:
        if not visited[next]:
            dfs(next, time + 1)
dfs(s, 1)
for i in range(1, n+1):
    print(result[i])
