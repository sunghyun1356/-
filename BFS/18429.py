from itertools import combinations, permutations

n, k = map(int, input().split())  # n: 선택할 운동 개수, k: 운동 후 깎이는 힘
workout = list(map(int, input().split()))  # 운동의 리스트

count = 0
for works in permutations(workout):
    temp = 500  # 초기 체력
    standard = True
    for work in works:
        temp += work  # 운동으로 얻는 체력
        temp -= k  # 운동 후 체력 감소
        if temp < 500:  # 체력이 500 미만이면 실패
            standard = False
            break
    if standard:
        count += 1  # 조건을 만족하면 카운트 증가
print(count)
