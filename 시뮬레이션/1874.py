n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

i = 1
stack_stack = []
result = []

now = stack.pop(0)

while True:
    # 스택이 비어 있거나, 현재 값보다 작은 경우에 push를 해준다
    if len(stack_stack) == 0 or stack_stack[-1] < now:
        stack_stack.append(i)
        result.append("+")
        i += 1
    # 스택의 마지막 값이 현재 찾고 있는 값과 같다면 pop 해준다
    elif stack_stack[-1] == now:
        stack_stack.pop()
        result.append("-")
        if len(stack) == 0:
            break
        now = stack.pop(0)
    # 스택의 마지막 값이 현재 값보다 큰 경우 pop을 해준다
    else:
        stack_stack.pop()
        result.append("-")
    
    # 잘못된 경우를 처리
    if len(stack_stack) == 0 and i > n:
        result = ["NO"]
        break

for r in result:
    print(r)
