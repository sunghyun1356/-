from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    for key in graph:
        graph[key].sort(reverse=False)
    

    def dfs(path):

        if len(path) == len(tickets) + 1:
            return path
        
        # 마지막으로 간 곳
        current = path[-1]
        destinations = graph[current]
        
        for i, dest in enumerate(destinations):
            graph[current].pop(i)  
            result = dfs(path + [dest])  
            graph[current].insert(i, dest)  
            
            if result:  
                return result
    

    answer = dfs(["ICN"])
    
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
