import sys
input = sys.stdin.readline

# 홀수 일때는 비교를 해주면 되긴하지만 
# 짝수 일때는 맨 처음꺼를 맨 뒤에 일단 끼워주고 생각한다
# dp[][]일때 처음은 총 숫자의 개수이며 뒤는 중간지점이 되고자 하는 위치

n = int(input())
penlindrome = list(map(int, input().split()))
reversed_penlindrome = penlindrome[::-1]
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if penlindrome[i-1] == reversed_penlindrome[j-1]:
           dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1] )
           
print(n - dp[n][n]) 


