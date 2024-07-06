"""문제
N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구해내는 프로그램을 작성하시오.

두 단어의 비슷한 정도는 두 단어의 접두사의 길이로 측정한다. 접두사란 두 단어의 앞부분에서 공통적으로 나타나는 부분문자열을 말한다. 즉, 두 단어의 앞에서부터 M개의 글자들이 같으면서 M이 최대인 경우를 구하는 것이다. "AHEHHEH", "AHAHEH"의 접두사는 "AH"가 되고, "AB", "CD"의 접두사는 ""(길이가 0)이 된다.

접두사의 길이가 최대인 경우가 여러 개일 때에는 입력되는 순서대로 제일 앞쪽에 있는 단어를 답으로 한다. 즉, 답으로 S라는 문자열과 T라는 문자열을 출력한다고 했을 때, 우선 S가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력하고, 그런 경우도 여러 개 있을 때에는 그 중에서 T가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력한다.

입력
첫째 줄에 N(2 ≤ N ≤ 20,000)이 주어진다. 다음 N개의 줄에 알파벳 소문자로만 이루어진 길이 100자 이하의 서로 다른 영단어가 주어진다.

출력
첫째 줄에 S를, 둘째 줄에 T를 출력한다. 단, 이 두 단어는 서로 달라야 한다. 즉, 가장 비슷한 두 단어를 구할 때 같은 단어는 제외하는 것이다.

예제 입력 1 
9
noon
is
lunch
for
most
noone
waits
until
two
예제 출력 1 
noon
noone
예제 입력 2 
4
abcd
abe
abc
abchldp
예제 출력 2 
abcd
abc"""
#첫 글자가 같은 것 끼리만 반복 한다
from collections import Counter
import heapq

n = int(input())
same = {}

for i in range(n):
    a = input()
    first_char = a[0]

    if first_char in same:
        same[first_char].append(a)
    else:
        same[first_char] = [a]

def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt

heap = []
maximum = 0
result = None

for i in same:
    if len(same[i]) >= 2:
        words = same[i]
        for j in range(len(words) - 1):
            current_max = check(words[-1], words[j])
            if current_max > maximum or (current_max == maximum and len(words[j]) < len(result[2])):
                maximum = current_max
                result = (maximum, words[-1], words[j])
                if len(heap) > 2:
                    heapq.heappop(heap)
                heapq.heappush(heap, result)

result = heapq.heappop(heap)
print(result[1], result[2])




        


        
        
        
    
    


    

