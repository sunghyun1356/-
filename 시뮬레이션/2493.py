"""문제
KOI 통신연구소는 레이저를 이용한 새로운 비밀 통신 시스템 개발을 위한 실험을 하고 있다. 실험을 위하여 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 각 탑의 꼭대기에 레이저 송신기를 설치하였다. 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다. 

예를 들어 높이가 6, 9, 5, 7, 4인 다섯 개의 탑이 수평 직선에 일렬로 서 있고, 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로 동시에 레이저 신호를 발사한다고 하자. 그러면, 높이가 4인 다섯 번째 탑에서 발사한 레이저 신호는 높이가 7인 네 번째 탑이 수신을 하고, 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신을 한다. 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신을 하지 못한다.

탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라. 

입력
첫째 줄에 탑의 수를 나타내는 정수 N이 주어진다. N은 1 이상 500,000 이하이다. 둘째 줄에는 N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어진다. 탑들의 높이는 1 이상 100,000,000 이하의 정수이다.

출력
첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다. 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
6 9 5 7 4
예제 출력 1 
0 0 2 2 4"""

# 역순으로 계산 한다. 각각을 업데이트 시켜줘야 한다
# 역순으로 max값을 각각 계산해주고 자기보다 큰게 나오면 그 인덱스에 해당하는 것들은 결국 거기에 포함, 근데 중간에 껴있는 애들은?

n = int(input())
top = list(map(int, input().split()))
stack = []
for i in range(n):
    stack.append([i,top[i]])
result = [0 for _ in range(n+1)]
storage = []
edge = stack.pop()# 맨처음 기준이 될 것
storage.append(edge)
for i in range(n-2,0,-1):# 맨 마지막꺼 꺼냈으니까 마지막 앞꺼로 기준이 잡아진다.
    if len(storage) == 0:
        a = stack.pop()
        storage.append(a)
    else:
        standard = stack.pop()
        while True: # 들어 있는 동안은
            edge = storage.pop() # 오른쪽
             # 왼쪽
            if standard[1] > edge[1]: # 왼쪽이 오른쪽 보다 더 크면 오른쪽 값은 그대로 저장
                result[edge[0]] = i+1
                if len(storage)==0:
                    storage.append(standard)
            else:
                storage.append(edge)
                storage.append(standard)
                break
for i in range(n):
    print(result[i], end=" ")

        
n = int(input())
top = list(map(int, input().split()))

result = [0 for _ in range(n)]  # 결과를 저장할 리스트

stack = []  # 스택을 이용하여 이전에 탐색한 탑들을 저장

for i in range(n-1, -1, -1):  # 역순으로 탑을 확인
    current_height = top[i]

    while stack:
        if stack[-1][1] < current_height:  # 현재 탑이 더 높으면
            result[stack.pop()[0]] = i+1  # 수신 가능한 탑으로 처리
        else:
            break  # 현재 탑이 더 낮으면 이후에도 수신 불가능하므로 스택에서 제거

    stack.append((i, current_height))  # 현재 탑을 스택에 추가

for r in result:
    print(r, end=" ")

        
    
    

# 스택에 모든걸 넣고 하나씩 빼는데 뺀거 보다 큰게 마지막이면 다시 넣는다
# 스택을 두개 사용한다
# 0 0 1 2 1 4
# 6 9 5 3 7 4     ||        4
# 6 9 5 3            ||     edge     7         ||   확정      4        4가 7보다 작으니까
# 6 9 5         ||        73      ||          43
# 6 9                 ||   7   5



