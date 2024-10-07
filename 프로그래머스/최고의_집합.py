def solution(n, s):
    a,b = s//n, s%n
    temp = [a] * n
    for i in range(0,b):
        temp[i]+=1
    temp = sorted(temp)
    if a < 1:
        temp = [-1]
    return temp