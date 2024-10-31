# 마지막 꺼 부터 써야한다

# dp의 값을 바꿔주는 것이 필요하다

n = int(input())
prices = list(map(int, input().split()))
real_prices = [[] for _ in range(n)]
for index, price in enumerate(prices):
    real_prices[index]=[index, price]
real_prices = sorted(real_prices, key = lambda x : (x[1],x[0]))
standard = real_prices[n-1][1]
standards = [real_prices[n-1][1]]
standard_index = real_prices[n-1][0]
standard_indexs = [real_prices[n-1][0]]
for i in range(n-2,-1,-1):
    if real_prices[i][1] == standard:
        real_prices[i][0] = standard_index
    else:
        standard = real_prices[i][1]
        standard_index = real_prices[i][0]
        standard_indexs.append(standard_index)
        standards.append(standard)

maximum = max(standards)

budget = int(input())
# 만약에 값이 같은게 있다면 이를 중복처리를 막고 제일 index 값으로 처리하는 작업이 필요

def change(value):
    total=0
    value.sort()
    for i in range(len(value)):
        total += (10**i) * value[i]
    return total

# dp에는 각각의 index 값이 저장된다

# 일단 가장 가격이 낮은 것의 

if budget <= maximum:
    dp = [[] for _ in range(maximum+1)]
else:
    dp = [[] for _ in range(budget+1)]
for i in standard_indexs:
    dp[real_prices[i][1]] = [real_prices[i][0]]

# 1원부터 예산때까지
for k in range(budget+1):
    # 총 n개의 숫자를 구입가능하다고 볼때
    for j in range(n):
        if k - real_prices[j][1] >=0:
            
            if change(dp[k])<change(dp[k-real_prices[j][1]] + [real_prices[j][1]]):
                dp[k] = dp[k-real_prices[j][1]] + [real_prices[j][0]]
print(change(dp[budget]))