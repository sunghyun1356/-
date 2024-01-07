from collections import deque
from itertools import combinations
import copy
    
# q에 담고 a공간 b공간 코인 c 그리고 몇번째 판인지를 넣어주는 리스트를 넣어주고 뽑아서 각각에 사용한다


from collections import deque
def first(lst, n):
    result = [list(pair) for pair in combinations(lst, 2) if sum(pair) == n]

    return result
def second(list1, list2, n):
    result = []
    for num1 in list1:
        for num2 in list2:
            if num1 + num2 == n:
                result.append([num1, num2])

    return result

def solution(coin, cards):
    
    n = len(cards)
    s = n+1
    left = cards[n//3:]
    result = []
    
    def BFS(a,b,c,d):

        q = deque()
        q.append([a,b,c,d])
        k = (n - n//3)//2
        while q:
            
            na,nb,nc,nd = q.popleft()
        
            if nd < k:
                if left[nd*2]:
                    nb.append(left[nd*2])
                if left[nd*2+1]:
                    nb.append(left[nd*2+1])
            
            
            if len(first(na,s))!=0:
                for candidate in first(na,s):
                    na = [x for x in na if x != candidate[0] and x != candidate[1]]
                    nd+=1  
                    q.append([na,nb,nc,nd])

            elif len(first(na,s))==0 and len(second(na,nb,s))!=0:
                for candidate in second(na,nb,s):
                    na = [x for x in na if x != candidate[0]]
                    nb = [x for x in nb if  x != candidate[1]]
                    nd+=1
                    nc-=1

                    q.append([na,nb,nc,nd])
            elif len(first(nb,s))!=0:
                for candidate in first(nb,s):
                    nb = [x for x in nb if x != candidate[0] and x != candidate[1]]
                    nd+=1
                    nc-=2

                    q.append([na,nb,nc,nd])
            elif len(first(na,s))==0 and len(first(nb,s))==0 and len(second(na,nb,s))==0 or nc==0:
                result.append(nd)
                break
        return result
    print(max(BFS(cards[:n//3],[],coin,0))+1)          
                    
                
                    
                    

    
                
solution(4,[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
solution(10,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
solution(2,[5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7])
solution(3,[1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12])