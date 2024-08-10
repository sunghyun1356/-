# 일단 다 더해서 만약에 감당가능하다면 그냥 그대로 두고

n = int(input()) 
budgets = list(map(int, input().split()))
maximum = int(input())

budgets.sort()

sumsum = 0

if sum(budgets) <= maximum:
    print(max(budgets))
else:
    average = maximum // n
    for index, num in enumerate(budgets):
        if num > average:
            break