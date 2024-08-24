import sys
input = sys.stdin.readline
from collections import Counter

def checking(graph, r, c, k):
    if graph[r][c] == k:
        return True
    return False

def r_change(graph):
    new_graph = []
    for i in graph:
        elem = set(i)
        temp = []
        new_temp = []
        for j in elem:
            if j == 0:
                continue
            cnt = i.count(j)
            temp.append((j,cnt))
        temp.sort(key= lambda x : (x[1], x[0]))

        for k in temp:
            new_temp.append(k[0])
            new_temp.append(k[1])
        new_temp = new_temp[:100]
        new_graph.append(new_temp)
    
    max_len = max(map(len, new_graph))

    for i in range(len(new_graph)):
        while len(new_graph[i]) != max_len:
            new_graph[i].append(0)
    return new_graph

def main():
    r,c,k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(3)]
    r_len = len(graph)
    c_len = len(graph[0])
    
    for i in range(101):
        if graph[r-1][c-1] == k:
            print(i)
            break
        if len(graph[0]) > len(graph):
            graph = r_change(graph)
        else:
            graph = r_change(graph)
        if i == 101:
            print(-1)
            
    if r_len >= c_len:
        graph = list(map(list, zip(*graph)))
        r_change(graph)
        graph = list(map(list, zip(*graph)))
    else:
        r_change(graph)

if __name__ == "__main__":
    main()