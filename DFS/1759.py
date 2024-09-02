import sys
import copy

n, m = map(int, input().split())
words = list(map(str, input().split()))
words = sorted(words)
words_visited = [False] * m
candidate = []

vowels = {'a', 'e', 'i', 'o', 'u'}


def check(candidate):
    candidate.sort()
    real = []
    for index, word in enumerate(candidate):
        mo_count = 0
        ja_count = 0
        for each in word:
            if each in vowels:
                mo_count +=1
            elif each not in vowels:
                ja_count +=1
        if not(mo_count < 1 or ja_count < 2):
            real.append(word)
    return real

def solution(depth, start, current_combination):
    if depth == n:
        candidate.append(current_combination)
        return

    for i in range(start, m):
        solution(depth+1, i+1, current_combination + words[i])
                    
solution(0,0,"" )
candidate = check(candidate)
for row in candidate:
    print("".join(row))