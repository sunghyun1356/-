import sys
input  = sys.stdin.readline

n = int(input())
rgb = []
dp = [[0]*3 for i in range(n)]
for i in range(n):
    inp = list(map(int, input().split()))
    rgb.append(inp)
    
for i in range(3):
    dp[0][i] = rgb[0][i]
    
for i in range(1, n):
    for j in range(0, 3):
        minimum = 1000*1000
        for k in range(0, 3):
            #  만약에 같은 색상이면 뛰어넘는다
            if j == k:
                continue
            # 전꺼를 만약에 k번째 색상으로 칠했을 때 그때가 최소보다 작다면 최소로 하고
            if dp[i-1][k] <minimum:
                minimum = dp[i-1][k]
            # 지금 현재 i번째 집을 j로 색칠한 누적값은 minimum에 그 색상 칠한거다
            dp[i][j] = minimum + rgb[i][j]
print(min(dp[n-1]))  
