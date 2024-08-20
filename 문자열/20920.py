import sys
from collections import Counter

input = sys.stdin.readline

# dict의 get를 사용 get은 (찾고 싳은 value의 key값, 없을 때의 초기화 값)

def is_similar(standard_dict, word_dict):
    diff = 0
    if len(standard_dict.keys() - word_dict.keys()) >=2:
        return False
    for letter in standard_dict.keys() | word_dict.keys():
        if  abs(standard_dict.get(letter, 0) - word_dict.get(letter, 0)) >=2:
            return False
        else:
            diff += abs(standard_dict.get(letter, 0) - word_dict.get(letter, 0))
        
    return diff <= 2

def main():
    n = int(input())
    standard = input().strip()

    standard_dict = Counter(standard)
    
    similar_count = 0
    for _ in range(n - 1):
        word = input().strip()
        word_dict = Counter(word)
        
        if is_similar(standard_dict, word_dict):
            similar_count += 1

    print(similar_count)

if __name__ == "__main__":
    main()
