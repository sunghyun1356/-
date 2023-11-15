"""문제
 
$N$개의 노드로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.

입력
첫째 줄에 노드의 개수 
$N$과 거리를 알고 싶은 노드 쌍의 개수 
$M$이 입력되고 다음 
$N-1$개의 줄에 트리 상에 연결된 두 점과 거리를 입력받는다. 그 다음 줄에는 거리를 알고 싶은 
$M$개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.

출력
 
$M$개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.

제한
 
$2≤N≤1\,000$ 
 
$1≤M≤1\,000$
트리 상에 연결된 두 점과 거리는 
$10\,000$ 이하인 자연수이다.
트리 노드의 번호는 
$1$부터 
$N$까지 자연수이며, 두 노드가 같은 번호를 갖는 경우는 없다.
예제 입력 1 
4 2
2 1 2
4 3 2
1 4 3
1 2
3 2
예제 출력 1 
2
7"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    f, s, d = map(int, input().split())
    graph[f].append((s, d))
    graph[s].append((f, d))

def cal(a, b, d):
    distance = 0
    q = deque()
    q.append((a, b, 0))
    check = [False] * (n + 1)

    while q:
        first, destination, dists = q.popleft()

        for i in graph[first]:
            second, weight = i
            if not check[second]:
                new_dists = dists + weight
                check[second] = True
                if second == destination:
                    distance = new_dists
                    return distance
                else:
                    q.append((second, destination, new_dists))
    return distance

distance = []
for j in range(m):
    first, second = map(int, input().split())
    distance.append(cal(first, second, 0))
    print(distance[j])


