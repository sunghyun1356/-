def solution(arr):
    zero = 0
    one = 0
    n = len(arr)
    
    # 초기 zero와 one 개수 계산
    for ar in arr:
        zero += sum(1 for i in ar if i == 0)
        one += sum(1 for i in ar if i == 1)
    
    size = n
    visited = [[False] * n for _ in range(n)]
    # 크기가 1 이상일 때만 반복
    while size > 1:
        for i in range(0, n, size):
            for j in range(0, n, size):
                if visited[i][j] == False:
                    sub_sum = 0

                    # 각 2차원 배열 영역의 합을 계산
                    for y in range(i, i + size):
                        for x in range(j, j + size):
                            sub_sum += arr[y][x]

                    # 압축 가능 여부 확인
                    if sub_sum == size**2:
                        one -= (size**2) - 1
                        for y in range(i, i + size):
                            for x in range(j, j + size):
                                visited[y][x] = True
                    elif sub_sum == 0:
                        zero -= (size**2) - 1
                        for y in range(i, i + size):
                            for x in range(j, j + size):
                                visited[y][x] = True

        size //= 2  # 배열 크기를 절반으로 줄임

    return [zero, one]
