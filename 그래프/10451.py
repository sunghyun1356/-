from collections import deque

def BFS(z):
    q = deque()
    q.append(z)
    visited[z] = True
    while q:
        k = q.popleft()
        for j in stack[k]:
            if visited[j] == False:
                q.append(j)
                visited[j] = True
    
t  = int(input())
for _ in range(t):
    n = int(input())
    stack = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    answer = 0
    numbers = list(map(int, input().split()))
    for i,j in enumerate(numbers):
        stack[i+1].append(j)
    
    for k in range(n):
        if visited[k+1] == False:
            BFS(k+1)
            answer+=1
    print(answer)
            

    
    