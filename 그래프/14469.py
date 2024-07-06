# 먼저 도착시간으로 오름차순으로 정렬하고
# 하나씩 빼서 각각이 가능하다면 그걸 또 배치하기
# 하나 씩 넣어줄 공간이 필요하다
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cows = []
for i in range(n):
    first, second = map(int, input().split())
    cows.append((first, second))

cows = sorted(cows, key=lambda x: x[0])
time = cows[0][0] + cows[0][1]
for i in range(1,n):
    if time <= cows[i][0]:
        time = cows[i][0]+cows[i][1]
    else:
        time += cows[i][1]
print(time)
