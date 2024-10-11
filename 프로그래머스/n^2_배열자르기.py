def solution(n, left, right):
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            graph[i][j] = i+1
        k = j
        for j in range(k,n):
            graph[i][j] = graph[i][j-1] + 1
    total = []
    for gra in graph:
        total.append(gra)
    graph = total
            
    answer = graph[left:right+1]
    return graph

print(solution(3,2,5))