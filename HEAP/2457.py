n = int(input())
flowers = []
thirty = [4, 6, 9, 11]
thirty_one = [1, 3, 5, 7, 8, 10, 12]

# 꽃들의 정보 입력
for _ in range(n):
    flowers.append(list(map(int, input().split())))

flowers.sort(key=lambda x: (x[0], x[1]))

current_end = 301  
last_end = 1130 
max_end = 0
count = 0
idx = 0

while current_end <= last_end:
    found = False
    # 시작점이 현재 마지막 시간대보다 작거나 같아야하고
    # 이렇게 되는 것들 중에서 마지막 시간대의 max를 찾아준다.
    # 
    while idx < n and (flowers[idx][0] * 100 + flowers[idx][1]) <= current_end:
        max_end = max(max_end, flowers[idx][2] * 100 + flowers[idx][3])
        idx += 1
        found = True
    
    if not found:
        print(0)
        exit()

    count += 1
    current_end = max_end

print(count)
