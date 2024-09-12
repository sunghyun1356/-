n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
dp = [[0] * 3 for _ in range(n)]

# 이번 텀에서는 마시지 않음
dp[0][0]=0
# 이번 텀에서 마심
dp[0][1]=wine[0]
# 이번 텀에서 
dp[0][2]=0


if n >1:
    dp[1][0] = dp[0][1]
    dp[1][1] = wine[1]
    dp[1][2] = dp[0][1] + wine[1]

# 총 3가지 
# 지금 i번째가 이제 처음으로 마시든지 아니면 2번째로 마시는 것인지 아니면 안먹고 넘어갈건지
# 나머지 잔에 대한 처리
for i in range(2, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])  # 이번 잔을 마시지 않음
    dp[i][1] = dp[i-1][0] + wine[i]  # 이번 잔을 마심 (연속 1잔)
    dp[i][2] = dp[i-1][1] + wine[i]  # 이번 잔을 연속 2잔째로 마심
    
print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))