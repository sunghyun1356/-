n1, n2 = map(int, input().split())
first = list(input())
first = first[::-1]
second = list(input())
value = {}
for f in first:
    value[f] = 1
for s in second:
    value[s] = -1


time = int(input())
total = first+second
# 횟수만큼 진행한다

for i in range(time):
    i = 0
    while i < len(total) -1 :
        if i >= len(total):
            break
        if value[total[i]]==1 and value[total[i+1]] == -1:
            total[i], total[i+1] = total[i+1], total[i]
            i+=2
        else:
            i+=1

for a in total:
    print(a, end = "")
