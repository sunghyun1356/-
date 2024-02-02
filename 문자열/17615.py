import sys
N = int(sys.stdin.readline().strip())
balls = str(sys.stdin.readline().strip())
cnt = []

# 몇개를 옮겨야하는가

# 우측으로 레드 모으기
rexplore = balls.rstrip('R')
print(rexplore)
cnt.append(rexplore.count('R'))

# 우측으로 블루 모으기
rexplore = balls.rstrip('B')
print(rexplore)
cnt.append(rexplore.count('B'))

# 좌측으로 레드 모으기
lexplore = balls.lstrip('R')
print(lexplore)
cnt.append(lexplore.count('R'))

# 좌측으로 블루 모으기
lexplore = balls.lstrip('B')
print(lexplore)
cnt.append(lexplore.count('B'))

print(min(cnt))