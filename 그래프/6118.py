import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, cnt):
    q = deque()
    q.append((start, 0))
    visited[start] = True
    
    while q:
        now, count = q.popleft()
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, count + 1))
                result.append((next_node, count + 1))

    # 중복을 제거하면서 가장 큰 count만 남기기
    unique_result = {}
    for a, b in result:
        if a not in unique_result or b > unique_result[a]:
            unique_result[a] = b

    # 다시 (a, b) 형식의 리스트로 변환하고 정렬: 첫번째 기준 x[1] 내림차순, 두번째 기준 x[0] 오름차순
    final_result = sorted(unique_result.items(), key=lambda x: (-x[1], x[0]))
    return final_result

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

final_result = bfs(1, 0)

smallest = final_result[0][0]
temp = final_result[0][1]
cnt = 0
for num in final_result:
    if num[1] == temp:
        cnt+=1
print(smallest,temp, cnt)

# dict으로 만들어서 정렬을 해준다 key = lambda x :