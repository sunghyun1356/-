from collections import deque
import math

check = [0] * 10000000
check[1] = 1
check[2] = 1
check[3] = 1
maximum = 24999 * 3 + 1

def BFS(n):
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        now_1 = 0  # Initialize now_1 here
        now_2 = 0  # Initialize now_2 here
        if now > 0:
            if now % 2 == 0:
                now_1 = now // 2
            else:
                now_2 = now * 3 - 1
            # Check if now_1 is valid and not checked
            if now_1 > 0 and check[now_1] == 0 and (now_1 & (now_1 - 1)) == 0:
                check[now_1] = 1
                q.append(now_1)
            # Check if now_2 is valid and not checked
            if now_2 > 0 and check[now_2] == 0:
                q.append(now_2)

answer = 0

a, b = map(int, input().split())
for i in range(a, b + 1):
    if i %3:
        pass
print(answer)
