import sys
input = sys.stdin.readline

villiage = []
all_people = 0

N = int(input())

for i in range(N):
    n_viliage, people = map(int, input().split())
    villiage.append([n_viliage, people])
    all_people += people

villiage.sort(key= lambda x: x[0]) # 이 부분

count = 0
for i in range(N):
    count += villiage[i][1]
    if count >= all_people/2:
        print (villiage[i][0])
        break

    # 간단히 생각해서 사람들간의 abs의 합이 제일 적어야하니까 이때의 인구의 절발이 넘어갈때를 체크