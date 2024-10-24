from itertools import combinations

n = int(input())
check_points = []
for _ in range(n):
    x, y = map(int, input().split())
    check_points.append((x,y))
total = 0
for i in range(1,n):
    total += abs(check_points[i][0] - check_points[i-1][0]) + abs(check_points[i][1] - check_points[i-1][1])
mock = 0
answer = 0
for i in range(1,n-1):
    atob = abs(check_points[i][0] - check_points[i-1][0]) + abs(check_points[i][1] - check_points[i-1][1])
    btoc = abs(check_points[i+1][0] - check_points[i][0]) + abs(check_points[i+1][1] - check_points[i][1])
    atoc = abs(check_points[i-1][0] - check_points[i+1][0]) + abs(check_points[i+1][1] - check_points[i-1][1])
    result = abs(atoc - (atob + btoc))
    mock = max(mock, result)

print(total-mock)