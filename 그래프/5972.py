"""문제
농부 현서는 농부 찬홍이에게 택배를 배달해줘야 합니다. 그리고 지금, 갈 준비를 하고 있습니다. 평화롭게 가려면 가는 길에 만나는 모든 소들에게 맛있는 여물을 줘야 합니다. 물론 현서는 구두쇠라서 최소한의 소들을 만나면서 지나가고 싶습니다.

농부 현서에게는 지도가 있습니다. N (1 <= N <= 50,000) 개의 헛간과, 소들의 길인 M (1 <= M <= 50,000) 개의 양방향 길이 그려져 있고, 각각의 길은 C_i (0 <= C_i <= 1,000) 마리의 소가 있습니다. 소들의 길은 두 개의 떨어진 헛간인 A_i 와 B_i (1 <= A_i <= N; 1 <= B_i <= N; A_i != B_i)를 잇습니다. 두 개의 헛간은 하나 이상의 길로 연결되어 있을 수도 있습니다. 농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N에 있습니다.

다음 지도를 참고하세요.

           [2]---
          / |    \
         /1 |     \ 6
        /   |      \
     [1]   0|    --[3]
        \   |   /     \2
        4\  |  /4      [6]
          \ | /       /1
           [4]-----[5] 
                3  
농부 현서가 선택할 수 있는 최선의 통로는 1 -> 2 -> 4 -> 5 -> 6 입니다. 왜냐하면 여물의 총합이 1 + 0 + 3 + 1 = 5 이기 때문입니다.

농부 현서의 지도가 주어지고, 지나가는 길에 소를 만나면 줘야할 여물의 비용이 주어질 때 최소 여물은 얼마일까요? 농부 현서는 가는 길의 길이는 고려하지 않습니다.

입력
첫째 줄에 N과 M이 공백을 사이에 두고 주어집니다.

둘째 줄부터 M+1번째 줄까지 세 개의 정수 A_i, B_i, C_i가 주어집니다.

출력
첫째 줄에 농부 현서가 가져가야 될 최소 여물을 출력합니다.

예제 입력 1 
6 8
4 5 3
2 4 0
4 1 4
2 1 1
5 6 1
3 6 2
3 2 6
3 4 4
예제 출력 1 
5
출처
Olympiad > USA Computing Olympiad > 2010-2011 Season > USACO March 2011 Contest > Silver 2번

문제를 번역한 사람: baemin0103
알고리즘 분류
그래프 이론
데이크스트라
최단 경로"""

# 사이클을 도므로, 가장 짧은 것을구하기 위해서는 다익스트라를 이용하자

import sys
input = sys.stdin.readline
import heapq



n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
# 가장 짧은 거리 구할거니까 distance는 최댓값으로 초기화
distance = [1e9]*(n+1)

def dijkstra(start):
    heap = []
    # 값과 시작지점을 넣음
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        # 현재 값과, 현재 출발지점
        now_value , now_dest = heapq.heappop(heap)
        if distance[now_dest] < now_value:
            continue
        # 출발지점에 도착했을 때의 각각의 목적지와 값
        for dest, value in graph[now_dest]:
            # 총 값은 그 전의 값+지금의 값
            cost = now_value+value
            # 만약 이 값이 이미 저장되있는 것보다 작으면
            if cost < distance[dest]:
                # 새로운 도착지의 값은 그 값으로 된다
                distance[dest] = cost
                # 그리고 다시 그 값 이랑 cost 넣어주기
                heapq.heappush(heap,(cost,dest))

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
dijkstra(1)
print(distance[n])
    


    

    
    