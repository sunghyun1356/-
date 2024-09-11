n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
numbers.sort()  # 배열을 오름차순으로 정렬

start = 0
end = 0
minimum_gap = float('inf')  # 최소 차이를 무한대로 초기화

# 투 포인터 방식으로 최소 차이 찾기
while end < n:
    gap = numbers[end] - numbers[start]
    
    # 차이가 m 이상인 경우
    if gap >= m:
        minimum_gap = min(minimum_gap, gap)
        start += 1  # start 포인터를 움직여서 더 작은 차이로 이동
    else:
        end += 1  # 차이가 m보다 작으므로 end 포인터를 움직여서 차이를 크게 만든다

print(minimum_gap)
