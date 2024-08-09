import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited = [False] * (n + 1)  # visited 리스트를 제대로 초기화
    visited[start] = True

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:  # 방문하지 않은 노드만 방문
                q.append(next)
                visited[next] = True
    
    return sum(visited)  # 방문된 노드의 수를 반환

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)  # a가 b를 해킹 가능 -> b에서 a로 간선 추가

maxc = 0
answer = []
for i in range(1, n + 1):
    m = bfs(i)
    if maxc < m:
        answer.clear()  # 더 큰 값이 나오면 리스트를 초기화
        maxc = m
        answer.append(i)
    elif maxc == m:
        answer.append(i)

print(*sorted(answer))  # 정답 출력
