# 앞에서 부터 움직이면서 stack에 담아놨다가 그게 나오면 바로 원래 있던거를 pop해준다
n = int(input())
result = 0
for _ in range(n):
    stack  = []
    words = input()
    for word in words:
        if len(stack) == 0:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    if len(stack) == 0:
        result+=1
print(result)