"""문제
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

입력
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

출력
좋은 수의 개수를 첫 번째 줄에 출력한다.

예제 입력 1 
10
1 2 3 4 5 6 7 8 9 10
예제 출력 1 
8"""

# 하나씩 지정해서 한다

n = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)


answer = 0
for i in range(n):
    goal = numbers[i]
    start = 0
    end = len(numbers)-1
    while start < end:
        # 합이 goal일때
        if numbers[start] + numbers[end] == goal:
            # 
            if start == i:
                start +=1
            elif end == i:
                end -=1
            else:
                answer +=1
                break
        # 합이 goal보다 크면 마지막 부분 앞으로 당겨주기
        elif numbers[start] + numbers[end] > goal:
            end -=1
        # 합이 goal보다 크면 start를 앞으로 해서 크게 만들어주기
        elif numbers[start] + numbers[end] < goal:
            start +=1
print(answer) 
