def check(s):
    stack = []
    for i in range(len(s)):
        if s[i] == ")":
            if len(stack)>0:
                stack.pop()
            else:
                return "NO"
        else:
            stack.append(s[i])
    if len(stack) >0:
        return "NO"
    else:
        return "YES"



n = int(input())
for _ in range(n):
    print(check(input()))