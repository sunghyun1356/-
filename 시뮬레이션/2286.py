n = int(input())  # 건물의 개수
buildings = list(map(int, input().split()))  # 건물 높이 리스트
buildings_info = [[] for _ in range(n)]  # 각 건물의 정보 리스트

# 각 건물에 대해 양옆으로 높은 건물을 찾는 투포인터 알고리즘
for i in range(1, n-1):  # 첫 번째와 마지막은 제외
    start = i - 1  # 왼쪽으로 이동할 포인터
    end = i + 1    # 오른쪽으로 이동할 포인터
    left_maximum = 0
    right_maximum = 0
    
    while start >= 0 and end < n:
        if start >= 0:
            if buildings[start] > buildings[i] and buildings[start] > left_maximum:
                left_maximum = buildings[start]
                buildings_info[i].append((i - start, start))
            start -= 1  # 왼쪽으로 한 칸 이동
        
        if end < n:
            if buildings[end] > buildings[i] and buildings[end] > right_maximum:
                right_maximum = buildings[end]
                buildings_info[i].append((end - i, end))
            end += 1  # 오른쪽으로 한 칸 이동

# 첫 번째 건물에 대해 오른쪽 건물 중 높은 건물 찾기
first_maximum = 0
for i in range(1, n):
    if buildings[i] > buildings[0] and buildings[i] > first_maximum:
        first_maximum = buildings[i]
        buildings_info[0].append((i, i))

# 마지막 건물에 대해 왼쪽 건물 중 높은 건물 찾기
last_maximum = 0
for i in range(n - 2, -1, -1):
    if buildings[i] > buildings[n - 1] and buildings[i] > last_maximum:
        last_maximum = buildings[i]
        buildings_info[n - 1].append((n - 1 - i, i))

# 결과 출력
for i in range(n):
    if buildings_info[i]:  # 높은 건물을 찾은 경우
        buildings_info[i] = sorted(buildings_info[i], key=lambda x: (x[0], x[1]))
        # 거리, 인덱스 튜플에서 인덱스 값만 +1
        print(len(buildings_info[i]), buildings_info[i][0][1] + 1)
    else:  # 높은 건물을 찾지 못한 경우
        print(0)
