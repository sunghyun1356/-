import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

total_decrease = 0

for i in range(n-2, -1, -1):
    if scores[i] >= scores[i+1]:
        decrease_amount = scores[i] - scores[i+1] + 1
        scores[i] -= decrease_amount
        total_decrease += decrease_amount

print(total_decrease)
