import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
location = list(map(int, input().split()))

if len(location) == 1:
    standard = max(location[0] - 0, n-location[0])
else:
    for i in range(location):
        if i == 0:
            height = location[i] - 0
        elif i == len(location) -1:
            height = n - location[i]
        else:
            temp = location[i] - location[i-1]
            if temp %2:
                height = temp // 2 +1
            else:
                height = temp //2
        standard = max(height,standard)
print(standard)