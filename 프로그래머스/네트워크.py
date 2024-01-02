"""문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
입출력 예 설명
예제 #1
아래와 같이 2개의 네트워크가 있습니다.
image0.png

예제 #2
아래와 같이 1개의 네트워크가 있습니다.
image1.png"""

#연결되어있는 개수를 구하기
# find, union으로 그냥 parent의 개수를 구하면 되지 않을까?
# parent의 개수를 구할 때 그냥 바로 구하는 것이 아니라 find를 통해서 한번 거치고 해야한다
def solution(n, computers):
    
    def find(parent, x):
        if parent[x] == x:
            return parent[x]
        parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        
        if rank[xroot] >= rank[yroot]:
            parent[yroot] = parent[xroot]
        
        else:
            parent[yroot] = xroot
    parent = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j] == 1:
                ir , ij = find(parent, i), find(parent, j)
                if ir == ij:
                    continue
                union(parent,i,j)
    
    parents = set()
    for i in range(n):
        parents.add(find(parent, parent[i]))
    
    answer = len(parents)
    return answer