import sys
from collections import deque

input = sys.stdin.readline

s = int(input().strip())

MAX = 1000  
visited = [[False] * (MAX + 1) for _ in range(MAX + 1)]

def bfs():
    q = deque([(1, 0, 0)])
    visited[1][0] = True

    while q:
        screen_now, clip_board_now, time_now = q.popleft()

        if screen_now == s:
            return time_now

        if screen_now <= MAX:
            clip_board_next = screen_now
            if not visited[screen_now][clip_board_next]:
                visited[screen_now][clip_board_next] = True
                q.append((screen_now, clip_board_next, time_now + 1))

        if clip_board_now > 0 and screen_now + clip_board_now <= MAX:
            screen_next = screen_now + clip_board_now
            if not visited[screen_next][clip_board_now]:
                visited[screen_next][clip_board_now] = True
                q.append((screen_next, clip_board_now, time_now + 1))

        if screen_now > 0:
            screen_next = screen_now - 1
            if not visited[screen_next][clip_board_now]:
                visited[screen_next][clip_board_now] = True
                q.append((screen_next, clip_board_now, time_now + 1))

result = bfs()
print(result)
