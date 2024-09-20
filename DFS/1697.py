# 판단
# n 차원이 아님 & 
# 각각의 case에 대해서 가장 빠른 시간이 언제 인지 알아야한다

from collections import deque

counting = [0] * 1001
checked = [False] * 100001
q = deque()


sister, brother = map(int, input().split())
q.append((sister, 0))

def BFS(q):
    ans = 100000000000
    while q:
        now, time = q.popleft()
        
        checked[now] = True
        
        if now == brother:
           if ans >= time :
               ans = time
            
            
        # BFS 니까 일단은 담아두자 안간곳이라면 
        
        # 뒤로 이동할 떄
        if now -1 >=0 and not checked[now-1]:
            q.append((now-1, time+1))
        # 앞으로 한칸 이동
        if now + 1 <= 100000 and not checked[now+1]:
            q.append((now+1, time+1))
        # 두배칸 앞으로 이동한다.
        if now * 2 <= 100000 and not checked[now *2]:
            q.append((now *2, time+1))
        
    return ans
print(BFS(q))


