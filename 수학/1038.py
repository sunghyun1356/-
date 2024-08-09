from itertools import combinations

def get_decreasing_number(n):
    decreasing_numbers = []

    # 각 자릿수 길이별로 감소하는 수 생성
    for length in range(1, 11):  # 1자리 수부터 10자리 수까지
        for comb in combinations(range(10), length):
            # 큰 자릿수부터 작은 자릿수로 정렬
            decreasing_numbers.append(int("".join(map(str, sorted(comb, reverse=True)))))
    
    # 모든 감소하는 수를 정렬
    decreasing_numbers.sort()

    # N번째 감소하는 수 출력
    if n < len(decreasing_numbers):
        return decreasing_numbers[n]
    else:
        return -1

# 입력
n = int(input())

# N번째 감소하는 수 출력
print(get_decreasing_number(n))

    