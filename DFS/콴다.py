def is_rule_satisfied(num):
    nums = []
    nums.append(num)
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num - 1
        if num in nums:
            return False
        nums.append(num)
    return True

result = 0
check = [False] * 100000  
for i in range(545, 553):
    check[i] = is_rule_satisfied(i)
for i in range(545,555):
    if check[i] == False:
        result += 1
print(result)
