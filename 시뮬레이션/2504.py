words = input()
stack = []
value = 0
# 괄호를 계산해주고 다시 stack에 넣어서 다음 결과값으로 참조할 수 있도록 만들기
for i in range(len(words)):
    if words[i] == ")":
        val = 0
        while True:
            if len(stack) <= 0:
                print(0)
                exit()
            now = stack.pop()
            if now == "(":
                if val == 0:
                    stack.append(2)
                else:
                    stack.append(val*2)
                break
            elif now != "(" and now!= "[" and now != "]" and now !=")":
                val += now
        
    elif words[i] == "]":
        val = 0
        while True:
            if len(stack) <= 0:
                print(0)
                exit()
            now = stack.pop()
            if now == "[":
                if val == 0:
                    stack.append(3)
                else:
                    stack.append(val*3)
                break
            elif now != "]" and now!= "(" and now != ")" and now != "[":
                val += now
    else:
        stack.append(words[i])
result = 0
for i in range(len(stack)):
    if stack[i] != "]" and stack[i]!= "(" and stack[i] != ")" and stack[i] != "[":
        result += stack[i]
    else:
        print(0)
        break
print(result)