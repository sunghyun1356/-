# dp로 풀어보자
# O(n)으로 풀어야한다
# 어떤 형식이면 좋을 까?
# dp[총개수][개수]
n, m = map(int,input().split())

total = 0
weights = list(map(int, input().split()))
times = list(map(int, input().split()))
total = sum(times)

dp = [[0] * (total+1) for _ in range(n)]
# 1개 넣을 때부터 여러개 넣을 때까지를 비교해준다. 
for i in range(n):
    for j in range(total+1):
        if j - times[i] >=0:
            # 기존의 것과 하나를 더했을 때의 dp를 비교한다.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-times[i]] + weights[i])
        dp[i][j] = max(dp[i][j], dp[i-1][j])
for i in range(total+1):
    if dp[n-1][i] >=m:
        print(i)
        break