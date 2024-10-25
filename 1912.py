n = int(input())
arr = list(map(int, input().split()))

# dp 배열을 1차원으로 선언
dp = [-1e9] * n
dp[0] = arr[0]

maximum = dp[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    maximum = max(maximum, dp[i])

print(maximum)