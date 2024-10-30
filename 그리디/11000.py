import sys, heapq
N = int(sys.stdin.readline())
lecture = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
room = []
heapq.heappush(room,lecture[0][1]) # 첫 강의 끝나는 시간

for i in range(1,N):
    if lecture[i][0] < room[0]: 
        heapq.heappush(room, lecture[i][1]) 
    else: 
        heapq.heappop(room) 
        heapq.heappush(room, lecture[i][1]) 
        
print(len(room))
