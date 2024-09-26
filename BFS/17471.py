from itertools import combinations
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

people = list(map(int, input().split()))
for i in range(1, n+1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]

total_candidate = []
numbers = [i for i in range(1, n+1)]

def combi(n):
    for i in range(1, n//2+1):
        cobs = [list(comb) for comb in combinations(numbers, i)]
        total_candidate.extend(cobs)  # 조합을 확장해서 리스트에 저장
combi(n)

# bfs를 이용해 연결 상태를 확인
def check(first_check):
    first = first_check[0]
    visited = [first]
    q = deque([first])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if next not in visited and next in first_check:
                visited.append(next)
                q.append(next)
    # 방문한 모든 노드가 first_check와 같은지 확인
    return sorted(first_check) == sorted(visited)

# 후보의 인구 수를 계산
def count(candi):
    total = 0
    for i in candi:
        total += people[i-1]
    return total

# 전체 조합을 체크해서 최소값을 구하는 함수
def all_check(total_candidate, numbers):
    minimum = 1e9  # 임의의 큰 값으로 초기화
    for candidate in total_candidate:
        opposite = list(set(numbers) - set(candidate))  # candidate의 반대 집합
        if check(candidate) and check(opposite):  # 두 구역 모두 연결된 경우
            candidate_count = abs(count(candidate) - count(opposite))
            minimum = min(minimum, candidate_count)
    return minimum

print(all_check(total_candidate, numbers) if all_check(total_candidate, numbers) != 1e9 else -1 )
