import sys
input = sys.stdin.readline

num = int(input().strip())
numbers = list(map(int, input().split()))
duplicated_numbers = list(set(numbers))
sorted_numbers = sorted(duplicated_numbers)
print(" ".join(map(str, sorted_numbers)))
