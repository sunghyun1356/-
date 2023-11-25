"""문제
월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.

예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.

4점, 5점 등은 같은 방법으로 정해진다. 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이라고 본다.

회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.

입력
입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.

출력
첫째 줄에는 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.

예제 입력 1 
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
예제 출력 1 
2 3
2 3 4"""
import sys
input = sys.stdin.readline
from collections import deque, defaultdict
n = int(input())

friends = [[] for _ in range(n+1)]

# 특정 노드부터 시작해서 그것에가 가능범위까지의 max 값을 더하는 것
def BFS(a):
    visited = [-1] * (n+1)
    visited[a] = 0
    q = deque([a])
    while q:
        now = q.popleft()
        for friend in friends[now]:
            if visited[friend] == -1:
                visited[friend] = visited[now] +1
               
                q.append(friend)
    return max(visited)


while True:
    first, second = map(int, input().split())
    if first == -1  and second == -1:
        break
    friends[first].append(second)
    friends[second].append(first)
    
#최대 가장 포인트가 많은 것 부터 작은거 까지 찾으면서 같으면 넣어주기
score = 50
candidate = []

for i in range(1, n+1):
    tmp = BFS(i)
    if tmp < score:
        score = tmp
        candidate = [i]
    elif tmp == score:
        candidate.append(i)

print(score, len(candidate))
print(*candidate)
    

