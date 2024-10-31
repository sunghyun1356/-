n = int(input())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))
boys.sort()
girls.sort()
answer = 0
start = 0
end = n-1

# 총 가지수를 생각해보자
# 남자중에서 제일 작은 음수, 여자중에 제일 큰 양수 중 만약에 남자의 키가 더 크다면 가능 하지만 반대면 여자쪽꺼 하나 줄여주면 됨
# 남자중에서 가장 큰 양수, 여자중에서 가장 크지만 음수에서 여자의 키가 더 크다면 가능 하지만 반대는 불가능
# 둘다 음수거나 양수면 불가능
while start < n and 0<=end:
    if boys[start]< 0  and 0<girls[end] and abs(boys[start]) > girls[end]:
        answer +=1
        start +=1
        end -=1
    elif boys[start]< 0  and 0<girls[end] and abs(boys[start]) <= girls[end]:
        end -=1
    elif boys[start]> 0  and girls[end]<0 and boys[start] < abs(girls[end]):
        answer +=1
        start +=1
        end -=1
    elif boys[start]> 0  and girls[end]<0 and boys[start] >= abs(girls[end]):
        end -=1
    elif boys[start] < 0 and girls[end] < 0:
        start +=1
    elif boys[start] > 0 and girls[end] > 0:
        end -=1
print(answer)