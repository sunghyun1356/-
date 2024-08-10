import sys
input = sys.stdin.readline
from collections import deque
# bfs로 돌아가면서 각각의 파티에 어떤 사람이 껴있는지를 확인한다. 

# 총 사람 수 / 총 파티 수
n, m = map(int, input().split())
temp_1 = list(map(int, input().split()))
true_number = temp_1[0]
if true_number > 0:
    true_member = temp_1[1:]
party = [[]for _ in range(m)]
for i in range(m):
    temp = list(map(int, input().split()))
    party[i] = temp[1:]
visited_party = [False for _ in range(m)]
used = [False for _ in range(n+1)]
def bfs(a):
    q = deque()
    q.append(a)
    used[a] = True
    while q:
        now = q.popleft()
        for index,i in enumerate(party):
            if now in i and visited_party[index] == False:
                visited_party[index]=True
                for j in i:
                    if used[j] == False and j!=now:
                        q.append(j)
sum = 0
if true_number == 0:
    print(m)
else:
    for i in true_member:
        bfs(i)
    for i in visited_party:
        if i == False:
            sum+=1
    print(sum)