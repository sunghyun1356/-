import sys
input = sys.stdin.readline

words = input()
# 띄엄 띄엄 부분을 알아서 계산하기

zero = 0
one = 0
s = words[0]

if s == '0':
    temp = '0'
else:
    temp = '1'
for i in range(1,len(words)):
    if words[i] !=temp and temp == '0':
        one+=1
    elif words[i] !=temp and temp == '1':
        zero+=1
    temp = words[i]
print(min(zero, one))