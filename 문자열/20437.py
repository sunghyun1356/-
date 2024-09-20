
# k의 개수부터 시작해서 뒤로 한칸 움직이면서 set에 포함이 되어있는지 확인한다
# 만약에 되어있다면 그 문자까지 앞을 당겨서 그 문자열에 대한 것을 candidate에 넣어주고 len값도 넣어준다
# k의 개수가 포함만되어있으면 되니까 만약에 그 값에 대해서 하나씩 처리를 해준다

"""def checking(w,k):
    result =  {}
    candidate = {}
    start = 0
    end = k
    for i in range(len(w)):
        if w[i] not in candidate:
            candidate[w[i]] = 0
            candidate[w[i]]+=1
            result[w[i]] = []
        else:
            candidate[w[i]]+=1
            if candidate[w[i]] == k:
                result[w[i]].append(w[start:end+1])
    
    
    if len(result) == 0:
        return -1
    else:
        minimum = 1e9
        maximum = 0
        for i in result:
            for j in i:
                if maximum < len(j):
                    maximum = len(j)
                if minimum > len(j):
                    minimum = len(j)
        return (minimum, maximum)"""


# 슬라이딩 윈도우로 맨처음의 max, min을 구하고 이 길이만큼 슬라이딩을 해준다
# 뒤로 이동하고 앞의
"""def checking(w,k):
    # 맨처음 기준 = standard
    start = 0
    end = 1
    minimum = len(w)
    maximum =0
    dulplicated = {}
    while start < end:
        if w[end] not in dulplicated:
            dulplicated[w[end]] = 0
            dulplicated[w[end]] +=1
            end+=1
        elif w[end] in dulplicated and dulplicated[w[end]] !=k:
            dulplicated[w[end]]+=1
            end+=1
        elif w[end] in dulplicated and dulplicated[w[end]] == k:
            if (end-start) >= maximum:
                maximum = end-start
                start+=1
                dulplicated[w[end]]-=1
                end+=1
            elif end-start <= minimum:
                minimum = end-start
                maximum = end-start
                start+=1
                dulplicated[w[end]]-=1
                end+=1
    return(minimum, maximum)    """
    

# 각각의 개수와 index를 모두다 저장해주고
# k개가 만족되는 것들에 대해서 각각의 index 값을 통해 길이를 구해준다

def checking(w,k):
    if k == 1:
        result.append([1,1])
    else:
        dulplicated ={}
        maximum = 0
        minimum = 1e9
        for i,j in enumerate(w):
            if j not in dulplicated:
                dulplicated[j] = []
                dulplicated[j].append(i)
            elif j in dulplicated:
                dulplicated[j].append(i)
        for a in dulplicated:
            if len(dulplicated[a])>=k:
                start = 0
                end = k-1
                for m in range(len(dulplicated[a])-k+1):
                    standard = dulplicated[a][end] - dulplicated[a][start]
                    if standard >= maximum:
                        maximum = standard
                    if standard <= minimum:
                        minimum = standard
                    start+=1
                    end+=1     
        if maximum == 0 or minimum == 1e9:
            result.append(-1)
        else:
            result.append([minimum+1,maximum+1])

result = []

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    checking(w,k)
for res in result:
    if res == -1:
        print(res)
    else:
        print(*res)