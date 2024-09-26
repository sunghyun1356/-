n, k = map(int, input().split())  # 멀티탭 구멍 수와 전기 용품의 총 사용횟수 입력
order = list(map(int, input().split()))  # 전기 용품의 사용 순서 입력
used_order = [0] * (k+1)  # 각 전기 제품의 사용 빈도 저장, 인덱스를 1-based로 맞춤

# 전기 제품이 얼마나 사용되는지 계산
for i in order:
    used_order[i] += 1

use = []  # 멀티탭에 꽂힌 전기 제품 목록
count = 0  # 플러그를 빼는 횟수

# 멀티탭에 꽂힌 제품 중 앞으로 가장 나중에 사용될 제품을 찾는 함수
def order_check(use, current_index):
    latest_use = -1  # 나중에 사용될 인덱스 추적
    minimum_index = -1  # 제거할 제품의 인덱스

    for i in range(len(use)):
        current_item = use[i]
        try:
            # 현재 이후에 해당 전기제품이 다시 사용되는 가장 첫번째 인덱스를 찾음
            future_index = next(idx for idx in range(current_index + 1, k) if order[idx] == current_item)
        except StopIteration:
            # 만약 이 전기제품이 더 이상 사용되지 않으면 즉시 제거 대상
            return i
        if future_index > latest_use:
            latest_use = future_index
            minimum_index = i

    return minimum_index  # 가장 나중에 다시 사용될 제품의 인덱스를 반환

for current_index, elec in enumerate(order):
    # 멀티탭에 이미 꽂혀 있으면 사용 가능하므로 넘어감
    if elec in use:
        used_order[elec] -= 1
        continue
    # 멀티탭에 빈 자리가 있으면 전기 제품을 꽂음
    if len(use) < n:
        use.append(elec)
        used_order[elec] -= 1
    else:
        # 멀티탭이 꽉 찼으면 가장 나중에 다시 사용될 제품을 제거하고 새 제품을 꽂음
        index = order_check(use, current_index)  # 교체할 전기 제품의 인덱스 찾기
        use.pop(index)  # 해당 인덱스의 제품을 제거
        use.append(elec)  # 새 제품을 멀티탭에 꽂음
        used_order[elec] -= 1
        count += 1  # 교체 횟수 증가

print(count)  # 결과 출력
