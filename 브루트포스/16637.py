import sys
input = sys.stdin.readline
n = int(input())
array = [*map(lambda x :int(x) if x.isdigit() else x, input())]
result = -float('inf')

def cal(num1, num2, s):
    if s == "+":
        return num1+num2
    elif s == "-":
        return num1-num2
    else:
        return num1 * num2

def dfs(idx, prev):
    global result
    if idx >= n:
        result = max(result, prev)
        return
    if idx+3 < n:
        dfs(idx+4, cal(prev, cal(array[idx+1], array[idx+3], array[idx+2]), array[idx]))
    dfs(idx+2, cal(prev, array[idx+1], array[idx]))
if n == 1:
    result = array[0]
else:
    dfs(1, array[0])
print(result)