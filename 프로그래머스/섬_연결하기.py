def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif parent[xroot] == parent[yroot]:
        rank[yroot]+=1
    else:
        parent[yroot] = xroot
    
def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    
    rank = [0] * n
    
    answer = 0
    edges = 0
    for i in costs:
        if edges == n-1:
            break
        
        x = find(parent, i[0])
        y = find(parent, i[1])
        
        if x!=y:
            union(parent, rank, x, y)
            answer +=i[2]
        edges+=1
    return answer