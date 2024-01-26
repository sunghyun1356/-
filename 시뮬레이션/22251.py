"""문제
치르보기 빌딩은 
$1$층부터 
$N$층까지 이용이 가능한 엘리베이터가 있다. 엘리베이터의 층수를 보여주는 디스플레이에는 
$K$ 자리의 수가 보인다. 수는 
$0$으로 시작할 수도 있다. 
$0$부터 
$9$까지의 각 숫자가 디스플레이에 보이는 방식은 아래와 같다. 각 숫자는 7개의 표시등 중의 일부에 불이 들어오면서 표현된다.



예를 들어 
$K=4$인 경우에 
$1680$층과 
$501$층은 아래와 같이 보인다.

 

빌런 호석은 치르보기 빌딩의 엘리베이터 디스플레이의 LED 중에서 최소 
$1$개, 최대 
$P$개를 반전시킬 계획을 세우고 있다. 반전이란 켜진 부분은 끄고, 꺼진 부분은 켜는 것을 의미한다. 예를 들어 숫자 
$1$을 
$2$로 바꾸려면 총 5개의 LED를 반전시켜야 한다. 또한 반전 이후에 디스플레이에 올바른 수가 보여지면서 
$1$ 이상 
$N$ 이하가 되도록 바꿔서 사람들을 헷갈리게 할 예정이다. 치르보기를 사랑하는 모임의 회원인 당신은 호석 빌런의 행동을 미리 파악해서 혼쭐을 내주고자 한다. 현재 엘리베이터가 실제로는 
$X$층에 멈춰있을 때, 호석이가 반전시킬 LED를 고를 수 있는 경우의 수를 계산해보자.

입력
 
$N, K, P, X$ 가 공백으로 구분되어 첫째 줄에 주어진다.

출력
호석 빌런이 엘리베이터 LED를 올바르게 반전시킬 수 있는 경우의 수를 계산해보자.

제한
 
$1 ≤ X ≤ N < 10^K$
 
$1 ≤ K ≤ 6 $ 
 
$1 ≤ P ≤ 42 $ 
예제 입력 1 
9 1 2 5
예제 출력 1 
4
LED를 2개까지 바꿀 수 있을 때, 5층에서 3층, 6층, 8층, 그리고 9층으로 바꿔버릴 수 있다.

예제 입력 2 
48 2 5 35
예제 출력 2 
30"""

# 반시계 방향 0123456
# k 자리 숫자
# p 개를 바꿔도 됨
# 1~n 까지이하가 되도록 바꾼다
# x층에 멈춰 있다


# 9 1 2 5
# 5층에 멈춰도 있고 1이상 9 이하가 되도록 바꾸고 1자리 숫자
# 바꿀 수 있는 개수를 구해야한다. -> 연속인가?
# 5 -> 최대 2개를 변경가능하다
# 5 -> 6, 9 (1개)
# 5 -> 8, 4

# 각각의 개수를 찾아보자

dp = [[0 for _ in range(10)]for _ in range(10)]
zero = [1,1,1,1,1,1,0]
one = [0,0,0,0,1,1,0]
two = [1,0,1,1,0,1,1]
three = [1,0,0,1,1,1,1]
four = [0,1,0,0,1,1,1]
five = [1,1,0,1,1,0,1]
six = [1,1,1,1,1,0,1]
seven = [1,0,0,0,1,1,0]
eight = [1,1,1,1,1,1,1]
nine = [1,1,0,1,1,1,1]
total =[]
total.append(zero)
total.append(one)
total.append(two)
total.append(three)
total.append(four)
total.append(five)
total.append(six)
total.append(seven)
total.append(eight)
total.append(nine)
def check(a,b):
    answer = 0
    for i in range(7):
        if a[i]!=b[i]:
            answer+=1
    return answer
            

for index_i,i in enumerate(total):
    for index_j,j in enumerate(total):
        dp[index_i][index_j] = check(i,j)


    
n, k, p, x = map(int, input().split())

# n,k,p,x 크기 조정해주기
x = list((k-len(list(str(x))))* "0" + str(x))

result = 0
for num in range(1, n+1):
    count = 0
    num = list((k-len(list(str(num))))*"0"+str(num))

    # 각각에 대해서 차이를 count해주고 더해주기
    for i in range(k):
        a = int(x[i])
        b = int(num[i])
        count +=dp[a][b]
    if count <=p:
        result +=1
print(result -1)
