import heapq
heap = []
n = int(input())
time = []

for _ in range(n):
    time.append(list(map(int, input().split())))
time = sorted(time, key = lambda x : (x[1], x[0]))
# 제일 빨리 끝나는 것
heap = [time[0][1]]
for i in range(1,n):
    if heap[0] <= time[i][0]:
        for j in range(len(heap)-1,-1,-1):
            if heap[j] <= time[i][0]:
                heapq.heappop(heap)
                break
    heapq.heappush(heap, time[i][1])
print(len(heap))