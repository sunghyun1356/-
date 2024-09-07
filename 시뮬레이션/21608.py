"""문제
상어 초등학교에는 교실이 하나 있고, 교실은 N×N 크기의 격자로 나타낼 수 있다. 학교에 다니는 학생의 수는 N2명이다. 오늘은 모든 학생의 자리를 정하는 날이다. 학생은 1번부터 N2번까지 번호가 매겨져 있고, (r, c)는 r행 c열을 의미한다. 교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다.

선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다. 이제 다음과 같은 규칙을 이용해 정해진 순서대로 학생의 자리를 정하려고 한다. 한 칸에는 학생 한 명의 자리만 있을 수 있고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.

비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
예를 들어, N = 3이고, 학생 N2명의 순서와 각 학생이 좋아하는 학생이 다음과 같은 경우를 생각해보자.

학생의 번호	좋아하는 학생의 번호
4	2, 5, 1, 7
3	1, 9, 4, 5
9	8, 1, 2, 3
8	1, 9, 3, 4
7	2, 3, 4, 8
1	9, 2, 5, 7
6	5, 2, 3, 4
5	1, 9, 2, 8
2	9, 3, 1, 4
가장 먼저, 4번 학생의 자리를 정해야 한다. 현재 교실의 모든 칸은 빈 칸이다. 2번 조건에 의해 인접한 칸 중에서 비어있는 칸이 가장 많은 칸인 (2, 2)이 4번 학생의 자리가 된다.

 	 	 
 	4	 
 	 	 
다음 학생은 3번이다. 1번 조건을 만족하는 칸은 (1, 2), (2, 1), (2, 3), (3, 2) 이다. 이 칸은 모두 비어있는 인접한 칸이 2개이다. 따라서, 3번 조건에 의해 (1, 2)가 3번 학생의 자리가 된다.

 	3	 
 	4	 
 	 	 
다음은 9번 학생이다. 9번 학생이 좋아하는 학생의 번호는 8, 1, 2, 3이고, 이 중에 3은 자리에 앉아있다. 좋아하는 학생이 가장 많이 인접한 칸은 (1, 1), (1, 3)이다. 두 칸 모두 비어있는 인접한 칸이 1개이고, 행의 번호도 1이다. 따라서, 3번 조건에 의해 (1, 1)이 9번 학생의 자리가 된다.

9	3	 
 	4	 
 	 	 
이번에 자리를 정할 학생은 8번 학생이다. (2, 1)이 8번 학생이 좋아하는 학생과 가장 많이 인접한 칸이기 때문에, 여기가 그 학생의 자리이다.

9	3	 
8	4	 
 	 	 
7번 학생의 자리를 정해보자. 1번 조건을 만족하는 칸은 (1, 3), (2, 3), (3, 1), (3, 2)로 총 4개가 있고, 비어있는 칸과 가장 많이 인접한 칸은 (2, 3), (3, 2)이다. 행의 번호가 작은 (2, 3)이 7번 학생의 자리가 된다.

9	3	 
8	4	7
 	 	 
이런식으로 학생의 자리를 모두 정하면 다음과 같다.

9	3	2
8	4	7
5	6	1
이제 학생의 만족도를 구해야 한다. 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다. 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다. 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.

학생의 만족도의 총 합을 구해보자.

입력
첫째 줄에 N이 주어진다. 둘째 줄부터 N2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다.

학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생으로 이루어져 있다. 입력으로 주어지는 학생의 번호, 좋아하는 학생의 번호는 N2보다 작거나 같은 자연수이다. 어떤 학생이 자기 자신을 좋아하는 경우는 없다.

출력
첫째 줄에 학생의 만족도의 총 합을 출력한다.

제한
3 ≤ N ≤ 20
예제 입력 1 
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4
예제 출력 1 
54
예제 입력 2 
3
4 2 5 1 7
2 1 9 4 5
5 8 1 4 3
1 2 9 3 4
7 2 3 4 8
9 8 4 5 7
6 5 2 3 4
8 4 9 2 1
3 9 2 1 4
예제 출력 2 
1053"""
# 1. 가장 인접한 칸이 많은 것 넣을 리스트
# 2. 좋아하는 학생이 인접한 칸에 많은지를 확인
# 3. 행, 열의 크기가 가장 작은 것으로 본다
import sys
from collections import Counter
from collections import defaultdict

n = int(input())
friends = {}
friend_order = []
friend_graph = [[0] * n for _  in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n**2):
    friend = list(map(int, input().split()))
    friends[friend[0]] = friend[1:]
    friend_order.append(friend[0])

def first_check(frined_number):

    # 만약에 아예 비어있는 경우는 다 비어있는 공간 중에서 제일 작은 것을 체크
    friend_location_candidate = []
    friend_candidate = friends[frined_number]
    
    for i in range(n):
        for j in range(n):
            if friend_graph[i][j] in friend_candidate:
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0<=ny<n and 0<=nx<n:
                        if friend_graph[ny][nx] == 0:
                            friend_location_candidate.append((ny,nx))
    if len(friend_location_candidate) == 0:
        temp = True
        for i in range(n):
            for j in range(n):
                if friend_graph[i][j] == 0:
                    for k in range(4):
                        ny = i + dy[k]
                        nx = j + dx[k]
                        if 0<=ny<n and 0<=nx<n:
                            if friend_graph[ny][nx] != 0:
                                temp = False
                        else:
                            temp = False
                    if temp == True:
                        friend_location_candidate.append((i,j))
                        break
            if temp == True:
                break
    frequency = Counter(friend_location_candidate)
    print(friend_location_candidate)
    max_count = max(frequency.values())
    most_common = [item for item, count in frequency.items() if count == max_count]
    print(most_common)
    return most_common                       
    

def second_check(most_common):

    count_dict = defaultdict(int)

    for location in most_common:
        y, x = location
        local_count = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if friend_graph[ny][nx] == 0:
                    local_count += 1
        count_dict[(y, x)] = local_count

    # 가장 높은 count 값을 찾기
    max_count = max(count_dict.values(), default=0)

    # 가장 높은 count 값을 가진 (y, x) 좌표들만 필터링
    most_frequent_locations = [loc for loc, count in count_dict.items() if count == max_count]

    return most_frequent_locations

def third_check(most_injust_common):
    minimum_y, minimum_x = 1e9,1e9
    for location in most_injust_common:
        y,x = location
        if minimum_y > y:
            minimum_y = y 
            minimum_x = x
        elif minimum_y == y:
            if minimum_x > x:
                 minimum_y = y
                 minimum_x = x
    return (minimum_y, minimum_x)

# 각각 친구가 인접할 때 친한친구가 인접한 (거리가 1)인 거리에 앉는 친구의 수가 1이면 1, 2면 10, 3이면 100 4면 1000이된다
def calculate_satisfaction(friend_graph):
    satisfaction = 0
    for i in range(n):
        for j in range(n):
            student = friend_graph[i][j]
            if student != 0:
                favorite_friends = friends[student]
                count = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < n and 0 <= nx < n and friend_graph[ny][nx] in favorite_friends:
                        count += 1
                satisfaction += 10 ** (count - 1) if count > 0 else 0
    return satisfaction

def main(friends, friends_order):
    for fireind in friends_order:
        a = first_check(fireind)
        if len(a) > 1 or len(a)== 0:
            a = second_check(a)
            if len(a) > 1 or len(a) == 0:
                a = third_check(a)
        y,x = a[0]
        friend_graph[y][x] = friend
    return friend_graph
friend_graph = main(friends, friend_order)
calculate_satisfaction(friend_graph)