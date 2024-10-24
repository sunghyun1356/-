# 1. 길이대로 정렬
# 2. 자리수의 합을 구한다.
# 3. 사전순으로 비교한다

n = int(input())
words = []
for i in range(n):
    word = input()
    length = len(word)
    sum = 0
    temp = []
    for j in list(word):
        if j.isdigit():
            sum+=int(j)
    words.append((length, sum, word))


words = sorted(words, key = lambda x : (x[0],x[1],x[2]))

for word in words:
    print(word[2])
