from collections import deque
import heapq

# BFS 탐색 함수
def bfs(start_y, start_x, target_y=None, target_x=None):
    queue = deque([(start_y, start_x)])
    distances = [[-1] * n for _ in range(n)]  # 거리를 -1로 초기화
    distances[start_y][start_x] = 0
    
    while queue:
        y, x = queue.popleft()
        
        # 목표 지점에 도달했으면 그 거리를 반환
        if target_y is not None and y == target_y and x == target_x:
            return distances[y][x]
        
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 0 and distances[ny][nx] == -1:
                distances[ny][nx] = distances[y][x] + 1
                queue.append((ny, nx))
    
    # 목적지까지의 경로가 없는 경우
    if target_y is not None and target_x is not None:
        return -1  # 목적지까지 도달할 수 없는 경우
    return distances  # 전체 맵에 대한 거리 반환

def main(n, m, fuel, graph, taxi_y, taxi_x, passengers):
    while fuel > 0 and passengers:
        # 택시 위치에서 모든 승객에 대한 거리를 구함
        distances_to_passengers = bfs(taxi_y, taxi_x)
        pq = []
        
        for idx, (a_y, a_x, b_y, b_x) in enumerate(passengers):
            dist_to_passenger = distances_to_passengers[a_y-1][a_x-1]
            if dist_to_passenger != -1:
                # 승객까지의 거리, 승객의 출발지와 목적지 좌표, 승객 인덱스를 우선순위 큐에 넣음
                heapq.heappush(pq, (dist_to_passenger, a_y-1, a_x-1, b_y-1, b_x-1, idx))
        
        if not pq:  # 택시가 도달할 수 있는 승객이 없는 경우
            print(-1)
            return
        
        # 가장 가까운 승객 선택
        dist_to_passenger, a_y, a_x, b_y, b_x, passenger_idx = heapq.heappop(pq)
        
        # 승객을 데리러 가는 연료가 부족한 경우
        if fuel < dist_to_passenger:
            print(-1)
            return
        
        # 승객을 태우러 감
        fuel -= dist_to_passenger
        dist_to_destination = bfs(a_y, a_x, b_y, b_x)
        
        # 목적지까지 갈 수 없으면 실패
        if dist_to_destination == -1 or fuel < dist_to_destination:
            print(-1)
            return
        
        # 목적지까지 태워다 줌
        fuel -= dist_to_destination
        fuel += dist_to_destination * 2  # 목적지 도착 후 연료 충전
        taxi_y, taxi_x = b_y, b_x  # 택시의 위치를 승객 목적지로 업데이트
        
        # 승객 제거
        passengers.pop(passenger_idx)

    # 남은 연료 출력
    if passengers:
        print(-1)  # 승객을 다 태우지 못했으면 실패
    else:
        print(fuel)

if __name__ == "__main__":
    n, m, fuel = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    taxi_y, taxi_x = map(int, input().split())
    passengers = [tuple(map(int, input().split())) for _ in range(m)]
    main(n, m, fuel, graph, taxi_y-1, taxi_x-1, passengers)
