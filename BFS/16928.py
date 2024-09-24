from collections import deque
import sys
input = sys.stdin.readline

graph = [1e9] * 101
graph[0] = 0

n, m = map(int, input().split())
snakes = {}
ladders = {}

for _ in range(n):
    start, end = map(int, input().split())
    snakes[start-1] = end-1

for _ in range(m):
    start, end = map(int, input().split())
    ladders[start-1] = end-1

def bfs():
    q = deque([0])
    
    while q:
        now = q.popleft()
        for i in range(1, 7):
            next_position = now + i
            if next_position > 100:
                continue
            
            if next_position in snakes:
                next_position = snakes[next_position]
            elif next_position in ladders:
                next_position = ladders[next_position]
            
            if graph[now] + 1 < graph[next_position]:
                graph[next_position] = graph[now] + 1
                q.append(next_position)

bfs()
print(graph[99] if graph[99] != 1e9 else -1)
