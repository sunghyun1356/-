def solution(a):
    left_maximum = [0] * len(a)
    left_maximum[0] = a[0]
    right_maximum = [0] * len(a)
    right_maximum[-1] = a[-1]  # 마지막 요소는 a[-1]로 설정
    
    answer = 0
    
    # left_maximum 계산
    for i in range(1, len(a)):
        left_maximum[i] = min(a[i-1], left_maximum[i-1])

    # right_maximum 계산
    for j in range(len(a)-2, -1, -1):  # 뒤에서 두 번째부터 0까지 순회
        right_maximum[j] = min(a[j+1], right_maximum[j+1])

    # 중간 요소 확인
    for k in range(1, len(a)-1):
        if a[k] > left_maximum[k] and a[k] > right_maximum[k]:
            answer += 1
    
    return len(a) - answer
