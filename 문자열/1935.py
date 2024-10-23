n = int(input()) 
words = list(input())
alpha = {}
for i in range(n):
    alpha[chr(65 + i)] = int(input())



stack = []

for k in range(len(words)):
    if words[k] in ["*", "%", "/", "+", "-"]:
         
        first = stack.pop()   
        second = stack.pop() 
        
        if words[k] == "*":
            stack.append(second * first)
        elif words[k] == "/":
            stack.append(second / first)
        elif words[k] == "+":
            stack.append(second + first)
        elif words[k] == "-":
            stack.append(second - first)
    else:
        stack.append(alpha[words[k]]) 

print(f"{stack[-1]:.2f}")
