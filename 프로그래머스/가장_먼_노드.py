# BFS로 접근, DEPTH이라는 걸로 각각이 몇인지 확인해주기
"""# BFS로 찾긴 찾아지는데 만약에 1234처럼 서로 다 이어진 상태라면 3에서 에러가 발생한다
# 이 경우는 2,3이 동일 선상에 있다는 것을 어떻게 확인 할 것인가? DFS?
# 거리까지 한번에 튜플 형식으로 넣어주면 된다
# BFS는 넣어주고 관련된거 다 확인하고 FALSE로 만들어주면 된다

from collections import deque

def find(parent, x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x)



def solution(n, edge):
    depth = [1 for _ in range(n+1)]
    edge = sorted(edge, key=lambda x : (x[0],x[1]))
    nodes = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for node in edge:
        nodes[node[0]].append(node[1])
        nodes[node[1]].append(node[0])
    def BFS():
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            now = q.popleft()
            print(now)
            for next in nodes[now]:
                if visited[next] == False:
                    visited[next] = True
                    depth[next] = depth[now]+1
                    q.append(next)
        return depth
                    
    distances = BFS()
    answer = max(distances)
    
    return distances"""
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    def bfs(start):
        visited = [False] * (n+1)
        distance = [0] * (n+1)
        queue = deque([(start, 0)])
        visited[start] = True

        while queue:
            current, dist = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1))

        return distance

    distances = bfs(1)

    max_distance = max(distances)
    answer = distances.count(max_distance)

    return answer

