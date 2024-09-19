from itertools import permutations

def one_time(tries, i, start, order):
    count = 0
    score = 0
    hitter = tries[i]
    places = [False] * 3  # 각 베이스 상태 (1루, 2루, 3루)
    
    while count < 3:
        if hitter[order[start]] == 0:  # 아웃
            count += 1
        elif hitter[order[start]] == 1:  # 안타
            if places[2]:  # 3루 주자가 있으면 득점
                score += 1
            places = [places[1], places[0], True]
        elif hitter[order[start]] == 2:  # 2루타
            if places[2]:  # 3루 주자가 있으면 득점
                score += 1
            if places[1]:  # 2루 주자가 있으면 득점
                score += 1
            if places[0]:
                places = [False,True, True]
            else:
                places = [False, True, False]
        elif hitter[order[start]] == 3:  # 3루타
            score += sum(places)  # 모든 주자 득점
            places = [False, False, True]
        elif hitter[order[start]] == 4:  # 홈런
            score += sum(places) + 1  # 모든 주자와 타자 득점
            places = [False, False, False]
        
        start = (start + 1) % 9  # 다음 타자
    return score, start

def max_score(tries, n):
    max_total_score = -1e9
    for perm in permutations(range(1, 9)):  # 1번 타자는 4번 고정, 나머지 8명만 순열 생성
        hitter_order = list(perm[:3]) + [0] + list(perm[3:])  # 4번에 1번 타자(0) 고정
        
        total_score = 0
        start = 0
        for i in range(n):
            score, start = one_time(tries, i, start, hitter_order)
            total_score += score
        
        max_total_score = max(max_total_score, total_score)
    return max_total_score

# 입력 처리
n = int(input())  # 이닝 수 입력
tries = [list(map(int, input().split())) for _ in range(n)]  # 각 이닝 타격 정보 입력

print(max_score(tries, n))
