n = int(input())
words = []
for _ in range(n):
    words.append(input())

# 알파벳 빈도 계산
freq = {}

for word in words:
    length = len(word)
    for i in range(length):
        # 각 알파벳에 대해 자릿수만큼 가중치를 부여
        if word[i] in freq:
            freq[word[i]] += 10 ** (length - i - 1)
        else:
            freq[word[i]] = 10 ** (length - i - 1)

# 빈도수가 높은 알파벳부터 내림차순으로 정렬
sorted_freq = sorted(freq.items(), key=lambda x: -x[1])

# 숫자 할당 (9, 8, 7, ...)
value = 9
char_to_digit = {}
for char, _ in sorted_freq:
    char_to_digit[char] = value
    value -= 1

# 단어 값을 계산
total_sum = 0
for word in words:
    current_value = 0
    for char in word:
        current_value = current_value * 10 + char_to_digit[char]
    total_sum += current_value

print(total_sum)

