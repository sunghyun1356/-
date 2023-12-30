import heapq

# heapq를 통해서 최소나 최대를 바로 뽑아내자
# 시작하는 시간과 지금 현재 시간 사이에서 jobs이 시작 가능의 상태면 넣어준다.
# 시간이 제일 적게 걸리는 것을 뽑아준다.]
# 시작시간은 현재시간으로 변경되고 지금 시간은 시작한 시간 + 걸린시간이 된다
def solution(jobs):
    
    answer = 0
    heap = []
    now = 0
    i = 0
    start = -1
    while i<len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1],j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start =now
            now += current[0]
            answer += (now-current[1])
            i+=1
        else:
            now+=1
    
    return int(answer / len(jobs))
