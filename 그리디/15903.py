import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
digits = list(map(int, input().split()))

# 제일 작은거 2개 골라서 다시 넣어야하니까 heapq를 사용하다
heapq.heapify(digits)

for _ in range(m):
    # 제일 작은거 2개 빼주고
    first = heapq.heappop(digits)
    second = heapq.heappop(digits)
    sum_value = first + second
    
    # 2개 다시 넣어주고
    heapq.heappush(digits, sum_value)
    heapq.heappush(digits, sum_value)

result = sum(digits)
print(result)
