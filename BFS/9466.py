from collections import deque

# 순환구조에서 순환 되는 부분만 return 해줘야하는 상황

def bfs(i, students, visited):
    q = deque([i])
    path = []
    while q:
        now = q.popleft()
        if visited[now]:
            if now in path:
                idx = path.index(now)
                return path[idx:]
            else:
                return []
        visited[now] = True
        path.append(now)
        next = students[now]
        q.append(next)
    return []

case = int(input())
for _ in range(case):
    n = int(input())
    student = list(map(int, input().split()))
    students = [value - 1 for value in student] 
    visited = [False] * n
    sum = n

    for i in range(n):
        if not visited[i]:
            can = bfs(i, students, visited)
            for c in can:
                visited[c] = True
            sum -= len(can)

    print(sum)
