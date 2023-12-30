from collections import deque

def DFS(graph, start, visited):
    q = deque([start])
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            for neighbor, cost in graph[now]:
                if not visited[neighbor]:
                    q.append(neighbor)

def solution(n,costs):
    answer = 0
    graph ={}
    for i in range(n):
        graph[i] = []
        
    costs = sorted(costs, key=lambda x : x[2])
    
    for i in costs:
        if not(graph[i[0]] and graph[i[1]]):
            graph[i[0]].append((i[1],i[2]))
            graph[i[1]].append((i[0],i[2]))
            
    visited = [False] *n
    DFS(graph, 0, visited)
    
    return answer

n =4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
result = solution(n, costs)
print(result)