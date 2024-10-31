long = list(input())
short = input()
answer = 0
i =0
if len(long)<len(short):
    print(0)
else:
    while i<=len(long)-len(short):
        if long[i:i+len(short)] == list(short):
            answer +=1
            for _ in range(len(short)):
                i+=1
        else:
            i+=1

    print(answer)