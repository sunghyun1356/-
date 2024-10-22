# 한번에 닫히는 곳을 찾아야한다
# 시작하고 닫히는 곳의 마킹을 해준다
gal = input()
stack = []
line = set()
razor = set()
for i in range(len(gal)):
    if gal[i] == ")":
        # 바로 전이 ( 이 였으면 레이저를 쏜다는 것
        if gal[i-1] == "(":
            razor.add(i)
            stack.pop()
        # 아니라면 시작점과 끝점을 뽑아준다
        else:
            start = stack.pop()
            line.add((start, i))
    
    # 시작점을 넣어준다
    else:
        stack.append(i)
sum = len(line)
for l in line:
    start, end = l
    for r in razor:
        if start<r<end:
            sum+=1
print(sum)