"""문제
N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. N=5일 때의 예를 보자.

12	7	9	15	5
13	8	11	19	6
21	10	26	31	16
48	14	28	35	25
52	20	32	41	49
이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,500)이 주어진다. 다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다. 표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다.

출력
첫째 줄에 N번째 큰 수를 출력한다.

예제 입력 1 
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
예제 출력 1 
35"""

# 어차피 찾아야 하는건 N번째로 큰 수
# 메모리 초과라면 전체다 저장하는게 아니라 읽으면서 하는것

import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap =[]

a = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(heap, a[i])
criteria = heapq.heappop(heap)
for i in range(1,n):
    a = list(map(int,input().split()))
    for j in range(n):
        if criteria < a[j]:
            heapq.heappush(heap, a[j])
            criteria = heapq.heappop(heap)
print(criteria)


            



# 위는 메모리 초과
# heap에 하나씩 다 넣어줄 필요가 없다 -> 적정량만 넣으면 된다는 것
# 넣을 것 안넣을것에 대한 조율이 필요하다
# 중간 열에 대해서 다시 기준점을 둬서 배치를 해보자


