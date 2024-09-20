"""문제
a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소로 하는 프로그램을 작성하시오.

이 문자열은 원형이기 때문에, 처음과 끝은 서로 인접해 있는 것이다.

예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.

입력
첫째 줄에 문자열이 주어진다. 문자열의 길이는 최대 1,000이다.

출력
첫째 줄에 필요한 교환의 회수의 최솟값을 출력한다.

예제 입력 1 
abababababababa
예제 출력 1 
3
예제 입력 2 
ba
예제 출력 2 
0
예제 입력 3 
aaaabbbbba
예제 출력 3 
0
예제 입력 4 
abab
예제 출력 4 
1
예제 입력 5 
aabbaaabaaba
예제 출력 5 
2
예제 입력 6 
aaaa
예제 출력 6 
0"""
words = input()
#################

# a개의 개수만큼이 필요한 윈도우슬라이드
# 움직이면서 최소의 개수를 구해주면 된다
# 만약에 아무것도 없는 a만 쭉 있다면

aa = 0 # a의 개수
bb = 0 # b의 개수


start = 0
a_count = words.count('a')
minimum = 1e9
words+=words
for i in range(len(words)-a_count+1):
    new_words = words[i:i+a_count]
    if new_words.count('a') == a_count:
        minimum =0
        break
    else:
        minimum = min(minimum, new_words.count('b'))
print(minimum)

