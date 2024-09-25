import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
first = list(input().rstrip())
second = list(input().rstrip())

first_visited = [False] * (n + k)
second_visited = [False] * (n + k)

def bfs():
    q = deque([(0,True,0)])

    while q:
        now, which, time = q.popleft()
        # 3초 지났을 때 3이상이여야한다
        # time 이 7이니까 4 
        if now >= n:
            if now+1 > time:
                return True
        if which:
            for i in range(3):
                if i == 0:
                    if now+1 >=n:
                        if now+1 > time:
                            return True
                    else:
                        if first[now+1] == "1" and first_visited[now+1]==False:
                            if now+1 > time:
                                q.append((now+1, True, time+1))
                                first_visited[now+1] = True
                elif i == 1:
                    if first[now-1] == "1" and first_visited[now-1]==False:
                        if now-1 > time:
                            q.append((now-1, True, time+1))
                            first_visited[now-1] = True
                else:
                    # 만약에 뛰어넘는 곳이 인덱스를 넘는 곳이라면
                    if now+k>=n:
                        if now+k > time:
                            return True
                    else:
                        if second[now+k] == "1" and second_visited[now+k]==False:
                            if now+k > time:
                                q.append((now+k, False, time+1))
                                second_visited[now+k] = True
        else:
            for i in range(3):
                if i == 0:
                    if now+1>=n:
                        if now+1 > time:
                            return True
                    else:
                        if second[now+1] == "1" and second_visited[now+1]==False:
                            if now+1 > time:
                                q.append((now+1, False, time+1))
                                second_visited[now+1] = True
                elif i == 1:
                    if second[now-1] == "1" and second_visited[now-1]==False:
                        if now-1 > time:
                            q.append((now-1, False, time+1))
                            second_visited[now-1] = True
                else:
                    # 만약에 뛰어넘는 곳이 인덱스를 넘는 곳이라면
                    if now+k>=n:
                        if now+1 > time:
                            return True
                    else:
                        if first[now+k] == "1" and first_visited[now+k]==False:
                            if now+k > time:
                                q.append((now+k, True, time+1))
                                first_visited[now+k] = True


    return False

print(1 if bfs() == True else 0)